from typing import List

import msgspec
from loguru import logger
from rich.console import Console

from whiteduck.templates.config import COMPONENTS_DIR
from whiteduck.templates.executor.dependeny_wizard_executor import (
    DependencyWizardExecutor,
)
from whiteduck.templates.executor.prompt_executor import PromptExecutor
from whiteduck.templates.model.prompt import Prompt
from whiteduck.templates.model.step import Step
from whiteduck.templates.model.util_classes import (
    DependencyGroup,
    DependencyWizard,
    Variable,
    WizardStepValues,
)
from whiteduck.templates.steps.base_step import BaseStep
from whiteduck.templates.utils.steps_utils import (
    check_condition,
    find_prompt_by_id,
)

console = Console()


class DependencyWizardStep(BaseStep):
    def __init__(
        self, step_data: Step, dependency_groups: List[DependencyGroup]
    ) -> None:
        """
        Initializes a WizardStep with the given step data and available prompts.

        Args:
            step_data (Step): The Step object containing step details.
            prompts (List[Prompt]): A list of available Prompt objects.
        """
        super().__init__(step_data)
        self.dependency_groups = dependency_groups

    def execute(self, variables: List[Variable]) -> None:
        """
        Execute the wizard steps using the provided variables.

        Args:
            variables (List[Variable]): The dictionary of variables for wizard execution.

        Raises:
            StepExecutionError: If any referenced prompt is not found or execution fails.
        """
        wizard_dep = msgspec.convert(
            self.step_data, type=DependencyWizard, strict=False
        )  # Assume this is a list of wizard step dictionaries

        title = self.step_data.title or "Wizard"

        logger.info(
            f"Executing wizard '{title}' with {len(self.dependency_groups)} steps"
        )

        DependencyWizardExecutor(wizard_dep, self.dependency_groups).execute(
            variables, COMPONENTS_DIR
        )
