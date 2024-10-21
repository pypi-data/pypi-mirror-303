import questionary
from loguru import logger
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
from rich.text import Text

from whiteduck.templates.exceptions import StepExecutionError
from whiteduck.templates.executor.step_processor import process_steps
from whiteduck.templates.executor.variable_processor import process_variables
from whiteduck.templates.model.template import Template

console = Console()


class TemplateExecutor:
    def __init__(self, template_path: str):
        logger.info(f"Initializing TemplateExecutor with template: {template_path}")
        self.template: Template = Template.load_template(template_path)

    def execute(self) -> None:
        logger.info("Executing template")

        console.print(Markdown("--------------------------------------------------"))
        title = "\n\n# 🚀" + self.template.template + " 🚀"
        console.print(Markdown(title), style="bold green", justify="left", markup=True)

        variables = process_variables(self.template.variables)
        try:
            process_steps(
                self.template,
                self.template.steps,
                variables,
                self.template.modules,
                self.template.prompts,
            )
        except StepExecutionError as e:
            console.print(f"\n[bold red]❌ Error:[/bold red] {e!s}")
            console.print(
                "[bold red]❗Execution aborted due to an error in one of the steps.[/bold red]"
            )
            raise

    @staticmethod
    def execute_template(template: Template) -> None:
        logger.info("Executing template")

        console.print(Markdown("--------------------------------------------------"))
        title = "\n\n# 🚀" + template.template + " 🚀"
        console.print(Markdown(title), style="bold green", justify="left", markup=True)

        variables = process_variables(template.variables)
        try:
            process_steps(
                template,
                template.steps,
                variables,
                template.modules,
                template.prompts,
            )
            console.line(1)
            console.print(
                Markdown("--------------------------------------------------")
            )
            title = (
                "\n\n# 🥳🎉 !! " + template.template + " SUCCESSFULLY CREATED !! 🥳🎉"
            )
            console.print(
                Markdown(title), style="bold green", justify="left", markup=True
            )

            console.line(1)
            choice = questionary.select(
                "Do you want to quit?",
                instruction=" \n",
                choices=["Yes", "No"],
            ).ask()

            if choice == "Yes":
                banner_text = Text(
                    """
    >(')____,  >(')____,  >(')____,  >(')____,  >(') ___,
    (` =~~/    (` =~~/    (` =~~/    (` =~~/    (` =~~/
    --~^~^`---'~^~^~^`---'~^~^~^`---'~^~^~^`---'~^~^~^`---'~^~^~
                """,
                    justify="center",
                    style="bold orange3",
                )

                console.print(
                    Panel(banner_text, title="quack quack 🦆", style="bold orange3")
                )
                quit()
            elif choice == "No":
                return
        except StepExecutionError as e:
            console.print(f"\n[bold red]❌ Error:[/bold red] {e!s}")
            console.print(
                "[bold red]❗Execution aborted due to an error in one of the steps.[/bold red]"
            )
            raise
