from enum import Enum
from typing import Callable, Dict, Optional, Any
from uuid import UUID, uuid4
from abc import ABC, abstractmethod

from pydantic import BaseModel, Field

from agenticos.connectors.base import BaseWorkflowConfig

MSG_HS_NODE = "MSG_HS_NODE"
MSG_HS_ACK = "MSG_HS_ACK"
MSG_TASK_REQ = "MSG_TASK_REQ"
MSG_TASK_FIN = "MSG_TASK_FIN"
MSG_STEP_FIN = "MSG_STEP_FIN"
MSG_HEARTBEAT = "MSG_HEARTBEAT"


class TaskStatus(str, Enum):
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"


class WorkflowRunner(ABC):
    @abstractmethod
    def kickoff(self, inputs: Dict[str, str]) -> None:
        pass

    @abstractmethod
    def output(self) -> str:
        pass

    @abstractmethod
    def ongoing_steps(self) -> list:
        pass


class AgenticConfig:
    def __init__(self, name: str, workflows: Dict[str, BaseWorkflowConfig]):
        self.name = name
        self.workflows = workflows

    id: Optional[UUID] = None
    name: str
    workflows: Dict[str, BaseWorkflowConfig] = {}

    def model_dump(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "workflows": {k: v.model_dump(k) for k, v in self.workflows.items()},
        }


class Task(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    inputs: Dict[str, str]
    status: TaskStatus = Field()
    output: str | None


class WrongFolderError(Exception):
    pass


class AgenticMessage(BaseModel):
    type: str


class AgenticHandshakeMessage(AgenticMessage):
    type: str = MSG_HS_NODE
    node: str


class TaskFinishedMessage(AgenticMessage):
    type: str = MSG_TASK_FIN
    task_id: str
    status: TaskStatus
    result: str | None


class StepFinishedMessage(AgenticMessage):
    type: str = MSG_STEP_FIN
    task_id: str
    step: int
    result: str


class TaskRequest(BaseModel):
    workflow: str
    inputs: Dict[str, str]
    task_id: UUID = Field(default_factory=uuid4)
    node_id: str


class AgenticTaskRequestMessage(BaseModel):
    type: str = MSG_TASK_REQ
    task: TaskRequest
