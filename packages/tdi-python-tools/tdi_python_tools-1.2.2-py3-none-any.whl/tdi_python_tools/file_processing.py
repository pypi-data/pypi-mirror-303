import argparse
import sys
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from typing import Self

from .ux_ui import get_user_choice_from_iterable


@dataclass(slots=True, frozen=True)
class FilesIO:
    import_dir: Path | None
    export_dir: Path | None
    import_filepaths: list[Path]

    @classmethod
    def from_args(cls, args: argparse.Namespace) -> Self:
        if args.import_filepaths:
            import_dir = None
            export_dir = None
            import_filepaths = [Path(filepath) for filepath in args.import_filepaths if filepath.endswith(".csv")]
        elif args.dir:
            import_dir = Path(f"./data/import/{args.dir}")
            import_dir.mkdir(parents=True, exist_ok=True)
            export_dir = Path(f"./data/export/{args.dir}")
            export_dir.mkdir(parents=True, exist_ok=True)
            import_filepaths = sorted(import_dir.glob("*.csv"))
        else:
            import_dir = Path("./data/import")
            export_dir = Path("./data/export")
            import_filepaths = [
                get_user_file(message="Enter the number of the file to process", import_directory=import_dir),
            ]

        return cls(import_dir=import_dir, export_dir=export_dir, import_filepaths=import_filepaths)


@dataclass(slots=True)
class FileProcessor:
    """Grouped collection of related Path objects, for use in importing and exporting a single file."""

    import_filepath: Path
    import_dir: Path | None
    export_dir: Path | None


def get_file_processor(
    raw_filepath: str | None,
    user_file_message: str = "Enter the number of the file you wish to process",
    subdirectory: str | None = None,
    import_file_extension: str = ".csv",
) -> FileProcessor:
    """Returns a FileProcessor for processing a single file, whether from command line args, or chosen by user input.

    If `raw_filepath` is given (i.e. from command line args), no further user input is required and no new directories
    need to be created (the directory of the filepath is used as the working directory for import and export). The
    filepath given must have the same extension as `import_file_extension`.

    Otherwise, `user_file_message` is displayed to the user, along with a list of all files from "./data/import"
    which have `import_file_extension`. "./data/import" and "./data/export" will be automatically created if not
    present. If `subdirectory` is given, a subdirectory in the above mentioned directories will also be created, and
    those are chosen as the working directories for import/export.

    Args:
        raw_filepath (str | None): String path to a file, usually from the command line args.
        user_file_message (str): Message to display to the user to help them choose the correct file.
        subdirectory (str, optional): Subdirectory inside import or export directories to read/write from or to.
        import_file_extension (str, optional): Filetype to show the user when choosing file. Defaults to ".csv".

    Returns:
        FileProcessor
    """
    if raw_filepath:
        import_dir = None
        export_dir = None
        import_filepath = get_filepath(raw_filepath, import_file_extension)

        if not import_filepath:
            print("Import file was not valid for this script")
            sys.exit()
    else:
        import_dir, export_dir = get_import_export_dirs(import_name=subdirectory)
        import_filepath = get_user_file(message=user_file_message, file_extension=import_file_extension)

    return FileProcessor(import_filepath=import_filepath, import_dir=import_dir, export_dir=export_dir)


@dataclass(slots=True)
class MultiFileProcessor:
    """Grouped collection of related Path objects, for use in importing and exporting multiple files in batch."""

    import_filepaths: list[Path]
    import_dir: Path | None
    export_dir: Path | None


def get_multi_file_processor(
    raw_filepaths: list[str] | None,
    user_file_message: str,
    subdirectory: str | None = None,
    import_file_extension: str = ".csv",
    *,
    batch: bool,
) -> MultiFileProcessor:
    """Returns a MultiFileProcessor for processing files, whether from command line args, or chosen by user input.

    If `raw_filepaths` is given (i.e. from command line args), no further user input is required and no new directories
    need to be created (the directory of the filepath is used as the working directory for import and export). The
    files in the filepath given must have the same extension as `import_file_extension`.

    Otherwise, "./data/import" and "./data/export" will be automatically created if not present. If
    `subdirectory` is given, a subdirectory in the above mentioned directories will also be created, and those are
    chosen as the working directories for import and export.

    If `batch`, all files of `import_file_extension` type from the working directory will be processed.

    Otherwise, `user_file_message` is displayed to the user, along with a list of all files from the working directory
    which have `import_file_extension`, and the user can choose a single file to process.

    Args:
        raw_filepaths (list[str] | None): List of str filepaths - usually from command line args.
        batch (bool): Process all files in the working directory. Display `user_file_message` and process a single file
            if not. Does nothing if `raw_filepaths` were given.
        user_file_message (str): Message to display to the user to help them choose the correct file. Does nothing if
            `batch` is True.
        subdirectory (str | None, optional): Subdirectory in import and export directories to process files from. Does
            nothing if `raw_filepaths` are given. Directory will be created if it does not exist. Defaults to None.
        import_file_extension (str, optional): Filetype to add to MultiFileProcessor or to offer to user to choose from.
            Defaults to ".csv".

    Returns:
        MultiFileProcessor
    """
    if raw_filepaths:
        import_dir = None
        export_dir = None

        import_filepaths: list[Path] = []
        for raw_filepath in raw_filepaths:
            if import_filepath := get_filepath(raw_filepath, import_file_extension):
                import_filepaths.append(import_filepath)  # noqa: PERF401
    else:
        import_dir, export_dir = get_import_export_dirs(import_name=subdirectory)
        if batch:
            import_filepaths = list(import_dir.glob(f"*{import_file_extension}"))
        else:
            import_filepaths = [get_user_file(message=user_file_message)]

    if not import_filepaths:
        print("No valid import files provided for this script")
        sys.exit()

    return MultiFileProcessor(import_filepaths=sorted(import_filepaths), import_dir=import_dir, export_dir=export_dir)


