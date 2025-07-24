import os

from .runner import Runner
from .file_handler import FileHandler
from .subprocess_error import SubprocessError
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
        """Executes the stda pipeline with the given parameters and returns the parsed output.

        Arguments:
            xtb4stda_parameters (list[str]): The parameters to append to the xtb4stda call.
            stda_parameters (list[str]): The parameters to append to the stda call.

        Returns:
            dict: The parsed stda output.

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

        if result.stderr.decode("utf-8") != "":
            raise SubprocessError(
                f"xtb4stda failed with standard error: {result.returncode}.",
                result,
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
        """Executes the stda pipeline with the given file and parameters and returns the parsed output.

        Arguments:
            file_path (str): The (relative/absolute) path to the molecule file.
            xtb4stda_parameters (list[str]): The parameters to append to the xtb4stda call.
            stda_parameters (list[str]): The parameters to append to the stda call.

        Returns:
            dict: The parsed stda output.

        Raises:
            FileNotFoundError: If the specified file does not exist.
        """

        if os.path.exists(file_path):
            file_path = os.path.abspath(file_path)
        else:
            raise FileNotFoundError("The specified file does not exist.")

        return self.run([file_path] + xtb4stda_parameters, stda_parameters)

    def run_from_molecule_data(
        self,
        molecule_data: str,
        file_extension: str,
        xtb4stda_parameters: list = [],
        stda_parameters: list = [],
    ):
        """Executes the stda pipeline with the given molecule data and parameters and returns the parsed output.

        Arguments:
            molecule_data (str): The contents of the molecule file.
            file_extension (str): The file extension corresponding to the formatting of the molecule file.
            xtb4stda_parameters (list[str]): The parameters to append to the xtb4stda call.
            stda_parameters (list[str]): The parameters to append to the stda call.

        Returns:
            dict: The parsed stda output.

        Raises:
            SubprocessError: If stda job failed.
        """

        file_path = os.path.join(self._working_directory, "mol." + file_extension)
        FileHandler.write_file(file_path, molecule_data)

        return self.run_from_file(
            file_path,
            xtb4stda_parameters=xtb4stda_parameters,
            stda_parameters=stda_parameters,
        )

    def run_from_xyz(
        self, xyz: str, xtb4stda_parameters: list = [], stda_parameters: list = []
    ):
        """Executes the stda pipeline with the given xyz data and parameters and returns the parsed output.

        Arguments:
            xyz (str): The xyz formatted data of the molecule.
            xtb4stda_parameters (list[str]): The parameters to append to the xtb4stda call.
            stda_parameters (list[str]): The parameters to append to the stda call.

        Returns:
            dict: The parsed stda output.

        Raises:
            SubprocessError: If stda job failed.
        """

        return self.run_from_molecule_data(
            xyz,
            "xyz",
            xtb4stda_parameters=xtb4stda_parameters,
            stda_parameters=stda_parameters,
        )
