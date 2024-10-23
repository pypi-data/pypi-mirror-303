"""paths.py: Contains paths for the application."""

import shutil
import tempfile
from importlib import resources
from pathlib import Path


class Paths:
    """
    Paths for the application.

    Notes
    -----
    This class contains paths used throughout the application.
    By storing paths in a single location, it is easier to
    manage and update them. Paths should be defined as class
    attributes and should be named in uppercase with underscores
    separating words. Paths should use type hints to indicate
    to the user what type of data they should store.
    """

    temp_dir = Path(tempfile.mkdtemp())

    @classmethod
    def temporary_clone(cls, directory_to_clone: str) -> None:
        """
        Create a temporary clone of a directory.

        Parameters
        ----------
        directory_to_clone : str
            The directory to clone.
        """
        # Get the package to clone
        package_to_clone = resources.files(directory_to_clone)

        # Remove the temporary directory if it exists
        shutil.rmtree(cls.temp_dir)

        # Create the temporary directory
        cls.temp_dir.mkdir(parents=True, exist_ok=True)

        # Copy the files from the package to the temporary directory
        for file in package_to_clone.iterdir():
            if file.is_file():
                shutil.copy(str(file), str(cls.temp_dir))

    TEMPLATES_PATH = temp_dir


def cleanup_temporary_files() -> None:
    """Cleanup temporary files."""
    shutil.rmtree(Paths.temp_dir)


Paths.temporary_clone("logbookgenerator.templates")
