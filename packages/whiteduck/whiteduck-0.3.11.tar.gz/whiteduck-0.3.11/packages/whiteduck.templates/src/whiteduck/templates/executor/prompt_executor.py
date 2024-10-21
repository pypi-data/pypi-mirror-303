from typing import List

import questionary
from loguru import logger
from rich.console import Console

from whiteduck.templates.exceptions import StepExecutionError
from whiteduck.templates.model.prompt import Prompt
from whiteduck.templates.model.util_classes import Variable

console = Console()


def load_prompt(prompt_data: dict) -> Prompt:
    """
    Load and deserialize prompt data into a Prompt instance.

    Args:
        prompt_data (dict): The prompt data to load.

    Returns:
        Prompt: A fully populated Prompt instance.

    Raises:
        ValueError: If prompt_data is not a dictionary or if required keys are missing.
    """
    if not isinstance(prompt_data, dict):
        logger.error("Prompt data must be a dictionary")
        raise ValueError("Prompt data must be a dictionary")

    logger.info("Starting prompt serialization")

    required_keys = ["id", "prompt"]
    for key in required_keys:
        if key not in prompt_data:
            logger.error(f"Missing required prompt key: {key}")
            raise ValueError(f"Prompt data missing required key: {key}")

    prompt_instance = Prompt(
        id=prompt_data["id"],
        prompt=prompt_data["prompt"],
        display_name=prompt_data.get("display_name"),
        default=prompt_data.get("default"),
        url=prompt_data.get("url"),
        type=prompt_data.get("type", "text"),
        value_set=prompt_data.get("value_set"),
        description=prompt_data.get("description"),
        show_description=prompt_data.get("show_description", False),
    )

    logger.info("Finished prompt serialization")
    return prompt_instance


class PromptExecutor:
    def __init__(self, Prompt: Prompt):
        logger.info(f"Initializing PromptExecutor with prompt: {Prompt.display_name}")
        self.prompt = Prompt

    def execute(self, variables: List[Variable]) -> str:
        logger.info("Executing prompt")

        # console.print(Markdown("--------------------------------------------------"))
        console.line(1)
        # title = f"\n\n#### 💬 Executing Prompt: {self.prompt.display_name} 💬"
        # console.print(Markdown(title), style="bold yellow", justify="left", markup=True)

        try:
            prompt_id = self.prompt.id
            prompt_value = self.prompt.prompt
            default_value = self.prompt.default or ""
            value_set = self.prompt.value_set
            out_var = self.prompt.out

            # Resolve default from variables if it references another variable
            if default_value.startswith("[[") and default_value.endswith("]]"):
                default_key = default_value[2:-2]
                # default_value = str(variables.get(default_key, value_set[0]))
                # get variable with id = default_key, if not found, use default_value
                single_var = next(
                    (var for var in variables if var.id == default_key), None
                )
                if single_var:
                    default_value = str(single_var.value)
                else:
                    default_value = str(default_value)

            display_name = self.prompt.display_name or prompt_id

            prompt_type = self.prompt.type

            logger.info(f"Executing prompt: {display_name}")

            # Handle different prompt types
            if value_set or prompt_type == "select":
                choices = [str(v) for v in (value_set or [])]
                user_input = questionary.select(
                    prompt_value, choices=choices, default=default_value
                ).ask()
            elif prompt_type == "password":
                user_input = questionary.password(prompt_value).ask()
            elif prompt_type == "file_dir":
                user_input = questionary.path(
                    prompt_value, only_directories=True, default=default_value
                ).ask()
            else:
                user_input = questionary.text(prompt_value, default=default_value).ask()

            # Update the variables dictionary with the user's input
            variable = next((var for var in variables if var.id == out_var), None)

            if variable:
                variable.value = user_input
                logger.debug(f"Variable '{variable.id}' updated to: {user_input}")
            else:
                if out_var:
                    variables.append(Variable(id=out_var, value=user_input))
                    logger.debug(
                        f"Variable '{out_var}' created and set to: {user_input}"
                    )
                else:
                    console.print(
                        "\n[bold red]❗ Warning: output var does not exist or is not defined...[/bold red]"
                    )

            return user_input

        except Exception as e:
            console.print(f"\n[bold red]❌ Error:[/bold red] {e!s}")
            console.print(
                "[bold red]❗Prompt execution aborted due to an error.[/bold red]"
            )
            raise StepExecutionError(
                f"Error executing prompt '{self.prompt.id}': {e!s}"
            )

        # finally:
        #     console.print(f"\n[bold green]✅ Prompt '{self.prompt.id}' executed successfully.[/bold green]")
