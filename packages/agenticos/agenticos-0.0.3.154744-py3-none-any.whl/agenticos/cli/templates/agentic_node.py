from uuid import UUID

from dotenv import load_dotenv
from fastapi import BackgroundTasks, FastAPI, HTTPException
from fastapi.responses import JSONResponse

from agenticos.node.models import Task, TaskStatus, Workflow

from .agentic_config import workflows

load_dotenv()

app = FastAPI()

tasks: dict[UUID, Task] = {}


def run_task(workflow: Workflow, task: Task) -> None:
    try:
        workflow.kickoff_function(task.inputs)
        task.output = workflow.output_function()
        task.status = TaskStatus.COMPLETED
    except Exception as e:
        task.output = str(e)
        task.status = TaskStatus.FAILED


@app.get(
    "/node/description",
    summary="Get the description of the node",
    response_model=dict[str,Workflow],
)
def description() -> dict[str,Workflow]:
    return workflows


@app.post("/workflow/{workflow_name}/run")
async def run(workflow_name : str, inputs: dict[str, str], background_tasks: BackgroundTasks) -> str:
    if workflow_name not in workflows:
        raise HTTPException(status_code=404, detail="Workflow not found")
    task = Task(inputs=inputs, status=TaskStatus.RUNNING, output="")
    tasks[task.id] = task
    background_tasks.add_task(run_task, workflows[workflow_name], task)
    return str(task.id)


@app.get("/task/{task_id}")
def get_task(task_id: str) -> Task:
    if UUID(task_id) not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    return tasks[UUID(task_id)]


@app.get("/tasks")
def get_tasks() -> list[str]:
    return [str(tk) for tk in tasks.keys()]


@app.get("/health")
def health() -> JSONResponse:
    return JSONResponse({"status": "ok"})
