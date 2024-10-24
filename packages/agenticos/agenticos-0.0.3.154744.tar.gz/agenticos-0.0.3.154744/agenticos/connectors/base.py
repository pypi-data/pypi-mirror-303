from abc import ABC, abstractmethod
from typing import Generator


class BaseWorkflowRunner(ABC):
    @abstractmethod
    def start(self, inputs : dict[str, str]) -> None:
        pass

    @abstractmethod
    def step_output(self) -> Generator[str, None, None]:
        pass


class BaseWorkflowConfig(ABC):
    @abstractmethod
    def description(self) -> str:
        pass

    @abstractmethod
    def inputs(self) -> dict[str, str]:
        pass

    @abstractmethod
    def steps_description(self) -> list[str]:
        pass

    @abstractmethod
    def new_runner(self) -> BaseWorkflowRunner:
        pass

    @abstractmethod
    def model_dump(self, name : str) -> dict:
        pass
