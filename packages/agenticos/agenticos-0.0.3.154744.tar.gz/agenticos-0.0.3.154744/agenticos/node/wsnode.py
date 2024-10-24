import json
import logging
from threading import Event, Lock, Thread
from uuid import UUID
import datetime, time

import websocket

from agenticos.node.http_support import HTTPHealthServer
from agenticos.node.models import *
from agenticos.connectors import BaseWorkflowConfig, BaseWorkflowRunner
from agenticos.node.settings import settings

log = logging.getLogger(__name__)
tasks: dict[UUID, Task] = {}

ID_FILE = ".node_id"


class RepeatTimer(Thread):
    def __init__(self, event, callback, frequency=30):
        Thread.__init__(self)
        self._stopped = event
        self._callback = callback
        self._frequency = frequency

    def run(self):
        while True:
            self._callback()
            if self._stopped.wait(self._frequency):
                print("@stopping@")
                break


class WSNode:
    def __init__(self, registry: str, config: AgenticConfig):
        self.registry = registry
        self.config = config
        print("Config", config.model_dump())
        self.lock = Lock()
        self.id = None

    def run_task(self, workflow: BaseWorkflowConfig, task: Task) -> None:
        wr = workflow.new_runner()
        task.output = None
        steps = [False] * len(workflow.steps_description())

        def follow_workflow():
            nonlocal workflow, self
            for step_idx, step_output in enumerate(wr.step_output()):
                if steps[step_idx]:
                    continue
                steps[step_idx] = True
                task.output = step_output
                step_finished_msg = StepFinishedMessage(
                    task_id=str(task.id),
                    step=step_idx,
                    result=step_output,
                )
                self.send_ws_message(json.dumps(step_finished_msg.model_dump()))

        try:
            stopFlag = Event()
            thread = RepeatTimer(stopFlag, follow_workflow, 1)
            thread.start()
            time.sleep(0.5)
            wr.start(inputs=task.inputs)
            task.status = TaskStatus.COMPLETED
        except Exception as e:
            task.output = str(e)
            task.status = TaskStatus.FAILED
        finally:
            time.sleep(1)
            stopFlag.set()

    def on_message(self, ws, msg):
        message = json.loads(msg)
        if "type" not in message:
            log.warning("Unknown message format", message)
        if message["type"] == MSG_HS_ACK:
            log.info("Handshake successful")
            self.id = message["id"]
            # Write the id to ID_FILE
            with open(ID_FILE, "w") as f:
                f.write(self.id)
        elif message["type"] == MSG_TASK_REQ:
            log.debug("Task request: ", message)
            t_req = AgenticTaskRequestMessage(**message)
            task = Task(
                id=t_req.task.task_id,
                inputs=t_req.task.inputs,
                status=TaskStatus.RUNNING,
                output="",
            )
            tasks[t_req.task.task_id] = task
            workflow = self.config.workflows[t_req.task.workflow]
            thread = Thread(target=self.run_and_report, args=(workflow, task))
            thread.start()

    def run_and_report(self, workflow: BaseWorkflowConfig, task: Task):
        log.debug("Running task", task.id)
        self.run_task(workflow, task)
        tf_msg = TaskFinishedMessage(
            task_id=str(task.id), status=task.status, result=task.output
        )
        time.sleep(1)
        log.debug("Sending task finished message", tf_msg.model_dump())
        self.send_ws_message(json.dumps(tf_msg.model_dump()))

    def send_ws_message(self, message):
        # Make sure that only one thread is sending messages at a time
        with self.lock:
            log.debug(
                f"Sending message: {message}",
            )
            self.ws.send(message)

    def on_error(self, ws, error):
        log.error(error)

    def on_close(self, ws, close_status_code, close_msg):
        self.stopFlag.set()
        if hasattr(self, "health_http_server"):
            self.health_http_server.stop()
        log.info("### closed ###")

    def on_open(self, ws):
        # if ID_FILE exists, read the id from it
        try:
            with open(ID_FILE, "r") as f:
                self.id = f.read()
                self.config.id = self.id
        except FileNotFoundError:
            pass
        if settings.HTTP_HEALTHCHECK:
            self.health_http_server = HTTPHealthServer(settings.HTTP_PORT)
            self.health_http_server.start()
        payload = json.dumps(self.config.model_dump())
        ws.send(payload)
        self._init_heartbeat()

    def send_heartbeat(self):
        log.debug("Sending heartbeat")
        self.send_ws_message(self.hearbeat_msg)

    def _init_heartbeat(self):
        log.debug("Init heartbeat")
        self.hearbeat_msg = json.dumps(AgenticMessage(type=MSG_HEARTBEAT).model_dump())
        self.stopFlag = Event()
        thread = RepeatTimer(self.stopFlag, self.send_heartbeat)
        thread.start()
        # this will stop the timer

    def connect_to_registry(self) -> None:
        print(log.getEffectiveLevel())
        if log.getEffectiveLevel() <= 10:  # 10 is DEBUG
            websocket.enableTrace(True)
        hdrs = []
        if settings.AUTH_TOKEN != "":
            hdrs.append("Authorization:Bearer " + settings.AUTH_TOKEN)
        self.ws = websocket.WebSocketApp(
            self.registry + "/ws/nodes/connect",
            on_open=self.on_open,
            on_message=self.on_message,
            on_error=self.on_error,
            on_close=self.on_close,
            header=hdrs,
        )
        self.ws.run_forever()
