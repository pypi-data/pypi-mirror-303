"""main.py: Called when the package is ran as a script."""

from logging import shutdown as shutdown_logging

from yaml import YAMLError

from .computation.config_generation import build_config_file
from .computation.context_generation import generate_logbook_contexts
from .computation.parsing import parse_input_directory
from .computation.render_context import create_logbook
from .config.constants import Constants
from .config.paths import cleanup_temporary_files
from .interface.command_line import command_line_interface
from .logs.setup_logging import setup_logging
from .utilities.file_handling import load_yaml, save_file
from .utilities.validation import validate_input_directory


def main() -> None:
    """
    Overall control flow of the application.

    Notes
    -----
    This function is the entry point for the application, so only really
    contains overall control flow logic. The actual work is done in the
    other modules, usually.
    """
    # Get the arguments from the command line
    user_arguments = command_line_interface()

    # Setup logging
    setup_logging(
        user_arguments["log_output_location"],
        console_logging_level=(
            "DEBUG" if user_arguments["verbose"] else Constants.LOGGING_LEVEL_CONSOLE_DEFAULT
        ),
    )

    # Validate the structure of the input directory
    validate_input_directory(user_arguments["input_directory"])

    # Load the configuration file
    try:
        config = load_yaml(user_arguments["config_file"])
    except YAMLError:
        config_file = build_config_file()
        config = load_yaml(config_file)

    # Parse through the input directory
    weekly_files, references = parse_input_directory(user_arguments["input_directory"])
    # TODO: Generalise functions to re-use for coursework generation
    # Issue URL: https://github.com/unkokaeru/logbookgenerator/issues/1

    # Create the template contexts
    logbook_contexts = generate_logbook_contexts(config, weekly_files, references)

    # Create the logbook
    logbook_markdown = create_logbook(logbook_contexts)

    # Write the logbook to the output file
    save_file(user_arguments["output_file"], logbook_markdown)

    shutdown_logging()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
        shutdown_logging()
        cleanup_temporary_files()
        raise e
