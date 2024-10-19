"""comment_extraction.py: Contains the functions for extracting comments from the code files."""

from ..config.constants import Constants
from . import logger

logger = logger.getChild(__name__)


def extract_comment_id(comment_line: str) -> str:
    """
    Extract the comment identifier from the comment line.

    Parameters
    ----------
    comment_line : str
        The comment line.

    Returns
    -------
    str
        The comment identifier.
    """
    comment_id = comment_line.strip(f"{Constants.ANSWER_KEYWORD}{Constants.ANSWER_ID_DELIMITERS}: ")
    logger.debug(f"Extracted comment ID: {comment_id}")
    return comment_id.replace(" ", "_").replace(".", "_")


def extract_comment_code(comment_lines: list[str], line_number: int) -> tuple[str, int]:
    """
    Extract the comment and code from the comment lines.

    Parameters
    ----------
    comment_lines : list[str]
        The comment lines.
    line_number : int
        The line number of the comment start.

    Returns
    -------
    str
        The comment content.
    int
        The line number of the last line of the comment.
    """
    comment_code = ""

    while line_number < len(comment_lines):
        comment_line = comment_lines[line_number].strip()
        logger.debug(f"Extracting comment code line: {comment_line}")
        if comment_line.startswith(Constants.CODE_COMMENT_DELIMITER):
            break

        comment_code += f"{comment_line}\n"
        logger.debug(f"Comment code: {comment_code}")
        line_number += 1

    return comment_code, line_number


def extract_comment_content(comment_lines: list[str]) -> str:
    """
    Extract the comment content from the comment lines.

    Parameters
    ----------
    comment_lines : list[str]
        The comment lines.

    Returns
    -------
    str
        The comment content.
    """
    comment_content = ""
    line_number = 1

    while line_number < len(comment_lines):
        comment_line = comment_lines[line_number].strip(f"{Constants.BLOCK_COMMENT_MIDDLE}")
        logger.debug(f"Extracting comment line: {comment_line}")
        if comment_line.startswith(Constants.CODE_COMMENT_DELIMITER):
            logger.debug("Extracting comment code")
            code_content, line_number = extract_comment_code(comment_lines, line_number)
            comment_content += f"{code_content}\n\n"

        comment_content += f"{comment_line} "
        logger.debug(f"Comment content: {comment_content}")

    return comment_content.strip()


def extract_block_comment(code_lines: list[str], line_number: int) -> tuple[list[str], int]:
    """
    Extract a block comment from the code lines.

    Parameters
    ----------
    code_lines : list[str]
        The code lines.
    line_number : int
        The line number of the block comment start.

    Returns
    -------
    list[str]
        The block comment lines.
    int
        The line number of the last line of the block comment.
    """
    block_comment_lines: list[str] = []

    while line_number < len(code_lines):
        line = code_lines[line_number].strip()
        logger.debug(f"Extracting block comment line: {line}")

        if line == Constants.COMMENT_END:
            break

        block_comment_lines.append(line.lstrip(Constants.BLOCK_COMMENT_MIDDLE))
        logger.debug(f"Block comment lines: {block_comment_lines}")
        line_number += 1

    return block_comment_lines, line_number
