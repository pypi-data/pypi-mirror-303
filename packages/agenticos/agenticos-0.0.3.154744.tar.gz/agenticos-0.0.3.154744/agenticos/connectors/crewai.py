from .base import BaseWorkflowConfig, BaseWorkflowRunner
from typing import Any, Type, Generator


class CrewaiWorkflowConfig(BaseWorkflowConfig):
    def __init__(self, description: str, inputs: dict[str, str], crew_cls: Type):
        self._description = description
        self._inputs = inputs
        crew_type = crew_cls.__name__
        self.crew_cls = crew_cls
        crew = crew_cls()
        if crew_type == "WrappedClass":
            self._steps_description = [t.description for t in crew.crew().tasks]
        elif crew_type == "Crew":
            self._steps_description = [t.description for t in crew.tasks]
        else:
            raise ValueError("Unknown crew type")

    def description(self) -> str:
        return self._description

    def inputs(self) -> dict[str, str]:
        return self._inputs

    def steps_description(self) -> list[str]:
        return self._steps_description

    def new_runner(self) -> BaseWorkflowRunner:
        return CrewaiWorkflowRunner(self.crew_cls)

    def model_dump(self, name: str) -> dict:
        return {
            "name": name,
            "description": self._description,
            "inputs": self._inputs,
            "steps_description": self._steps_description,
        }


class CrewaiWorkflowRunner(BaseWorkflowRunner):
    def __init__(self, crew_cls: Type):
        c = crew_cls()
        crew_type = crew_cls.__name__
        if crew_type == "WrappedClass":
            self.crew = c.crew()
        elif crew_type == "Crew":
            self.crew = c
        else:
            raise ValueError("Unknown crew type")

    def start(self, inputs: dict[str, str]) -> None:
        self._output = self.crew.kickoff(inputs=inputs)

    def step_output(self) -> Generator[str, None, None]:
        for task in self.crew.tasks:
            if hasattr(task, "output") and task.output:
                yield task.output.raw
