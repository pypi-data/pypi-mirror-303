from typing import List, Optional

import msgspec
from loguru import logger

from whiteduck.templates.config import COMPONENTS_DIR
from whiteduck.templates.exceptions import StepExecutionError
from whiteduck.templates.executor.module_executor import ModuleExecutor
from whiteduck.templates.model.step import Step
from whiteduck.templates.model.util_classes import Module, Variable
from whiteduck.templates.steps.base_step import BaseStep
from whiteduck.templates.utils.steps_utils import find_module_by_id


class ModuleStep(BaseStep):
    def __init__(self, step_data: Step, modules: List[Module]) -> None:
        """
        Initializes a ModuleStep with the given step data and available modules.

        Args:
            step_data (Step): The Step object containing step details.
            modules (List[Module]): A list of available Module objects.
        """
        super().__init__(step_data)
        # Use the utility function to find the module by ID

        if isinstance(step_data.value, str):
            self.module: Optional[Module] = find_module_by_id(step_data.value, modules)
        else:
            self.module = msgspec.convert(step_data.value, Module)

    def execute(self, variables: List[Variable]) -> None:
        """
        Execute the module associated with this step using the provided variables.

        Args:
            variables (List[Variable]): The dictionary of variables for module execution.

        Raises:
            StepExecutionError: If the module is not found or execution fails.
        """
        if self.module:
            logger.info(f"Executing module: {self.module.id}")
            ModuleExecutor(self.module).execute(variables, COMPONENTS_DIR)
        else:
            module_id = self.step_data.value
            logger.error(f"Module not found: {module_id}")
            raise StepExecutionError(f"Module not found: {module_id}")
