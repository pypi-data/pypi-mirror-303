import json
import os

import questionary
from rich import inspect, print

from whiteduck.core.models import BaseModule


class Settings(BaseModule):
    def __init__(self, default_settings=None):
        self.filename = os.path.join(os.path.expanduser("~"), "wd.settings.json")
        self.default_settings = default_settings or {}
        self.settings = self.load_settings()

    def load_settings(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                try:
                    settings = json.load(file)
                    print("[green]Settings loaded successfully.[/green]")
                    return settings
                except json.JSONDecodeError:
                    print("[red]Error decoding settings file. Loading defaults.[/red]")
        return self.default_settings

    def save_settings(self):
        with open(self.filename, "w") as file:
            json.dump(self.settings, file, indent=4)
            print("[green]Settings saved successfully.[/green]")

    def set(self, key, value):
        self.settings[key] = value
        self.save_settings()

    def get(self, key, default=None):
        return self.settings.get(key, default)

    def configure(self):
        for key, value in self.default_settings.items():
            answer = questionary.text(f"Enter value for {key} (default: {value}): ", default=value).ask()
            self.settings[key] = answer
        self.save_settings()

    def run(self):
        print("[bold cyan]Settings 🛠️[/bold cyan]")
        print("[cyan]Configure settings for the application.[/cyan]")
        print("[cyan]Current settings:[/cyan]")
        for key, value in self.settings.items():
            print(f"[cyan]{key}[/cyan]: {inspect(value)}")
        print("\n")

        choices = ["Set a setting", "Configure settings", "Exit"]
        mode = questionary.select("Choose an action:", choices=choices).ask()

        if mode == "Set a setting":
            key = questionary.text("Enter setting key: ").ask()
            value = questionary.text("Enter setting value: ").ask()
            self.set(key, value)
        elif mode == "Configure settings":
            self.configure()
        elif mode == "Exit":
            return

    @classmethod
    def get_name(cls):
        return "Settings"

    @classmethod
    def get_description(cls):
        return "Configure settings 🛠️"
