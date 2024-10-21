from abc import ABC, abstractmethod
from typing import List

from whiteduck.templates.model.step import Step
from whiteduck.templates.model.util_classes import Variable


class BaseStep(ABC):
    def __init__(self, step_data: Step) -> None:
        """
        Base class for all steps. Subclasses must implement the execute method.

        Args:
            step_data (Dict[str, Any]): Serialized step data.
        """
        self.step_data = step_data

    @abstractmethod
    def execute(self, variables: List[Variable]) -> None:
        """
        Execute the step with the provided variables.

        Args:
            variables (Dict[str, Any]): Dictionary of variables used during execution.
        """
        pass
