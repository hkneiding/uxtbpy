import os

from .runner import Runner
from .stda_output_parser import StdaOutputParser


class StdaRunner(Runner):
    """Adapter class for running stda jobs."""

    def __init__(self, working_directory: str = "./.temp/"):
        """Constructor.

        Arguments:
            stda_directory (str): The path to the directory in which temporary files will be created
             from the stda calculations.
        """

        super().__init__(working_directory)

    def check(self):
        """Checks if xtb4stda and stda are available on the system.

        Raises:
            RunTimeError: If xtb4stda or stda is not available.
        """

        Runner.check_binary("xtb4stda")
        Runner.check_binary("stda")

    def run(self, xtb4stda_parameters: list = [], stda_parameters: list = []):
        """Executes the stda pipeline with the given parameters.

        Arguments:

        Returns:
            str: The stda output.

        Raises:
            RuntimeError: If the stda job failed.
        """

        result = Runner.run_binary(
            "xtb4stda",
            xtb4stda_parameters,
            working_directory=self._working_directory,
            write_stdout=True,
            write_stderr=False,
        )

        result = Runner.run_binary(
            "stda",
            ["-xtb"] + stda_parameters,
            working_directory=self._working_directory,
            write_stdout=True,
            write_stderr=False,
        )

        return StdaOutputParser().parse(result.stdout.decode("utf-8"))

    def run_from_file(
        self, file_path: str, xtb4stda_parameters: list = [], stda_parameters: list = []
    ):
        """Executes the stda pipeline with the given file and parameters.

        Arguments:
            file_path (str): The (relative/absolute) path to the molecule file.

        Returns:
            str: The xtb output.

        Raises:
            FileNotFoundError: If the specified file does not exist.
        """

        if os.path.exists(file_path):
            file_path = os.path.abspath(file_path)
        else:
            raise FileNotFoundError("The specified file does not exist.")

        return self.run([file_path] + xtb4stda_parameters, stda_parameters)
