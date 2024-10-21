from typing import List, Optional, TypeVar

from loguru import logger

from whiteduck.templates.model.prompt import Prompt
from whiteduck.templates.model.util_classes import Condition, Module, Variable

# Type variable for generalized find_by_id function
T = TypeVar("T", Prompt, Module)


def find_by_id(item_id: str, items: List[T], id_attr: str = "id") -> Optional[T]:
    """
    Generalized function to find an item by its ID attribute.

    Args:
        item_id (str): The ID of the item to find.
        items (List[T]): List of items with an 'id' attribute.
        id_attr (str): The attribute name to use for ID comparison (default is 'id').

    Returns:
        Optional[T]: The item if found, otherwise None.
    """
    return next(
        (item for item in items if getattr(item, id_attr, None) == item_id), None
    )


def find_prompt_by_id(prompt_id: str, prompts: List[Prompt]) -> Optional[Prompt]:
    """
    Find a prompt by its ID in a list of Prompt objects.

    Args:
        prompt_id (str): The ID of the prompt to find.
        prompts (List[Prompt]): The list of available Prompt objects.

    Returns:
        Optional[Prompt]: The matching Prompt object, or None if not found.
    """
    return find_by_id(prompt_id, prompts)


def find_module_by_id(module_id: str, modules: List[Module]) -> Optional[Module]:
    """
    Find a module by its ID in a list of Module objects.

    Args:
        module_id (str): The ID of the module to find.
        modules (List[Module]): The list of available Module objects.

    Returns:
        Optional[Module]: The matching Module object, or None if not found.
    """
    return find_by_id(module_id, modules)


def check_condition(conditions: List[Condition], variables: List[Variable]) -> bool:
    """
    Check if all conditions are met based on the current variables.

    Args:
        conditions (List[Condition]): A list of Condition objects specifying required variable states.
        variables (List[Variable]): The dictionary of Variable objects to check against.

    Returns:
        bool: True if all conditions are met, otherwise False.
    """
    if not conditions:
        return True

    for condition in conditions:
        var_name = condition.var
        expected_value = condition.value
        actual_value = str(
            next((var.value for var in variables if var.id == var_name), "")
        )

        if actual_value != str(expected_value):
            logger.info(
                f"Condition not met: {var_name}={expected_value} (actual={actual_value})"
            )
            return False
    return True
