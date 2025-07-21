import os
from abc import ABC, abstractmethod

from .logger import Logger


class Runner(ABC):

    """Abstract adapter class for interfacing binaries."""

    def __init__(self, working_directory: str = './.temp/'):
        
        """Constructor.

            Arguments:
                working_directory (str): The path to the directory from which the interfaced binary will be launched.
        """

        self._check_available()

        self._root_directory = os.getcwd()
        self._working_directory = working_directory
        if not os.path.isdir(self._working_directory):
            os.makedirs(self._working_directory, exist_ok=True)

        self._logger = Logger(os.path.join(self._root_directory, 'logs'))

    @abstractmethod
    def _check_available(self):

        """Checks if binary is available on the system.

        """

        pass

    @abstractmethod
    def run(self, parameters: list = []):

        """Executes the binary with the given parameters.

        Arguments:
            parameters (list[str]): The parameters to append to the binary call.

        Returns:
            str: The output.
        """

        pass
