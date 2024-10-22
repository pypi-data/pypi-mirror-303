from typing import Any, List, Type

from chainalysis._exceptions import BadRequest


def get_list_type(_list: List[Any]) -> Type:
    """
    Return the type of list elements if all are the same type, otherwise raise an error.
    """
    if not _list:
        raise ValueError("The list is empty and has no element type.")

    element_types = {type(item) for item in _list}

    if len(element_types) > 1:
        raise BadRequest(
            f"The list contains multiple types: {element_types}. Enter a list with only numbers, strings, or bools."
        )

    return element_types.pop()
