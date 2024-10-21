import json
import os
from typing import Any, Dict, List, Optional

import questionary
import toml
from rich.console import Console
from rich.syntax import Syntax
from rich.table import Table
from rich.traceback import install
from rich.tree import Tree

from whiteduck.core.models.base_module import BaseModule
from whiteduck.tasks.model.tasks import PoeTask, VSCodeTask

# Install rich traceback handler for better error display
install()
console = Console()


class TasksModule(BaseModule):
    """
    TasksModule manages and synchronizes tasks between VSCode (tasks.json) and Poe (pyproject.toml).

    This module provides functionality to:
    1. Find task files (tasks.json and pyproject.toml) in the workspace.
    2. Parse and display VSCode and Poe tasks.
    3. Visualize the dependency between VSCode and Poe tasks.
    4. Synchronize Poe tasks to VSCode tasks.
    5. Edit existing VSCode and Poe tasks.
    6. Create new VSCode and Poe tasks.

    The module offers an interactive interface for users to manage and sync tasks,
    making it easier to maintain consistency between different task management systems.
    """

    @classmethod
    def get_name(cls):
        return "Tasks"

    @classmethod
    def get_description(cls):
        return (
            "Set up automatic tasks, like a local pipeline! 📋"
            + "\n------------------------"
        )

    def run(self):
        task_files = self.find_task_files()
        if not task_files:
            console.print("[yellow]No task files found.[/yellow]")
            return

        vscode_tasks_file = next(
            (f for f in task_files if f.endswith("tasks.json")), None
        )
        poe_tasks_file = next(
            (f for f in task_files if f.endswith("pyproject.toml")), None
        )

        if vscode_tasks_file and poe_tasks_file:
            self.display_task_dependency(vscode_tasks_file, poe_tasks_file)
            self.sync_tasks_menu(vscode_tasks_file, poe_tasks_file)
        else:
            console.print(
                "[yellow]Both tasks.json and pyproject.toml files are required.[/yellow]"
            )

    def find_task_files(self) -> List[str]:
        """Find pyproject.toml and tasks.json files in the workspace."""
        task_files = []
        for root, _, files in os.walk(os.getcwd()):
            for file in files:
                if file in ["pyproject.toml", "tasks.json"]:
                    task_files.append(os.path.join(root, file))
        return task_files

    def parse_vscode_tasks(self, file_path: str) -> List[VSCodeTask]:
        with open(file_path, "r") as f:
            data = json.load(f)

        tasks = []
        for task_data in data.get("tasks", []):
            task = VSCodeTask(
                label=task_data.get("label", ""),
                type=task_data.get("type", ""),
                command=task_data.get("command", ""),
                args=task_data.get("args", []),
                group=task_data.get("group", {}),
                problem_matcher=task_data.get("problemMatcher", ""),
                presentation=task_data.get("presentation", {}),
            )
            tasks.append(task)
        return tasks

    def parse_poe_tasks(self, file_path: str) -> Dict[str, PoeTask]:
        with open(file_path, "r") as f:
            data = toml.load(f)

        poe_tasks = {}
        for name, command in (
            data.get("tool", {}).get("poe", {}).get("tasks", {}).items()
        ):
            if isinstance(command, str):
                poe_tasks[name] = PoeTask(name=name, command=command)
            elif isinstance(command, list):
                poe_tasks[name] = PoeTask(name=name, command=", ".join(command))
        return poe_tasks

    def display_task_dependency(self, vscode_file: str, poe_file: str) -> None:
        console.line(2)
        vscode_tasks = self.parse_vscode_tasks(vscode_file)
        poe_tasks = self.parse_poe_tasks(poe_file)

        tree = Tree("Task Dependency")
        vscode_node = tree.add(
            "[cyan]VSCode Tasks[/cyan]\n   [magenta]Poe Tasks[/magenta]"
        )
        # poe_node = vscode_node.add("")

        for vscode_task in vscode_tasks:
            if "poe" in vscode_task.command or "poe" in vscode_task.args:
                poe_task_name = vscode_task.args[-1] if vscode_task.args else ""
                if poe_task_name in poe_tasks:
                    poe_task = poe_tasks[poe_task_name]
                    vscode_task_node = vscode_node.add(
                        f"[cyan bold]{vscode_task.label}[/cyan bold][green] → {poe_task_name}[/green]"
                    )
                    vscode_task_node.add(
                        f"[magenta bold]{poe_task_name} →[/magenta bold]  [magenta]{poe_task.command}[/magenta]"
                    )
                    # Remove the task from poe_tasks to avoid duplication
                    del poe_tasks[poe_task_name]

        # Add remaining Poe tasks that are not linked to VSCode tasks
        if poe_tasks:
            other_poe_node = tree.add("Other Poe Tasks")
            for name, poe_task in poe_tasks.items():
                other_poe_node.add(f"[magenta]{name}[/magenta]: {poe_task.command}")

        console.print(tree)

    def sync_tasks_menu(self, vscode_file: str, poe_file: str) -> None:
        while True:
            console.line(2)

            choice = questionary.select(
                "Task Synchronization Menu:",
                choices=[
                    "Sync Poe tasks to VSCode tasks",
                    "View current tasks",
                    "Edit existing task",
                    "Create new task",
                    "Exit",
                ],
                qmark="🚀",
                instruction=" ",
            ).ask()

            if choice == "Sync Poe tasks to VSCode tasks":
                self.sync_poe_to_vscode(vscode_file, poe_file)
            elif choice == "View current tasks":
                self.display_task_dependency(vscode_file, poe_file)
            elif choice == "Edit existing task":
                self.edit_vscode_task(vscode_file, poe_file)
            # elif choice == "Edit existing Poe task":
            #     self.edit_poe_task(poe_file)
            elif choice == "Create new task":
                self.create_new_task(vscode_file, poe_file)
            else:
                break

    def sync_poe_to_vscode(self, vscode_file: str, poe_file: str) -> None:
        vscode_tasks = self.parse_vscode_tasks(vscode_file)
        poe_tasks = self.parse_poe_tasks(poe_file)

        new_vscode_tasks = []
        for name, poe_task in poe_tasks.items():
            if not any(vt for vt in vscode_tasks if vt.label == name):
                new_vscode_task = VSCodeTask(
                    label=name,
                    type="process",
                    command="uv",
                    args=["run", "poe", name],
                    group={"kind": "test", "isDefault": True},
                    problem_matcher="$python",
                    presentation={
                        "echo": True,
                        "reveal": "always",
                        "focus": True,
                        "panel": "new",
                        "clear": False,
                    },
                )
                new_vscode_tasks.append(new_vscode_task)

        if new_vscode_tasks:
            with open(vscode_file, "r+") as f:
                data = json.load(f)
                data["tasks"].extend([task.to_dict() for task in new_vscode_tasks])
                f.seek(0)
                json.dump(data, f, indent=2)
                f.truncate()

            console.print(
                f"[green]Added {len(new_vscode_tasks)} new VSCode tasks.[/green]"
            )
        else:
            console.print("[yellow]No new tasks to add.[/yellow]")

    def edit_vscode_task(self, vscode_file: str, poe_file: str) -> None:
        vscode_tasks = self.parse_vscode_tasks(vscode_file)
        poe_tasks = self.parse_poe_tasks(poe_file)

        # Create combined list of choices
        task_choices = [
            f"{vscode_task.label} -> {vscode_task.command}###{poe_task}->{poe_tasks[poe_task]}"
            for vscode_task, poe_task in zip(vscode_tasks, poe_tasks.keys())
        ]

        ## Split the elements in task_choice by ### and flatten the list
        task_choices = [
            item for sublist in task_choices for item in sublist.split("###")
        ]

        task_name = questionary.select(
            "Select a VSCode task to edit:", choices=task_choices
        ).ask()

        if any(task_name.startswith(vscode_task.label) for vscode_task in vscode_tasks):
            console.print(
                f"[green]You have selected a VSCode task: {task_name}[/green]"
            )
        elif any(task_name.startswith(poe_task) for poe_task in poe_tasks.keys()):
            console.print(f"[blue]You have selected a POE task: {task_name}[/blue]")
        else:
            console.print(f"[red]Unknown task type: {task_name}[/red]")

        return
        selected_vscode_task_label = task_name.split(" → ")[0]
        task = next(
            task for task in vscode_tasks if task.label == selected_vscode_task_label
        )

        new_label = questionary.text(
            "Enter new label (leave empty to keep current):", default=task.label
        ).ask()
        new_command = questionary.text(
            "Enter new command (leave empty to keep current):", default=task.command
        ).ask()
        new_args = questionary.text(
            "Enter new arguments (comma-separated, leave empty to keep current):",
            default=",".join(task.args),
        ).ask()

        task.label = new_label or task.label
        task.command = new_command or task.command
        task.args = new_args.split(",") if new_args else task.args

        with open(vscode_file, "r+") as f:
            data = json.load(f)
            for i, t in enumerate(data["tasks"]):
                if t["label"] == task_name:
                    data["tasks"][i] = task.to_dict()
                    break
            f.seek(0)
            json.dump(data, f, indent=2)
            f.truncate()

        console.print(f"[green]Updated VSCode task: {task.label}[/green]")

    def edit_poe_task(self, poe_file: str) -> None:
        poe_tasks = self.parse_poe_tasks(poe_file)
        task_names = list(poe_tasks.keys())

        task_name = questionary.select(
            "Select a Poe task to edit:", choices=task_names
        ).ask()
        task = poe_tasks[task_name]

        new_name = questionary.text(
            "Enter new name (leave empty to keep current):", default=task.name
        ).ask()
        new_command = questionary.text(
            "Enter new command (leave empty to keep current):", default=task.command
        ).ask()

        task.name = new_name or task.name
        task.command = new_command or task.command

        with open(poe_file, "r") as f:
            data = toml.load(f)

        if "tool" not in data:
            data["tool"] = {}
        if "poe" not in data["tool"]:
            data["tool"]["poe"] = {}
        if "tasks" not in data["tool"]["poe"]:
            data["tool"]["poe"]["tasks"] = {}

        if task_name != new_name:
            del data["tool"]["poe"]["tasks"][task_name]
        data["tool"]["poe"]["tasks"][task.name] = task.command

        with open(poe_file, "w") as f:
            toml.dump(data, f)

        console.print(f"[green]Updated Poe task: {task.name}[/green]")

    def create_new_task(self, vscode_file: str, poe_file: str) -> None:
        task_type = questionary.select(
            "Select task type:", choices=["VSCode", "Poe"]
        ).ask()
        task_name = questionary.text("Enter task name:").ask()
        task_command = questionary.text("Enter task command:").ask()

        if task_type == "VSCode":
            new_task = VSCodeTask(
                label=task_name,
                type="process",
                command="uv",
                args=["run", "poe", task_name],
                group={"kind": "test", "isDefault": True},
                problem_matcher="$python",
                presentation={
                    "echo": True,
                    "reveal": "always",
                    "focus": True,
                    "panel": "new",
                    "clear": False,
                },
            )

            with open(vscode_file, "r+") as f:
                data = json.load(f)
                data["tasks"].append(new_task.to_dict())
                f.seek(0)
                json.dump(data, f, indent=2)
                f.truncate()

            console.print(f"[green]Created new VSCode task: {task_name}[/green]")

        elif task_type == "Poe":
            with open(poe_file, "r") as f:
                data = toml.load(f)

            if "tool" not in data:
                data["tool"] = {}
            if "poe" not in data["tool"]:
                data["tool"]["poe"] = {}
            if "tasks" not in data["tool"]["poe"]:
                data["tool"]["poe"]["tasks"] = {}

            data["tool"]["poe"]["tasks"][task_name] = task_command

            with open(poe_file, "w") as f:
                toml.dump(data, f)

            console.print(f"[green]Created new Poe task: {task_name}[/green]")

    def display_file_content(self, file_path: str) -> None:
        """Display the content of the selected file."""
        with open(file_path, "r") as f:
            content = f.read()

        file_extension = os.path.splitext(file_path)[1]
        lexer = "toml" if file_extension == ".toml" else "json"

        syntax = Syntax(content, lexer, theme="monokai", line_numbers=True)
        console.print(
            f"\n[bold green]Content of {os.path.basename(file_path)}:[/bold green]"
        )
        console.print(syntax)
