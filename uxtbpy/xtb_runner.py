import os

from .runner import Runner
from .file_handler import FileHandler
from .xtb_output_parser import XtbOutputParser


class XtbRunner(Runner):
    """Adapter class for running xtb jobs."""

    def __init__(self, working_directory: str = "./.temp/"):
        """Constructor.

        Arguments:
            working_directory (str): The path to the directory from which xtb will be launched.
            output_format (str): The format to output the result of xtb calculations.
        """

        super().__init__(working_directory)

    def check(self):
        """Checks if xtb is available on the system.

        Raises:
            RunTimeError: If xtb is not available.
        """

        Runner.check_binary("xtb")

    def run(self, parameters: list = []):
        """Executes xtb with the given parameters and returns the parsed output.

        Arguments:
            parameters (list[str]): The parameters to append to the xtb call.

        Returns:
            dict: The parsed xtb output.

        Raises:
            SubprocessError: If xtb job failed.
        """

        result = Runner.run_binary(
            "xtb",
            parameters,
            working_directory=self._working_directory,
            write_stdout=True,
            write_stderr=False,
        )

        return XtbOutputParser().parse(result.stdout.decode("utf-8"))

    def run_from_file(self, file_path: str, parameters: list = []):
        """Executes xtb with the given file and parameters and returns the parsed output.

        Arguments:
            file_path (str): The (relative/absolute) path to the molecule file.
            parameters (list[str]): The parameters to append to the xtb call.

        Returns:
            dict: The parsed xtb output.

        Raises:
            FileNotFoundError: If the specified file does not exist.
            SubprocessError: If xtb job failed.
        """

        if os.path.exists(file_path):
            file_path = os.path.abspath(file_path)
        else:
            raise FileNotFoundError("The specified file does not exist.")

        return self.run([file_path] + parameters)

    def run_from_molecule_data(
        self, molecule_data: str, file_extension: str, parameters: list = []
    ):
        """Executes xtb with the given molecule data and parameters and returns the parsed output.

        Arguments:
            molecule_data (str): The contents of the molecule file.
            file_extension (str): The file extension corresponding to the formatting of the molecule file.
            parameters (list[str]): The parameters to append to the xtb call.

        Returns:
            dict: The parsed xtb output.

        Raises:
            SubprocessError: If xtb job failed.
        """

        file_path = os.path.join(self._working_directory, "mol." + file_extension)
        FileHandler.write_file(file_path, molecule_data)

        return self.run_from_file(file_path, parameters=parameters)

    def run_from_xyz(self, xyz: str, parameters: list = []):
        """Executes xtb with the given xyz data and parameters and returns the parsed output.

        Arguments:
            xyz (str): The xyz formatted data of the molecule.
            parameters (list[str]): The parameters to append to the xtb call.

        Returns:
            dict: The parsed xtb output.

        Raises:
            SubprocessError: If xtb job failed.
        """

        return self.run_from_molecule_data(xyz, "xyz", parameters=parameters)
