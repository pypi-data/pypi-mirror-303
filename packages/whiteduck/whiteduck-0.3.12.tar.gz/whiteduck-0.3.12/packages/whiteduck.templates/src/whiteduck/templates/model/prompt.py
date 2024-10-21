from typing import Any, List, Optional

from loguru import logger
from msgspec import Struct


class Prompt(Struct):
    id: str
    prompt: str
    display_name: Optional[str] = None
    default: Optional[str] = None
    url: Optional[str] = None
    type: Optional[str] = "text"
    value_set: Optional[List[Any]] = None
    description: Optional[str] = None
    show_description: Optional[bool] = False
    out: Optional[str] = None

    def __post_init__(self) -> None:
        logger.info(f"Initialized Prompt with id: {self.id}, prompt: {self.prompt}, type: {self.type}")
