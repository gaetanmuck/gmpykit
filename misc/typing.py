from typing import Any, List, Type
import pandas as pd


class TypeValidationError(TypeError):
    def __init__(self, message: str):
        super().__init__(message)


def validate(variable: Any, possible_classes: List[Type]) -> None:
    """
    Validates if the variable is an instance of any class in the possible_classes list.

    Args:
        variable: The variable to check.
        possible_classes: A list of class constructors to validate against.
        variable_name: the name of the variable (for error logs).
    Raises:
        TypeValidationError: If the variable is not an instance of any of the provided classes.
    """
    if not any(isinstance(variable, cls) for cls in possible_classes):
        expected_types = ", ".join(cls.__name__ for cls in possible_classes)
        found_type = type(variable).__name__
        raise TypeValidationError(
            f"Expected one of [{expected_types}], but found [{found_type}]"
        )


def validate_enum(
    variable: str | int | float, correct_values: List[str | int | float]
) -> None:

    if not variable in correct_values:
        expected_values = ", ".join(value for value in correct_values)
        found_value = variable
        raise TypeValidationError(
            f"Expected one of [{expected_values}], but found [{found_value}]"
        )


def validate_dict(obj: dict, key_type: type, value_type: type):

    if not isinstance(obj, dict):
        raise TypeValidationError(
            f"Object is supposed to be a dictonnary, but is actually a {type(obj).__name__}."
        )

    for key, value in dict.items():
        if not isinstance(key, key_type):
            raise TypeValidationError(
                f"Key is expected to be of type {key_type.__name__}, but is actually of type {type(key).__name__}."
            )

        if not isinstance(value, value_type):
            raise TypeValidationError(
                f"Value is expected to be of type {value_type.__name__}, but is actually of type {type(value).__name__}."
            )


def validate_iterable(array: list | pd.Series, item_type: type):

    if not isinstance(array, list) and not isinstance(array, pd.Series):
        raise TypeValidationError(
            f"Object is supposed to be an iterable, but is actually a {type(obj).__name__}."
        )

    for item in array:
        if not isinstance(item, item_type):
            raise TypeValidationError(
                f"Item of iterable is supposed to be an {item_type.__name__}, but is actually a {type(item).__name__}."
            )


def validate_tuple(tpl: tuple, types: List[type]):

    if not isinstance(tpl, tuple):
        raise TypeValidationError(
            f"Object is supposed to be an iterable, but is actually a {type(obj).__name__}."
        )

    for i, value in enumerate(tpl):
        if not isinstance(value, types[i]):
            raise TypeValidationError(
                f"Item of tuple is supposed to be an {type(types[i]).__name__}, but is actually a {type(value).__name__}."
            )


def validate_iterable_tuple(iterable: list | pd.Series, types: List[type]):

    # Validate the container
    validate_iterable(iterable, tuple)

    # Validate the content
    for i, item in enumerate(iterable):
        validate_tuple(item, types)
