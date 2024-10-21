from typing import List

import msgspec
from loguru import logger
from rich.console import Console

from whiteduck.templates.exceptions import StepExecutionError
from whiteduck.templates.executor.prompt_executor import PromptExecutor
from whiteduck.templates.model.prompt import Prompt
from whiteduck.templates.model.step import Step
from whiteduck.templates.model.util_classes import Variable, WizardStepValues
from whiteduck.templates.steps.base_step import BaseStep
from whiteduck.templates.utils.steps_utils import (
    check_condition,
    find_prompt_by_id,
)

console = Console()


class WizardStep(BaseStep):
    def __init__(self, step_data: Step, prompts: List[Prompt]) -> None:
        """
        Initializes a WizardStep with the given step data and available prompts.

        Args:
            step_data (Step): The Step object containing step details.
            prompts (List[Prompt]): A list of available Prompt objects.
        """
        super().__init__(step_data)
        self.prompts = prompts

    def execute(self, variables: List[Variable]) -> None:
        """
        Execute the wizard steps using the provided variables.

        Args:
            variables (List[Variable]): The dictionary of variables for wizard execution.

        Raises:
            StepExecutionError: If any referenced prompt is not found or execution fails.
        """
        wizard_steps = msgspec.convert(
            self.step_data.value, type=List[WizardStepValues], strict=False
        )  # Assume this is a list of wizard step dictionaries

        title = self.step_data.title or "Wizard"

        logger.info(f"Executing wizard '{title}' with {len(wizard_steps)} steps")

        for index, wizard_step_data in enumerate(wizard_steps):
            if isinstance(wizard_step_data, str):
                logger.error(f"Invalid wizard step data: {wizard_step_data}")
                raise StepExecutionError(
                    f"Invalid wizard step data: {wizard_step_data}"
                )

            prompt_id = wizard_step_data.prompt
            conditions = wizard_step_data.condition

            if conditions and not check_condition(conditions, variables):
                logger.info(f"Skipping wizard step: {prompt_id} (condition not met)")
                continue

            prompt = find_prompt_by_id(prompt_id, self.prompts)
            if prompt:
                console.print(
                    f"\n[cyan]### Step {index+1}:[/cyan] {prompt.display_name} \n"
                )
                logger.info(f"Executing wizard step prompt: {prompt.id}")

                if prompt.show_description:
                    console.print(f"\n{prompt.description}\n")
                PromptExecutor(prompt).execute(variables)
            else:
                logger.error(f"Prompt not found in wizard: {prompt_id}")
                raise StepExecutionError(f"Prompt not found in wizard: {prompt_id}")
