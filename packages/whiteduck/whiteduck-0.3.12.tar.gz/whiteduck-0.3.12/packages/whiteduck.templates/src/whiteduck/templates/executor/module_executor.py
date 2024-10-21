import os
import platform
import shutil
import subprocess
import sys
import time
from typing import List

from loguru import logger
from poethepoet.app import PoeThePoet
from poethepoet.config import PoeConfig
from rich.console import Console

from whiteduck.templates.config import POE_TEMPLATES, TEMPLATES_DIR
from whiteduck.templates.exceptions import StepExecutionError
from whiteduck.templates.executor.variable_processor import (
    replace_placeholder,
    replace_placeholders,
)
from whiteduck.templates.model.util_classes import Module, Variable

console = Console()
project_dir = ""


def load_module(module_data: dict) -> Module:
    """
    Load and deserialize module data into a Module instance.

    Args:
        module_data (dict): The module data to load.

    Returns:
        Module: A fully populated Module instance.

    Raises:
        ValueError: If module_data is not a dictionary or if required keys are missing.
    """
    if not isinstance(module_data, dict):
        logger.error("Module data must be a dictionary")
        raise ValueError("Module data must be a dictionary")

    logger.info("Starting module serialization")

    required_keys = ["id", "type"]
    for key in required_keys:
        if key not in module_data:
            logger.error(f"Missing required module key: {key}")
            raise ValueError(f"Module data missing required key: {key}")

    module_instance = Module(
        id=module_data["id"],
        type=module_data["type"],
        module_definition=module_data["module_definition"],
        arguments=module_data.get("arguments", []),
        displayName=module_data.get("displayName"),
    )

    logger.info("Finished module serialization")
    return module_instance


class ModuleExecutor:
    def __init__(self, module: Module):
        logger.info(f"Initializing ModuleExecutor with module: {module.id}")
        self.module: Module = module

    def execute(self, variables: List[Variable], components_path: str) -> None:
        global project_dir
        """
        Executes the module's install script based on its type and arguments.

        Args:
            module (Module): The Module object containing the type, arguments, and display name.
            variables (List[Variable]): A dictionary of Variable objects for placeholder replacements.
            components_path (str): The base directory path to locate the component scripts.

        Raises:
            StepExecutionError: If the script execution fails.
        """
        logger.info("Executing module")

        # console.print(Markdown("--------------------------------------------------"))
        title = f"\n\n# 🔧 Executing Module: {self.module.displayName} 🔧"
        logger.info(title)

        try:
            # Since the Module class doesn't have steps, prompts, or modules attributes,
            # we'll need to adjust how we process the module. For now, we'll just log the module details.
            logger.info(f"Module ID: {self.module.id}")
            logger.info(f"Module Type: {self.module.type}")
            logger.info(f"Module Arguments: {self.module.arguments}")
            logger.info(f"Module Display Name: {self.module.displayName}")

            # Determine the correct script based on OS
            script_name = (
                "install.bat" if platform.system() == "Windows" else "install.sh"
            )
            script_path = f"{components_path}/{self.module.type}/{script_name}"

            # Replace placeholders in the display name and prepare arguments
            display_name = self.module.displayName or "Executing Module"
            display_name = replace_placeholder(display_name, variables)
            args = replace_placeholders(self.module.arguments, variables)  # type: ignore

            logger.info(f"Executing module: {display_name}")
            console.print(f"\n[bold magenta]Executing: {display_name} [/bold magenta]")
            console.line(1)

            with console.status(
                "[bold green]Executing...   [/bold green]", spinner="dots"
            ):
                time.sleep(1)
                try:
                    params = []
                    params.append(self.module.module_definition)
                    for arg in args:
                        logger.info(f"Argument: {arg}")
                        for key, value in arg.items():
                            params.append(f"{value}")
                        # params.append(f"{key}")

                    if self.module.type == "init":
                        # create dir at params[0]
                        os.makedirs(params[1], exist_ok=False)
                        project_dir = params[1]
                        # copy os.path.join(TEMPLATES_DIR, "poe_tasks.toml") into new dir
                        old_poe_tasks = os.path.join(
                            TEMPLATES_DIR, "/poe_tasks/default_tasks.toml"
                        )
                        if not os.path.exists(old_poe_tasks):
                            old_poe_tasks = POE_TEMPLATES

                        new_poe_tasks = os.path.join(project_dir, "poe_tasks.toml")
                        shutil.copy2(
                            old_poe_tasks,
                            new_poe_tasks,
                        )

                        config = PoeConfig(cwd=new_poe_tasks)
                        poe_instance = PoeThePoet(
                            config=config,
                            program_name="whiteduck",
                        )

                        is_uv_available = shutil.which("uv")
                        if not is_uv_available:
                            if platform.system() == "Windows":
                                result = poe_instance(["install_win"])
                            else:
                                result = poe_instance(["install"])

                        result = poe_instance(["init"])
                    elif self.module.type == "poe":
                        project_dir = params[1]
                        new_poe_tasks = os.path.join(project_dir, "poe_tasks.toml")
                        config = PoeConfig(cwd=new_poe_tasks)
                        poe_instance = PoeThePoet(
                            config=config,
                            program_name="whiteduck",
                        )

                        del params[1]
                        packages = params[1].split(" ")
                        cmd = params[0]
                        for package in packages:
                            result = poe_instance([cmd, package])
                            console.line(1)

                except subprocess.CalledProcessError as e:
                    logger.error(f"Error executing script: {e}")
                    console.print(f"[bold red]Error executing script:[/bold red] {e}")
                    raise StepExecutionError(
                        f"Error executing script {display_name}: {e!s}"
                    )

            console.print(
                f"\n[bold green]✅ '{display_name}' executed successfully.[/bold green]"
            )

        except Exception as e:
            console.print(f"\n[bold red]❌ Error:[/bold red] {e!s}")
            console.print(
                "[bold red]❗Module execution aborted due to an error.[/bold red]"
            )
            raise StepExecutionError(
                f"Error executing module '{self.module.id}': {e!s}"
            )
