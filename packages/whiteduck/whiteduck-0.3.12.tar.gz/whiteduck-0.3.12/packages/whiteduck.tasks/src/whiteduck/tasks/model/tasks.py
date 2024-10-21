from typing import Any, Dict, List

from msgspec import Struct


class VSCodeTask(Struct):
    label: str
    type: str
    command: str
    args: List[str]
    group: Dict[str, Any]
    problem_matcher: str
    presentation: Dict[str, Any]

    def to_dict(self) -> Dict[str, Any]:
        return {
            "label": self.label,
            "type": self.type,
            "command": self.command,
            "args": self.args,
            "group": self.group,
            "problemMatcher": self.problem_matcher,
            "presentation": self.presentation,
        }


class PoeTask(Struct):
    name: str
    command: str
