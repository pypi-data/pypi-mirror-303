from typing import Any, Dict, List, Optional

from loguru import logger
from msgspec import Struct, field


class Variable(Struct):
    id: str
    value: str | bool

    def __post_init__(self) -> None:
        logger.info(f"Initialized Variable with value: {self.value}")


class Condition(Struct):
    var: str
    value: Any

    def __post_init__(self) -> None:
        logger.info(f"Initialized Condition with var: {self.var}, value: {self.value}")


class Module(Struct):
    id: str
    type: str
    module_definition: str
    arguments: Optional[List[Dict[str, str]]] = field(default_factory=list)
    displayName: Optional[str] = None

    def __post_init__(self) -> None:
        logger.info(f"Initialized Module with id: {self.id}, type: {self.type}, arguments: {self.arguments}")


class Dependency(Struct):
    name: str


class WizardStepValues(Struct):
    prompt: str
    condition: Optional[List[Condition]] = field(default_factory=list)


class DependencyGroup(Struct):
    name: str
    environment: str
    description: str
    is_mandatory: bool
    dependencies: List[Dependency] = field(default_factory=list)

    def __post_init__(self) -> None:
        logger.info(f"Initialized DependencyGroup with name: {self.name}, environment: {self.environment}")


class DependencyWizard(Struct):
    id: str
    type: str
    title: Optional[str] = None
    values: List[DependencyGroup] = field(default_factory=list)
