import os
from typing import List, Optional

import questionary
from loguru import logger
from rich import inspect
from rich.console import Console
from rich.markdown import Markdown
from rich.syntax import Syntax
from rich.table import Table
from rich.traceback import install

from whiteduck.core.models import BaseModule
from whiteduck.templates.config import TEMPLATES_DIR
from whiteduck.templates.exceptions import StepExecutionError
from whiteduck.templates.executor.template_executor import TemplateExecutor
from whiteduck.templates.model.template import Template
from whiteduck.templates.utils.file_utils import list_yaml_files

# Install rich traceback handler for better error display
install()
console = Console()


class TemplateModule(BaseModule):
    @classmethod
    def get_name(cls):
        return "Templates"

    @classmethod
    def get_description(cls):
        return "Get your project started! 🧩"

    def run(self):
        yaml_files = list_yaml_files(TEMPLATES_DIR)
        if not yaml_files:
            logger.error("No YAML files found in templates directory")
            console.print(
                f"[bold red]🚫 No YAML files found in '{TEMPLATES_DIR}' directory.[/bold red]"
            )
            return

        selected_template = self.load_and_display_templates(yaml_files)

        if selected_template and self.display_template_details(selected_template):
            logger.info(f"Executing template: {selected_template.template}")
            self.execute_template(selected_template)
            return
        else:
            logger.info("Returning to mode selection")
            console.print("\n[yellow]🔄 Returning to mode selection...[/yellow]\n")
            return

    def load_and_display_templates(self, yaml_files: List[str]) -> Optional[Template]:
        """Load templates from YAML files and display them for selection."""
        templates = []
        choices = []

        for file_name in yaml_files:
            file_path = os.path.join(TEMPLATES_DIR, file_name)
            template = Template.load_template(file_path)
            templates.append(template)

            logger.info(f"Found template: {template.template}")
            choices.append(f"{template.template}")

        choices[-1] += "\n"

        choices.append("Schema - The yaml schema")
        choices.append(
            "Type Info - Internal Python Type info of the 'Template' object\n"
        )
        console.print(Markdown("# 📁 Template Overview 📁 "), style="bold cyan")
        console.line(1)

        selected = questionary.select(
            "Select a template", qmark="📄 ", choices=choices, instruction=" \n"
        ).ask()

        if selected == "Schema - The yaml schema":
            console.print(Markdown("# 📁 Template Schema 📁 "), style="bold cyan")
            schema = Template.get_schema()
            console.print(Syntax(schema, "json"))
            questionary.text("Press Enter to continue...").ask()
            return None
        elif (
            selected
            == "Type Info - Internal Python Type info of the 'Template' object\n"
        ):
            console.print(Markdown("# 📁 Template Type Info 📁 "), style="bold cyan")
            info = Template.get_info()
            inspect(info, console=console)
            questionary.text("Press Enter to continue...").ask()
            return None

        if selected:
            return templates[choices.index(selected)]

        return None

    def create_dependency_groups_table(self, template: Template) -> Table:
        table = Table(title="Dependency Groups")
        table.add_column("Name", style="cyan")
        table.add_column("Environment", style="magenta")
        table.add_column("Description", style="green")
        table.add_column("Mandatory", style="yellow")
        table.add_column("Dependencies", style="blue")

        for group in template.dependency_groups:
            dependencies = ", ".join([dep.name for dep in group.dependencies])
            table.add_row(
                group.name,
                group.environment,
                group.description,
                str(group.is_mandatory),
                dependencies,
            )

        return table

    def display_template_details(self, template: Template) -> bool:
        """Display selected template's details and prompt user for action."""
        readme_content = "No detailed readme available."

        if template.documentation_path and os.path.exists(template.documentation_path):
            with open(template.documentation_path, "r") as md_file:
                readme_content = md_file.read()

        title = f"# {template.template} \n\n"
        description_md = Markdown(title + template.description)

        console.print(description_md)
        console.line(1)
        # Display dependency groups table
        if template.dependency_groups:
            dependency_table = self.create_dependency_groups_table(template)
            console.print(dependency_table)
        else:
            console.print(
                "[yellow]No dependency groups defined for this template.[/yellow]"
            )

        console.line(1)
        while True:
            choice = questionary.select(
                "Do you want to proceed with this template?",
                instruction=" \n",
                choices=["Yes", "No", "Show Readme"],
            ).ask()

            if choice == "Yes":
                return True
            elif choice == "No":
                return False
            elif choice == "Show Readme":
                console.print("\n[bold cyan]Readme:[/bold cyan]")
                console.print(Markdown(readme_content))
                questionary.text("Press Enter to continue...").ask()

    def execute_template(self, template: Template) -> None:
        """Execute the selected template using TemplateExecutor."""
        try:
            TemplateExecutor.execute_template(template)
        except StepExecutionError as error:
            logger.error(f"Execution aborted due to an error: {error}")
            console.print(
                "\n[bold red]Execution aborted. Exiting the application.[/bold red]"
            )
