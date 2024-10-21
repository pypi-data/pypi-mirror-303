from typing import Literal, Optional

from msgspec import Struct


class PoeTask(Struct):
    name: str
    command: str
    type: Literal["cmd", "sequence"]
    parent: Optional["PoeTask"] = None
    children: list["PoeTask"] = []

    def append_to_file(self, filename: str):
        with open(filename, "a") as file:
            if self.children:
                file.write(f"[tool.poe.tasks.{self.name}]\n")
                file.write("sequence = [\n")
                for child in self.children:
                    file.write(f'    {{ ref = "{child.name}" }},\n')
                file.write("]\n")
            else:
                file.write("[tool.poe.tasks._jupyter_libs]\n")
                file.write(f'cmd = "{self.command}"\n')
