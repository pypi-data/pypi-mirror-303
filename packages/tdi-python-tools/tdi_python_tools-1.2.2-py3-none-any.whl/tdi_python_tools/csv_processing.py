import csv
from collections.abc import Iterable
from pathlib import Path
from typing import Any

from .ux_ui import get_user_choice_from_iterable


def column_selector(headers: Iterable[str]) -> str:
    """Returns a column name from `headers`, chosen by the user.

    Args:
        headers (list[str]): A list of available column headers.

    Returns:
        str: A column name.
    """
    print("Available columns:")
    headers = sorted(headers)
    while True:
        column = get_user_choice_from_iterable(
            headers,
            "Please enter the number of the column you wish to select",
            item_header="Column",
        )
        if column is not None:
            return column


def limited_output_csv(
    export_filepath: Path,
    headers: Iterable[str],
    rows: Iterable[dict[str, Any]],
    limit: int,
) -> None:
    """Exports rows of data to multiple CSV files, each containing a limited number of rows.

    Writes the provided rows of data to multiple CSV files, with each file containing a maximum of 'limit' rows. If the
    total number of rows exceeds 'limit', multiple CSV files will be created. The CSV files will have the same column
    headers as specified in the 'headers' parameter. The CSV files are named based on the 'export_filepath' parameter
    with an additional index appended to differentiate the files. The function outputs the number of rows and files
    created.

    Args:
        export_filepath (Path): The file path to export the CSV files to.
        headers (Iterable[str]): The column headers of the CSV file.
        rows (Iterable[dict[str, Any]]): The rows of data to be written to the CSV files.
        limit (int): The maximum number of rows to be written to each CSV file.
    """
    file_number = 0
    row_number = 0

    while True:
        # Export until there are no more rows left
        try:
            file_number += 1
            current_export_filepath = export_filepath.with_name(f"{export_filepath.stem}_{file_number}.csv")
            with Path(current_export_filepath).open(
                "w",
                newline="",
                encoding="utf-8-sig",
            ) as output_file:
                output_writer = csv.DictWriter(
                    output_file,
                    fieldnames=list(headers),
                    delimiter=",",
                    extrasaction="ignore",
                )

                # Headers
                output_writer.writeheader()

                # Write next row until limit is reached for that file, then start again in the next file
                for _ in range(limit):
                    row = next(rows)  # pyright: ignore[reportUnknownVariableType, reportArgumentType]
                    row_number += 1
                    output_writer.writerow(row)  # type: ignore  # noqa: PGH003

        except StopIteration:
            # No rows left to process
            break

    print(f"Output {row_number} rows into {file_number} file(s)")
