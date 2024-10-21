from typing import List, Optional

import msgspec
from loguru import logger

from whiteduck.templates.exceptions import StepExecutionError
from whiteduck.templates.executor.prompt_executor import PromptExecutor
from whiteduck.templates.model.prompt import Prompt
from whiteduck.templates.model.step import Step
from whiteduck.templates.model.util_classes import Variable
from whiteduck.templates.steps.base_step import BaseStep
from whiteduck.templates.utils.steps_utils import find_prompt_by_id


class PromptStep(BaseStep):
    def __init__(self, step_data: Step, prompts: List[Prompt]) -> None:
        """
        Initializes a PromptStep with the given step data and available prompts.

        Args:
            step_data (Step): The Step object containing step details.
            prompts (List[Prompt]): A list of available Prompt objects.
        """
        super().__init__(step_data)
        # Use the utility function to find the prompt by ID
        if isinstance(step_data.value, str):
            self.prompt: Optional[Prompt] = find_prompt_by_id(
                str(step_data.value), prompts
            )
        else:
            self.prompt = msgspec.convert(step_data.value, Prompt)

    def execute(self, variables: List[Variable]) -> None:
        """
        Execute the prompt associated with this step using the provided variables.

        Args:
            variables (List[Variable]): The dictionary of variables for prompt execution.

        Raises:
            StepExecutionError: If the prompt is not found or execution fails.
        """
        if self.prompt:
            logger.info(f"Executing prompt: {self.prompt.id}")
            PromptExecutor(self.prompt).execute(variables)
        else:
            prompt_id = self.step_data.value
            logger.error(f"Prompt not found: {prompt_id}")
            raise StepExecutionError(f"Prompt not found: {prompt_id}")
