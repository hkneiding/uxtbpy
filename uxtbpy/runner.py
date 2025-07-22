import os
import shutil
import subprocess
from abc import ABC, abstractmethod

from .tools import change_directory
from .subprocess_error import SubprocessError


class Runner(ABC):
    """Abstract adapter class for interfacing binaries."""

    def __init__(self, working_directory: str = "./.temp/"):
        """Constructor.

        Arguments:
            working_directory (str): The path to the directory from which the interfaced binary will be launched.
        """

        self.check()

        self._working_directory = working_directory
        if not os.path.isdir(self._working_directory):
            os.makedirs(self._working_directory, exist_ok=True)

    @staticmethod
    def check_binary(binary_name: str):
        """Checks if a given binary is available on the system.

        Arguments:
            binary_name (str): The binary.

        Raises:
            RunTimeError: If the binary is not available.
        """

        if shutil.which(binary_name) is None:
            raise RuntimeError("No valid version of " + binary_name + " found.")

    @staticmethod
    def run_binary(binary_name: str, parameters: list, working_directory: str):
        """Excutes a given binary with a given list of parameters in a given working directory.

        Arguments:
            binary_name (str): The binary.
            parameters (list[str]): The list of parameters to append to the binary call.
            working_directory (str): The path to the directory from which the interfaced binary will be launched.

        Returns:
            CompletedProcess: The CompletedProcess object.

        Raises:
            SubprocessError: If the execution of the binary failed.
        """

        with change_directory(working_directory):

            result = subprocess.run(
                [binary_name + " " + " ".join(parameters)],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                shell=True,
            )

            if result.returncode != 0:
                raise SubprocessError(
                    f"{binary_name} failed with standard error: {result.returncode}.",
                    result,
                )

        return result

    @abstractmethod
    def check(self):
        """Checks if required binaries are available on the system.

        Raises:
            RunTimeError: If the required binaries are not available.
        """

        pass

    @abstractmethod
    def run(self, *args, **kwargs):
        """Executes the binary pipeline.

        Raises:
            SubprocessError: If the execution of the binaries failed.
        """

        pass
