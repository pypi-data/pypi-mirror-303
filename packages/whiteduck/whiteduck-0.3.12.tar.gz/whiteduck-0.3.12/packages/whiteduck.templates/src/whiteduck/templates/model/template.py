import json
from typing import List, Optional

import msgspec
import yaml
from loguru import logger
from msgspec import Struct, field

from whiteduck.core.models.poe_task import PoeTask
from whiteduck.templates.model.prompt import Prompt
from whiteduck.templates.model.step import Step
from whiteduck.templates.model.util_classes import (
    DependencyGroup,
    Module,
    Variable,
)


class Template(Struct):
    version: str
    template: str
    short_description: str
    description: str
    documentation_path: Optional[str] = None
    module_path: Optional[str] = None
    variables: List[Variable] = field(default_factory=list)
    prompts: List[Prompt] = field(default_factory=list)
    modules: List[Module] = field(default_factory=list)
    steps: List[Step] = field(default_factory=list)
    dependency_groups: List[DependencyGroup] = field(default_factory=list)

    def __post_init__(self) -> None:
        logger.info(
            f"Initialized Template with version: {self.version}, template: {self.template}"
        )
        self.validate_steps()

    def validate_steps(self) -> None:
        """
        Validate the steps within the template, ensuring referenced prompts and modules exist.
        """
        logger.info("Starting validation of steps")
        prompt_ids = {prompt.id for prompt in self.prompts}
        module_ids = {module.id for module in self.modules}

        for step in self.steps:
            # Check if prompt or module is referenced in the steps

            if step.type == "prompt_id" and step.value not in prompt_ids:
                logger.error(
                    f"Prompt '{step.value}' referenced in step '{step.title}' not found"
                )
                raise ValueError(f"Prompt '{step.value}' not found")

            elif step.type == "module_id" and step.value not in module_ids:
                logger.error(
                    f"Module '{step.value}' referenced in step '{step.title}' not found"
                )
                raise ValueError(f"Module '{step.value}' not found")

            # Check if prompt or module are created in the step
            if step.type == "prompt":
                if isinstance(step.value, dict):
                    res_bytes = json.dumps(step.value).encode("utf-8")
                    value = msgspec.yaml.decode(res_bytes, type=Prompt, strict=False)
                    self.prompts.append(value)
                    prompt_ids.add(value.id)
                else:
                    logger.error(
                        f"Prompt '{step.value}' referenced in step '{step.title}' not found"
                    )
                    raise ValueError(f"Prompt '{step.value}' not found")

            elif step.type == "module":
                if isinstance(step.value, dict):
                    res_bytes = json.dumps(step.value).encode("utf-8")
                    value = msgspec.yaml.decode(res_bytes, type=Module, strict=False)
                    self.modules.append(value)
                    module_ids.add(value.id)
                else:
                    logger.error(
                        f"Module '{step.value}' referenced in step '{step.title}' not found"
                    )
                    raise ValueError(f"Module '{step.value}' not found")

            # Check if wizard steps have valid prompt references
            elif step.type == "wizard":
                if not isinstance(step.value, list):
                    logger.error(f"Wizard step '{step.title}' value must be a list")
                    raise ValueError(f"Wizard step '{step.title}' value must be a list")
                for wizard_step in step.value:
                    if (
                        "prompt" not in wizard_step
                        or wizard_step["prompt"] not in prompt_ids
                    ):
                        logger.error(
                            f"Invalid prompt reference in wizard step '{step.title}'"
                        )
                        raise ValueError(
                            f"Invalid prompt reference in wizard step '{step.title}'"
                        )

        logger.info("Validation of steps completed")

    @staticmethod
    def get_schema() -> str:
        msgspec.json.schema(Template)
        result = json.dumps(msgspec.json.schema(Template), indent=4)
        return result

    @staticmethod
    def get_info():
        return msgspec.inspect.type_info(Template)

    @staticmethod
    def load_template(template_path: str) -> "Template":
        """
        Load and deserialize template data into a Template instance.

        Args:
            template_data (dict): The template data to load.

        Returns:
            Template: A fully populated Template instance.

        Raises:
            ValueError: If template_data is not a dictionary or if required keys are missing.
        """
        logger.info("Starting template serialization")

        with open(template_path, "r") as file:
            template_data = msgspec.convert(yaml.safe_load(file), type=Template)

        return template_data
