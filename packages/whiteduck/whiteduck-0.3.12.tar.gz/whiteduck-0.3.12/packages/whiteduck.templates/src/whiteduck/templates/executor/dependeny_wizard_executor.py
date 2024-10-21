from typing import List

from loguru import logger
from rich.console import Console

from whiteduck.templates.exceptions import StepExecutionError
from whiteduck.templates.model.util_classes import (
    DependencyGroup,
    DependencyWizard,
    Variable,
)

console = Console()
project_dir = ""


class DependencyWizardExecutor:
    def __init__(
        self,
        dependency_wizard: DependencyWizard,
        dependency_groups: List[DependencyGroup],
    ):
        logger.info(
            f"Initializing ModulDependencyWizardeExecutor with module: {dependency_wizard.id}"
        )
        self.dependency_wizard: DependencyWizard = dependency_wizard
        self.dependency_groups: List[DependencyGroup] = dependency_groups

    def execute(self, variables: List[Variable], components_path: str) -> None:
        global project_dir

        logger.info("Executing module")
        logger.info(f"Module ID: {self.dependency_wizard.id}")
        logger.info(f"Module Type: {self.dependency_wizard.type}")
        logger.info(f"Module Type: {self.dependency_wizard.title}")
        # console.print(Markdown("--------------------------------------------------"))
        title = f"\n\n# 🔧 Executing Module: {self.dependency_wizard.title} 🔧"
        logger.info(title)

        try:
            for dg in self.dependency_groups:
                console.print(
                    f"\n[bold green]✅ '{dg.description}' executed successfully.[/bold green]"
                )

        except Exception as e:
            console.print(f"\n[bold red]❌ Error:[/bold red] {e!s}")
            console.print(
                "[bold red]❗Module execution aborted due to an error.[/bold red]"
            )
            raise StepExecutionError(
                f"Error executing module '{self.dependency_wizard.id}': {e!s}"
            )
