"""context_generation.py: Contains the functions for generating the context for the logbook."""

from datetime import datetime, timedelta
from typing import Any

from ..config.constants import Constants
from . import logger
from .code_processing import process_code_comments

logger = logger.getChild(__name__)


def generate_tasks_context(cpp_files: dict[str, str]) -> dict[str, Any]:
    """
    Generate the tasks context.

    Parameters
    ----------
    cpp_files : dict[str, str]
        The CPP files.

    Returns
    -------
    dict[str, Any]
        The tasks context.
    """
    tasks_context: dict[str, Any] = {
        "lab": {},
        "extra": {},
    }

    # Iterate through the CPP files
    for file_name, file_content in cpp_files.items():
        # Extract information from the file name
        logger.debug(f"Processing file: {file_name}")
        task_codeword, task_topic, task_name = file_name.split("-", maxsplit=2)

        # Clean up the extracted information
        task_type = "lab" if task_codeword.startswith("l") else "extra"
        task_number = task_codeword[1:]
        task_topic = task_topic.replace("_", " ").title()
        task_name = task_name.replace("_", " ").title()
        logger.debug(
            f"Task type: {task_type}, number: {task_number}, topic: {task_topic}, name: {task_name}"
        )

        # Process the file content
        code_lines = file_content.splitlines()
        task_code_explanations = process_code_comments(code_lines)

        tasks_context[task_type][task_number] = {
            "topic": task_topic,
            "name": task_name,
            "code": task_code_explanations,
        }
        logger.debug(f"Task context: {tasks_context[task_type][task_number]}")

    # Sort the tasks by their number
    for task_type in tasks_context:
        tasks_context[task_type] = dict(sorted(tasks_context[task_type].items()))

    logger.debug(f"Tasks context: {tasks_context}")
    return tasks_context


def generate_week_context(
    week_number: int,
    week_start_date: datetime,
    week_end_date: datetime,
    weekly_file: dict[str, dict[str, str] | str],
) -> dict[str, Any]:
    """
    Generate the week context.

    Parameters
    ----------
    week_number : int
        The week number.
    week_start_date : datetime
        The start date of the week.
    week_end_date : datetime
        The end date of the week.
    weekly_file : dict[str, dict[str, str] | str]
        The weekly file, containing the CPP files and reflections.

    Returns
    -------
    dict[str, Any]
        The week context.
    """
    week_context: dict[str, Any] = {
        "number": week_number,
        "start_date": week_start_date.strftime(Constants.DATE_DATETIME_FORMAT),
        "end_date": week_end_date.strftime(Constants.DATE_DATETIME_FORMAT),
        "reflection": weekly_file["reflection"],
        "tasks": generate_tasks_context(weekly_file["cpp"]),  # type: ignore
    }

    logger.debug(f"Week {week_number} context: {week_context}")
    return week_context


def generate_weeks_context(
    weekly_files: list[dict[str, dict[str, str] | str]], start_date: datetime
) -> dict[str, Any]:
    """
    Generate the weeks context.

    Parameters
    ----------
    weekly_files: list[dict[str, dict[str, str] | str]]
        The weekly files, containing the CPP files and reflections.
    start_date : datetime
        The start date of the university.

    Returns
    -------
    dict[str, Any]
        The weeks context.
    """
    weeks_context: dict[str, Any] = {"weeks": {}}
    numbered_weekly_files = enumerate(weekly_files, start=1)
    logger.debug(f"Numbered weekly files: {numbered_weekly_files}")

    for week_number, weekly_file in numbered_weekly_files:
        week_start_date = start_date + timedelta(weeks=week_number - 1)
        week_end_date = week_start_date + timedelta(weeks=1)

        week_context = generate_week_context(
            week_number,
            week_start_date,
            week_end_date,
            weekly_file,
        )

        weeks_context["weeks"][str(week_number)] = week_context

    return weeks_context


def generate_logbook_contexts(
    config: dict[str, Any],
    weekly_files: list[dict[str, dict[str, str] | str]],
    references: list[dict[str, str]],
) -> dict[str, Any]:
    """
    Generate the contexts for the logbook.

    Parameters
    ----------
    config : dict[str, Any]
        The configuration file.
    weekly_files: list[dict[str, dict[str, str] | str]]
        The weekly files, containing the CPP files and reflections.
    references : list[dict[str, str]]
        The references.

    Returns
    -------
    dict[str, Any]
        The logbook contexts.
    """
    logbook_contexts: dict[str, Any] = {}

    logbook_contexts["cover"] = config
    logger.debug(f"Cover context: {logbook_contexts["cover"]}")

    start_date = datetime.strptime(
        config["university"]["start"],
        Constants.DATE_DATETIME_FORMAT,
    )
    logger.debug(f"Start date: {start_date}")
    logbook_contexts["weeks"] = generate_weeks_context(weekly_files, start_date)
    logger.debug(f"Weeks context: {logbook_contexts["weeks"]}")

    logbook_contexts["references"] = references
    logger.debug(f"References context: {logbook_contexts["references"]}")

    return logbook_contexts
