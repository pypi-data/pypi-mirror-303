from collections.abc import Sequence
from datetime import date
from pathlib import Path
from typing import TypeVar

import pytest

from src.tdi_python_tools.ux_ui import get_bool_input, get_date_input, get_int_input, get_user_choice_from_iterable


@pytest.mark.parametrize(
    argnames=("message, min_value, max_value, input_values, expected_output"),
    argvalues=(
        ("Enter a number: ", None, None, [1], 1),
        ("Enter a number greater than 10: ", 11, None, [5, 10, 11, 15], 11),
        ("Enter a number between 1 and 10: ", 1, 10, [0, 5, 10, 11], 5),
        ("Enter 'n' to not provide a number: ", None, None, ["n"], None),
    ),
)
def test_get_int(  # noqa: PLR0913, PLR0917
    message: str,
    min_value: int | None,
    max_value: int | None,
    input_values: list[int],
    expected_output: int,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    # Monkeypatch the input() function to simulate user input
    monkeypatch.setattr("builtins.input", lambda _: str(input_values.pop(0)))

    # Call the get_int() function with the given arguments and assert the output
    assert get_int_input(message, min_value, max_value) == expected_output


@pytest.mark.parametrize(
    argnames=("message, input_values, expected_output"),
    argvalues=(
        ("Enter 'y' or 'n': ", ["y"], True),
        ("Enter 'y' or 'n': ", ["n"], False),
        ("Enter 'y' or 'n': ", ["yes"], True),
        ("Enter 'y' or 'n': ", ["no"], False),
        ("Enter 'y' or 'n': ", ["ok"], True),
        ("Enter 'y' or 'n': ", ["Y"], True),
        ("Enter 'y' or 'n': ", ["N"], False),
        ("Enter 'y' or 'n': ", ["YES"], True),
        ("Enter 'y' or 'n': ", ["NO"], False),
        ("Enter 'y' or 'n': ", ["OK"], True),
        ("Enter 'y' or 'n': ", ["invalid", "y"], True),
        ("Enter 'y' or 'n': ", ["invalid", "n"], False),
    ),
)
def test_get_bool_input(
    message: str,
    input_values: list[str],
    expected_output: bool,  # noqa: FBT001
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    # Monkeypatch the input() function to simulate user input
    monkeypatch.setattr("builtins.input", lambda _: input_values.pop(0))

    # Call the get_bool_input() function with the given arguments and assert the output
    assert get_bool_input(message) == expected_output


T = TypeVar("T")


@pytest.mark.parametrize(
    argnames=("objects, message, input_values, expected_output"),
    argvalues=(
        ([1, 2, 3], "Select a number: ", [1], 1),
        (["apple", "banana", "cherry"], "Select a fruit: ", [2], "banana"),
        ([Path("/path/to/file1"), Path("/path/to/file2")], "Select a file: ", [2], Path("/path/to/file2")),
    ),
)
def test_get_user_choice_from_iterable(
    objects: Sequence[T],
    message: str,
    input_values: list[int],
    expected_output: T,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    # Monkeypatch the input() function to simulate user input
    monkeypatch.setattr("builtins.input", lambda _: str(input_values.pop(0)))

    # Call the get_user_choice_from_iterable() function with the given arguments and assert the output
    assert get_user_choice_from_iterable(objects, message) == expected_output


@pytest.mark.parametrize(
    argnames=("message, input_values, expected_output"),
    argvalues=(
        ("Enter a date in the format YYYY-MM-DD: ", ["2021-01-01"], date(2021, 1, 1)),
        ("Enter a date in the format YYYY-MM-DD: ", ["2021-01-01", "2021-02-02"], date(2021, 1, 1)),
        ("Enter a date in the format YYYY-MM-DD: ", ["invalid", "2021-01-01"], date(2021, 1, 1)),
    ),
)
def test_get_date_input(
    message: str,
    input_values: list[str],
    expected_output: str,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    # Monkeypatch the input() function to simulate user input
    monkeypatch.setattr("builtins.input", lambda _: input_values.pop(0))

    # Call the get_date_input() function with the given arguments and assert the output
    assert get_date_input(message) == expected_output
