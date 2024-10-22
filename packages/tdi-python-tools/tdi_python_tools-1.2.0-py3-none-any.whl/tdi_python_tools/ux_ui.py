import sys
from collections.abc import Sequence
from datetime import date
from functools import cache
from pathlib import Path
from typing import TypeVar

from tabulate import tabulate

T = TypeVar("T")


def print_header(text: str) -> None:
    """Prints formatted header, which is printed in the middle of 2 lines of 80 "=" characters.

    Args:
        text (str): The text to be printed in the header.

    Notes:
        - Text is centered in the middle of the 80 character line.
    """
    print("=" * 80)
    print(f"{text:^80}")
    print("=" * 80)


def print_subheader(text: str) -> None:
    """Prints formatted subheader, which is printed above a line of 80 "-" characters.

    Args:
        text (str): The text to be printed as the subheader.

    Notes:
        - Text is centered in the middle of the 80 character line.
    """
    print(f"{text:^80}")
    print("-" * 80)


def get_input(message: str) -> str:
    """Prints `message` and asks for the user's input on a second line.

    Args:
        message (str): The message to be displayed to the user.

    Returns:
        str: The user's input.
    """
    print(message)
    return input("> ")


def get_bool_input(message: str) -> bool:
    """Prompts the user to enter a boolean value.

    The message is printed as a prompt to the user, and the user is expected to enter 'y' or 'n' to indicate their
    choice. The function will continue to prompt the user until a valid input is entered.
    """
    while True:
        user_input = get_input(message).strip().lower()

        if user_input in {"y", "yes", "ok"}:
            return True
        if user_input in {"n", "no"}:
            return False
        print("Please enter 'y' or 'n'")


def get_int_input(message: str, min_value: int | None = None, max_value: int | None = None) -> int | None:
    """Prompts the user to enter an integer value within a specified range or opt not to make selection.

    User is required to enter "n" if they wish to not make a selection.

    Ensure the `message` to the user informs them of the range of valid inputs.

    Args:
        message (str): A string message that is printed as a prompt to the user.
        min_value (int, optional): An optional integer value that sets the minimum allowed value for the input.
            If no minimum value is specified, None is used as a default. Defaults to None.
        max_value (int, optional): An optional integer value that sets the maximum allowed value for the input.
            If no maximum value is specified, None is used as a default. Defaults to None.

    Raises:
        ValueError: If min_value is greater than max_value (if both are provided).

    Returns:
        int | None: The integer value entered by the user or None if the user opts to not make a selection.

    Example:
        >>> get_int("Enter a number between 1 and 10: ", 1, 10)
        Enter a number between 1 and 10:
        > 5
        5
    """
    print(message)
    if min_value and max_value and min_value > max_value:
        msg = "min_value must be less than or equal to max_value"
        raise ValueError(msg)
    while True:
        # Checking if user wants make no choice and return None if not
        user_input = input("> ").lower().strip()
        if user_input == "n":
            return None

        # otherwise, checking if user input is a valid integer and returns it
        try:
            user_int = int(user_input)
            if (min_value is not None and user_int < min_value) or (max_value is not None and user_int > max_value):
                msg = "Not within limits"
                raise ValueError(msg)  # noqa: TRY301
        except ValueError:
            print("Please enter a valid number")
        else:
            return user_int


def get_user_choice_from_iterable(objects: Sequence[T], message: str, item_header: str = "Item") -> T | None:
    """Display a list of objects to the user and prompt them to select one or None by entering its index number.

    User is required to enter "n" if they wish to not make a selection.

    Ensure the `message` to the user informs them of the range of valid inputs.

    Args:
        objects: A sequence of objects to choose from.
        message: A prompt message to display to the user when requesting their input.
        item_header: A string to use as the header for the items in the list.

    Returns:
        The selected object from the input sequence or None if user opts to not make a selection.
    """

    def get_values() -> list[tuple[int, T | str]]:
        values: list[tuple[int, T | str]] = []
        for index, obj in enumerate(objects, start=1):
            object_title = obj.name if isinstance(obj, Path) else obj
            values.append((index, object_title))

        return values

    print(tabulate(get_values(), headers=["#", item_header], tablefmt="simple_outline"))

    # Checking if user opted to not make selection
    if (user_choice := get_int_input(message=message, min_value=1, max_value=len(objects))) is None:
        return None

    # if valid integer is entered, return the respective object
    return objects[user_choice - 1]


def get_date_input(message: str) -> date:
    print(message)

    try:
        user_date = date.fromisoformat(input("(Enter in YYYY-MM-DD) > "))
    except ValueError:
        print("Please enter a valid date in the format YYYY-MM-DD")
        return get_date_input(message)
    return user_date


@cache
def get_user_acknowledgement(message: str) -> None:
    print(message)
    response = input("Continue? (Y/n) > ").lower().strip()
    if response == "n":
        sys.exit()