def get_import_export_dirs(import_name: str | None = None, export_name: str | None = None) -> tuple[Path, Path]:
    """Returns a tuple of an import and export filepath, for use in csv reading and writing.

    Creates directories and any parent directories if required.

    Args:
        import_name (Optional[str], optional): Directory name to use inside "./data/import", if any. Defaults to None.
        export_name (Optional[str], optional): Directory name to use inside "./export", if any. Defaults to None.

    Returns:
        tuple[Path, Path]: import filepath and export filepath as a tuple.
    """
    import_dir = f"./data/import/{import_name}" if import_name else "./data/import"

    if export_name:
        export_dir = f"./data/export/{export_name}"
    elif import_name:
        export_dir = f"./data/export/{import_name}"
    else:
        export_dir = "./data/export"

    import_path = Path(import_dir)
    export_path = Path(export_dir)

    # Creating directories, if needed
    import_path.mkdir(parents=True, exist_ok=True)
    export_path.mkdir(parents=True, exist_ok=True)

    return import_path, export_path


def get_user_file(
    message: str,
    import_directory: Path | None = None,
    file_extension: str = ".csv",
    filename_contains: str | None = None,
) -> Path:
    """Gets the user's csv import file choice from `import_directory`. Quits if no files in `import_directory`.

    Args:
        message (str): Message to be displayed to the user to help them to choose the correct file.
        import_directory (Path, optional): Import path to display csv files from. Defaults to Path("./data/import").
        file_extension (str, optional): File extension to filter files by. Defaults to ".csv".
        filename_contains (str, optional): String to filter filenames by. Defaults to None.

    Returns:
        Path: User's import csv file choice
    """
    if not import_directory:
        import_directory = Path("./data/import")

    if not (filenames := sorted(import_directory.glob(f"*{file_extension}"))):
        # Exit if there are no files in the import folder
        print("\nNo files found")
        sys.exit()
    else:
        if filename_contains:
            filenames = [filename for filename in filenames if filename_contains in filename.stem]
        print("\n" + "INPUT FILES FOUND".center(40, "-"))

        while True:
            file = get_user_choice_from_iterable(objects=filenames, message=message, item_header="Filename")
            if file is not None:
                return file


def get_optional_user_file(
    message: str,
    import_directory: Path | None = None,
    file_extension: str = ".csv",
    filename_contains: str | None = None,
) -> Path | None:
    """Gets the user's csv import file choice from `import_directory`. Returns None if no files in `import_directory`.

    Ensure the `message` to the user informs them that they can enter "n" to skip file selection.

    Args:
        message (str): Message to be displayed to the user to help them to choose the correct file.
        import_directory (Path, optional): Import path to display csv files from. Defaults to Path("./data/import").
        file_extension (str, optional): File extension to filter files by. Defaults to ".csv".
        filename_contains (str, optional): String to filter filenames by. Defaults to None.

    Returns:
        Path | None: User's import csv file choice
    """
    if not import_directory:
        import_directory = Path("./data/import")

    filenames = sorted(import_directory.glob(f"*{file_extension}"))

    if filename_contains:
        filenames = [filename for filename in filenames if filename_contains in filename.stem]

    if not (filenames := sorted(import_directory.glob(f"*{file_extension}"))):
        # Exit if there are no files in the import folder
        print("\nNo files found")
        return None

    print("\n" + "INPUT FILES FOUND".center(40, "-"))
    return get_user_choice_from_iterable(objects=filenames, message=message, item_header="Filename")


def get_filepath(raw_filepath: str, file_extension: str) -> Path | None:
    """Returns a Path object if `raw_filepath`'s file extension matches `file_extension`. Returns None otherwise.

    Args:
        raw_filepath (str): String filepath to a file
        file_extension (str): Extension to check `raw_filepath` against.

    Returns:
        Path | None
    """
    if raw_filepath.endswith(file_extension):
        return Path(raw_filepath)
    return None


def get_export_filepath(
    import_filepath: Path,
    export_dir: Path | None,
    export_filename: str | None = None,
    file_extension: str = ".csv",
) -> Path:
    """Returns a suitable export Path for a file, based on where the file will be exported to, keeping original name.

    If `export_dir`, simply change the directory from `import_filepath` and change `file_extension` if necessary.

    Otherwise, simply adds "output" to the end of the filename with `file_extension` as the extension, in the same
    directory as `import_filepath`.

    Args:
        import_filepath (Path): Path to the import file.
        export_dir (Path | None): Path to where the export file will be saved. Leave as None if the export file will be
            saved to the same location as the import file.
        export_filename (str, optional): Filename to use for the export file. Uses the import_filepath with "output"
            appended if None.
        file_extension (str, optional): Extension to be used on the export filepath. Defaults to ".csv".

    Returns:
        Path
    """
    if not export_filename:
        export_filename = import_filepath.stem
    if export_dir:
        return export_dir / f"{export_filename}{file_extension}"
    return import_filepath.with_name(f"{export_filename}_output{file_extension}")


def download_file(file_name: str, download_url: str, export_path: Path) -> None:
    """Downloads file from a URL and saves and renames the file using an export path.

    Args:
        file_name (str): A string of the file name
        download_url (str): A string of the URL to download
        export_path (Path): A Path detailing where the file is to be saved to.
    """
    save_directory = export_path / file_name
    _ = urllib.request.urlretrieve(download_url, save_directory)  # noqa: S310
