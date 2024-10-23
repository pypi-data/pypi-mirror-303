"""command_line.py: Command line interface for the application."""

from argparse import ArgumentDefaultsHelpFormatter, ArgumentParser
from os import getcwd
from pathlib import Path
from typing import Any

from ..config.constants import Constants
from . import __version__, logger

logger = logger.getChild(__name__)


def command_line_interface() -> dict[str, Any]:
    """
    Takes arguments from the command line and returns them as a dictionary.

    Returns
    -------
    dict[str, Any]
        A dictionary containing the arguments passed to the application.
    """
    argparser = ArgumentParser(
        formatter_class=ArgumentDefaultsHelpFormatter
    )  # Automatically generates help messages

    argparser.add_argument(
        "--log_output_location",
        "-l",
        action="store",
        type=str,
        required=False,
        default=Constants.DEFAULT_LOG_SAVE_PATH,
        help="Path to save the log file, should end in .txt.",
    )  # Path to save the log file

    argparser.add_argument(
        "--verbose",
        "-v",
        action="store_true",
        required=False,
        help="Increase logging verbosity.",
    )  # Increase logging verbosity

    argparser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
    )  # Display the version number

    argparser.add_argument(
        "--config_file",
        "-c",
        action="store",
        type=str,
        required=False,
        default=getcwd() / Constants.DEFAULT_CONFIG_FILE,
        help="Path to the YAML configuration file.",
    )  # Path to the configuration file

    argparser.add_argument(
        "--input_directory",
        "-i",
        action="store",
        type=str,
        required=False,
        default=getcwd() / Constants.DEFAULT_INPUT_DIRECTORY,
        help="Path to the directory containing the input files.",
    )  # Path to the input directory

    argparser.add_argument(
        "--output_file",
        "-o",
        action="store",
        type=str,
        required=False,
        default=getcwd() / Constants.DEFAULT_OUTPUT_FILE,
        help="Path to save the output file, should end in .md.",
    )  # Path to the output file

    parsed_args = argparser.parse_args()

    # Create a dictionary to return the parsed arguments
    arguments: dict[str, Any] = {
        "log_output_location": Path(parsed_args.log_output_location),
        "verbose": parsed_args.verbose,
        "config_file": Path(parsed_args.config_file),
        "input_directory": Path(parsed_args.input_directory),
        "output_file": Path(parsed_args.output_file),
    }

    logger.debug(f"Arguments: {arguments}")

    return arguments
