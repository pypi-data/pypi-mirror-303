import os
import subprocess
import sys
from typing import Dict, List, Optional, Tuple, Union

import click
import questionary
from loguru import logger
from rich.console import Console
from rich.markdown import Markdown
from rich.text import Text
from rich.traceback import install

from whiteduck.config import __version__
from whiteduck.core import Style
from whiteduck.core.config import STYLE_SPEC
from whiteduck.core.models import BaseModule
from whiteduck.core.modules.settings import Settings
from whiteduck.tasks.app import TasksModule
from whiteduck.templates import TemplateModule

# Install rich traceback handler for better error display
install()
console = Console()


def display_banner() -> None:
    banner_text = Text(
        """
              WWW      dWb WWW                 WWW                   WWW      
              WWW      YWP WWW                 WWW                   WWW      
              WWW          WWW                 WWW                   WWW      
WWW  WWW  WWW WWWWWb.  WWW WWWWWW .dWWb.   .dWWWWW WWW  WWW  .dWWWWb WWW  WWW 
WWW  WWW  WWW WWW "WWb WWW WWW   dWP  YWb dWW" WWW WWW  WWW dWWP"    WWW .WWP 
WWW  WWW  WWW WWW  WWW WWW WWW   WWWWWWWW WWW  WWW WWW  WWW WWW      WWWWWWK  
YWWb WWW dWWP WWW  WWW WWW YWWb. YWb.     YWWb WWW YWWb WWW YWWb.    WWW "WWb 
 "YWWWWWWWP"  WWW  WWW WWW  "YWWW "YWWWW   "YWWWWW  "YWWWWW  "YWWWWP WWW  WWW 
""",
        justify=STYLE_SPEC["banner"]["justify"],
        style=STYLE_SPEC["banner"]["text_style"],
    )
    console.print(banner_text)
    console.print(
        f"[bold]{__version__}[/] - new templating! - [bold]whiteduck GmbH[/] - [cyan]https://whiteduck.de[/]\n"
    )


def get_git_user_info() -> Tuple[Optional[str], Optional[str]]:
    """Retrieve Git user name and email from the local Git configuration."""
    try:
        # Check if Git is available
        subprocess.check_output(["which", "git"])

        # Retrieve Git user name
        user_name = (
            subprocess.check_output(
                ["git", "config", "--get", "user.name"], stderr=subprocess.DEVNULL
            )
            .strip()
            .decode("utf-8")
        )

        # Retrieve Git user email
        user_email = (
            subprocess.check_output(
                ["git", "config", "--get", "user.email"], stderr=subprocess.DEVNULL
            )
            .strip()
            .decode("utf-8")
        )

        return user_name, user_email

    except subprocess.CalledProcessError:
        logger.error(
            "Failed to retrieve Git user info. Please ensure Git is configured correctly."
        )
    except FileNotFoundError:
        logger.error("Git is not installed or not available in the PATH.")

    return None, None


def setup_logging(verbose: bool) -> None:
    """Configure logging based on the verbosity flag."""
    logger.remove()
    if verbose:
        logger.add(sys.stderr, level="DEBUG")
        click.echo("Verbose mode is ON. Running in development mode.")
    else:
        logger.add("file.log", level="ERROR")


def gather_env_vars() -> Dict[str, str]:
    """Gather environment variables and Git user info into a dictionary."""
    env_vars = dict(os.environ)
    git_user_name, git_user_email = get_git_user_info()

    if git_user_name:
        env_vars["GIT_USER_NAME"] = git_user_name
        logger.info(f"Git user name: {git_user_name}")
    if git_user_email:
        env_vars["GIT_USER_EMAIL"] = git_user_email
        logger.info(f"Git user email: {git_user_email}")

    return env_vars


def get_modules() -> List[BaseModule]:
    style = Style()
    settings_dic = {
        "style": style,
        "other": "other",
    }
    return [
        TemplateModule(),
        TasksModule(),
        Settings(settings_dic),
    ]


def run_cli() -> None:
    """Main entry point for the CLI application."""
    console.clear()
    display_banner()
    console.print(
        "[bold blue]🔥 whiteduck's Awesome Dev Tools 🔥[/] - A strange collection of weird tools... perfectly fit for a small white duck 🦆\n"
    )
    console.print(Markdown("---------------------\n\n"))
    console.line(1)

    modules = get_modules()

    try:
        while True:
            choices = [
                f"{module.get_name()} - {module.get_description()}"
                for module in modules
            ]
            choices.append("Exit - Goodbye! 👋")

            mode = questionary.select(
                "Choose a Mode\n",
                instruction=" ",
                qmark="🚀 ",
                choices=choices,
            ).ask()

            if mode == "Exit - Goodbye! 👋":
                console.print(
                    "[bold green]🎉 Thank you for using whiteduck's Awesome Dev Tools. Goodbye! 👋[/bold green]"
                )
                break

            selected_module = next(
                module
                for module in modules
                if f"{module.get_name()} - {module.get_description()}" == mode
            )
            console.line(1)
            selected_module.run()

    except KeyboardInterrupt:
        console.print("\n[yellow]🔄 Returning to mode selection...[/yellow]\n")
        run_cli()


@click.command()
@click.option(
    "-v", "--verbose", is_flag=True, help="Enable verbose output and development mode"
)
def main(verbose: bool) -> None:
    """Main entry point for the application."""
    # style = Style()
    # style.apply(style._3024_night)
    setup_logging(verbose)

    # Set template directory based on verbose mode
    templates_dir = "dev_templates" if verbose else "templates"

    # Gather all environment variables and log them
    global GLOBAL_VARS
    GLOBAL_VARS = gather_env_vars()

    for name, value in GLOBAL_VARS.items():
        logger.info(f"{name}: {value}")

    # Set the global template directory
    global TEMPLATES_DIR
    TEMPLATES_DIR = templates_dir

    # Run the CLI application
    run_cli()


if __name__ == "__main__":
    main()
