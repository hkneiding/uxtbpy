import os
import warnings
import datetime
from subprocess import CompletedProcess

from .file_handler import FileHandler


class Logger:
    """Class for handling all logging."""

    def __init__(self, log_directory):
        """Constructor.

        Arguments:
            log_directory (str): The path to the directory in which logs will be stored.

        """

        self._log_directoy = log_directory

    def log_failed_subprocess(self, subprocess_result: CompletedProcess):
        """Logs a failed subprocess.

        Arguments:
            subprocess_result (CompletedProcess): The returned subprocess result object.

        Raises:
            RuntimeError: _description_
        """

        if not os.path.isdir(self._log_directoy):
            os.mkdir(self._log_directoy)

        log_file_path = os.path.join(
            self._log_directoy,
            datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + ".log",
        )
        warnings.warn(
            'xTB calculation failed with standard error: "'
            + subprocess_result.stderr.decode("utf-8").rstrip()
            + '".\n'
            + 'Writing output to "'
            + log_file_path
            + '".'
        )
        FileHandler.write_file(log_file_path, subprocess_result.stdout.decode("utf-8"))
