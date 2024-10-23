"""constants.py: Constants for the application."""

from pathlib import Path
from typing import Literal


class Constants:
    """
    Constants for the application.

    Notes
    -----
    This class contains constants used throughout the application.
    By storing constants in a single location, it is easier to
    manage and update them. Constants should be defined as class
    attributes and should be named in uppercase with underscores
    separating words. Constants should use type hints to indicate
    to the user what type of data they should store.
    """

    # Logging constants
    POSSIBLE_LOGGING_LEVELS = Literal["CRITICAL", "ERROR", "WARNING", "INFO", "DEBUG"]
    LOGGING_LEVEL_LOGFILE_DEFAULT: POSSIBLE_LOGGING_LEVELS = "DEBUG"
    LOGGING_LEVEL_CONSOLE_DEFAULT: POSSIBLE_LOGGING_LEVELS = "INFO"
    LOGGING_LOGFILE_FORMAT: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    LOGGING_CONSOLE_FORMAT: str = "%(message)s"
    LOGGING_TIMESTAMP_FORMAT: str = "%Y-%m-%d_%H-%M-%S"
    LOGGING_DATE_FORMAT: str = "[%X]"
    LOGGING_TRACEBACKS: bool = True

    # API response constants
    SUCCESS_CODE: int = 200
    SUCCESS_TEXT: str = "OK"
    FORBIDDEN_CODE: int = 403

    # Default values
    DEFAULT_LOG_SAVE_PATH: Path = Path("logbookgenerator_log.txt")

    # Type hints
    TASK_ANNOTATION = dict[str, str | dict[str, list[tuple[str, str]]]]
    WEEK_ANNOTATION = dict[str, str | dict[Literal["lab", "extra"], dict[str, TASK_ANNOTATION]]]

    # Format patterns
    YEAR_REGEX_FORMAT: str = r"^\d{4}$"
    ID_REGEX_FORMAT: str = r"^\d{8}$"
    DATE_REGEX_FORMAT: str = r"^\d{4}-\d{2}-\d{2}$"
    DATE_DATETIME_FORMAT: str = "%Y-%m-%d"

    # Config file constants
    DEFAULT_MODULE_CODE: str = "MTH2008"
    DEFAULT_MODULE_NAME: str = "Scientific Computing"
    DEFAULT_STATEMENT_TEXT: str = (
        "I confirm that this logbook is entirely my own work and that all references and "
        "quotations, from both primary and secondary sources, have been fully identified "
        "and properly acknowledged."
    )
    DEFAULT_UNIVERSITY_DEPARTMENT: str = "School of Engineering and Physical Sciences"
    DEFAULT_UNIVERSITY_NAME: str = "University of Lincoln"
    SEMESTER_CHOICES: list[str] = ["Semester A", "Semester B"]

    # Formatting
    JINJA_DATE_FORMAT: str = "%Y-%m-%d"
    ANSWER_KEYWORD: str = "ANSWER"
    INLINE_COMMENT_START: str = "/*"
    BLOCK_COMMENT_START: str = "/**"
    BLOCK_COMMENT_MIDDLE: str = "*"
    COMMENT_END: str = "*/"
    ANSWER_ID_DELIMITERS: str = "()"
    INLINE_ANSWER_COMMENT: str = f"{ANSWER_KEYWORD} {r'\(Task (\d+).(\d+)\): (.+)'}"
    CODE_COMMENT_DELIMITER: str = "```"
