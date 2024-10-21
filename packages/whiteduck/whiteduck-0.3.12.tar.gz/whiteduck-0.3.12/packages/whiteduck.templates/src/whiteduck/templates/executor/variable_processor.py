import re
import time
import uuid
from typing import Dict, List

from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.traceback import install

from whiteduck.templates.config import GLOBAL_VARS
from whiteduck.templates.model.util_classes import Variable

install(show_locals=True)
console = Console()

# Define logger (assuming it was intended to be Loguru or similar)


def get_program_variable(variable_name: str) -> str:
    """Retrieve a program-specific variable based on the variable name."""
    if variable_name.lower() == "timestamp":
        return str(int(time.time()))
    elif variable_name.lower() == "guid":
        return str(uuid.uuid4())
    elif variable_name.lower() == "now_":
        return time.strftime("%Y_%m_%d_%H_%M_%S")
    return ""


def replace_variable_patterns(variable: Variable) -> str:
    """Replace environment and program variables in the given value string."""
    env_pattern = re.compile(r"\[\[env\.(.*?)\]\]")
    wd_pattern = re.compile(r"\[\[wd\.(.*?)\]\]")

    value = (
        variable.value if isinstance(variable.value, str) else ""
    )  # Ensure value is str
    # Replace environment variables
    value = env_pattern.sub(lambda match: resolve_env_variable(match.group(1)), value)

    # Replace program variables (e.g., GUID, timestamp)
    value = wd_pattern.sub(
        lambda match: resolve_program_variable(match.group(1)), value
    )

    return value


def resolve_env_variable(variable_name: str) -> str:
    """Resolve environment variables from GLOBAL_VARS."""
    env_value = str(GLOBAL_VARS.get(variable_name, ""))  # type: ignore # Removed .value (incorrect)
    if not env_value:
        console.print(
            f"[bold yellow]Warning:[/bold yellow] Environment variable '{variable_name}' not found. Using empty string."
        )
    return env_value


def resolve_program_variable(variable_name: str) -> str:
    """Resolve program-specific variables like timestamp and GUID."""
    value = get_program_variable(variable_name)
    if not value:
        console.print(
            f"[bold yellow]Warning:[/bold yellow] Program variable '{variable_name}' not found. Using empty string."
        )
    return value


def process_variables(variables: List[Variable]) -> List[Variable]:
    """
    Process the variables by replacing placeholders in their values.

    Args:
        variables (List[Variable]): List of variables to process.

    Returns:
        List[Variable]: A list of processed Variable instances.
    """
    # variables = [Variable(**var) if isinstance(var, dict) else var for var in variables]

    if variables:
        console.print("\n[bold blue]Building template logic and flow...[/bold blue]")

        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            transient=True,
        ) as progress:
            for variable in variables:
                variable.value = replace_variable_patterns(variable)  # Replace in-place
                progress.add_task(description=f"Processing {variable.id}", total=None)
                time.sleep(0.05)

    return variables


def replace_placeholder(text: str, variables: List[Variable]) -> str:
    """
    Replace placeholders in the format [[VAR_NAME]] with values from variables.

    Args:
        text (str): The text containing placeholders.
        variables (List[Variable]): A list of Variable objects.

    Returns:
        str: The text with placeholders replaced.
    """

    for variable in variables:
        # Replace using the Variable's id as the placeholder name
        text = text.replace(f"[[{variable.id}]]", str(variable.value))
    return text


def replace_placeholders(
    arguments: List[Dict[str, str]], variables: List[Variable]
) -> List[Dict[str, str]]:
    """
    Replace placeholders in the format [[VAR_NAME]] with values from variables.

    Args:
        text (str): The text containing placeholders.
        variables (List[Variable]): A list of Variable objects.

    Returns:
        str: The text with placeholders replaced.
    """
    if isinstance(arguments, list):
        for arg in arguments:
            for key, value in arg.items():
                arg[key] = replace_placeholder(value, variables)

        return arguments
