from typing import List, Optional

from loguru import logger
from msgspec import Struct, field

from whiteduck.templates.model.util_classes import Condition


class Step(Struct):
    type: str
    value: str | dict | list
    title: Optional[str] = None
    condition: Optional[List[Condition]] = field(default_factory=list)

    def __post_init__(self) -> None:
        logger.info(
            f"Initialized Step with title: {self.title}, type: {self.type}, value: {self.value}"
        )
