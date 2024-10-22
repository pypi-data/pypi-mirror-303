import argparse

multi_import_file_parser = argparse.ArgumentParser(add_help=False)
_ = multi_import_file_parser.add_argument(
    "-f",
    "--import_filepaths",
    help="Filepaths to be processed by the script.",
    nargs="*",
)
_ = multi_import_file_parser.add_argument(
    "-d",
    "--dir",
    help=("Name of a directory in the ./data/import directory to process all csv files from."),
)

import_file_parser = argparse.ArgumentParser(add_help=False)
_ = import_file_parser.add_argument("-f", "--import_filepaths", help="Filepath to be processed by the script.")


def get_args(*, multi: bool = False) -> argparse.Namespace:
    """Returns command-line arguments, used to process either batch or singular files, based on `multi`.

    Args:
        multi (bool, optional): Set to True if the script is meant to process multiple files via either the command-line
        args or via the -b ("Batch") argument. Defaults to False.

    Returns:
        argparse.Namespace: `args.import_filepath` for a singular filepath, or `args.import_filepaths` for a list of
        multiple raw filepaths.
    """
    if multi:
        parser = argparse.ArgumentParser(parents=[multi_import_file_parser])
    else:
        parser = argparse.ArgumentParser(parents=[import_file_parser])
    return parser.parse_args()
