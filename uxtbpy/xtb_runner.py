import os
import subprocess
import warnings

from .tools import change_directory
from .logger import Logger
from .file_handler import FileHandler
from .xtb_output_parser import XtbOutputParser


class XtbRunner:

    """Adapter class for running xtb jobs."""

    def __init__(self, xtb_directory: str = './.temp/', output_format: str = 'raw'):
        
        """Constructor.

            Arguments:
                xtb_directory (str): The path to the directory in which temporary files will be created 
                 from the xtb calculations.
                output_format (str): The format to output the result of xtb calculations.
        """

        self._check_xtb_available()

        self._root_directory = os.getcwd()

        self._xtb_directory = xtb_directory
        if not os.path.isdir(self._xtb_directory):
            os.makedirs(self._xtb_directory, exist_ok=True)

        self._logger = Logger(os.path.join(self._root_directory, 'logs'))

        supported_output_formats = ['raw', 'dict']
        if output_format not in supported_output_formats:
            warnings.warn('Warning: Output format "' + output_format + '" not recognised. Defaulting to "raw".')
            self._output_format = 'raw'
        else:
            self._output_format = output_format

    def _check_xtb_available(self):

        """Checks if xtb is available on the system.

        Raises:
            RuntimeError: If xtb cannot be accessed.
        """

        result = subprocess.run(['xtb -version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        if b'normal termination of xtb' not in result.stderr:
            raise RuntimeError('No valid version of xTB found. Please make sure you have xTB installed and it is accessible via "xtb".')

    def run_xtb(self, parameters: list = []):

        """Executes xtb with the given parameters.

        Arguments:
            parameters (list[str]): The parameters to append to the xtb call.

        Returns:
            str: The xtb output.

        Raises:
            RuntimeError: If xtb job failed.
        """

        with change_directory(self._xtb_directory):
            
            result = subprocess.run(['xtb' + ' ' + ' '.join(parameters)], 
                                    stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

            if result.returncode != 0:
                self._logger.log_failed_subprocess(result)
                raise RuntimeError()

            with open('xtb.stdout', 'w') as fh:
                fh.write(result.stdout.decode('utf-8'))
            with open('xtb.stderr', 'w') as fh:
                fh.write(result.stderr.decode('utf-8'))

        if self._output_format == 'raw':
            return result.stdout.decode('utf-8')
        elif self._output_format == 'dict':
            return XtbOutputParser().parse(result.stdout.decode('utf-8'))

    def run_xtb_from_file(self, file_path: str, parameters: list = []):

        """Executes xtb with the given file and parameters.

        Arguments:
            file_path (str): The (relative/absolute) path to the molecule file.
            parameters (list[str]): The parameters to append to the xtb call.

        Returns:
            str: The xtb output.
        
        Raises:
            FileNotFoundError: If the specified file does not exist.
        """
        
        if os.path.exists(file_path):
            file_path = os.path.abspath(file_path)
        else:
            raise FileNotFoundError('The specified file does not exist.')

        return self.run_xtb([file_path] + parameters)

    def run_xtb_from_molecule_data(self, molecule_data: str, file_extension: str, parameters: list = []):

        """Executes xtb with the given molecule data and parameters.

        Arguments:
            molecule_data (str): The contents of the molecule file.
            file_extension (str): The file extension corresponding to the formatting of the molecule file.
            parameters (list[str]): The parameters to append to the xtb call.

        Returns:
            str: The xtb output.
        """

        file_path = os.path.join(self._xtb_directory, 'mol.' + file_extension)
        FileHandler.write_file(file_path, molecule_data)

        return self.run_xtb_from_file(file_path, parameters=parameters)

    def run_xtb_from_xyz(self, xyz: str, parameters: list = []):

        """Executes xtb with the given xyz data and parameters.

        Arguments:
            xyz (str): The xyz formatted data of the molecule.
            parameters (list[str]): The parameters to append to the xtb call.

        Returns:
            str: The xtb output.
        """

        return self.run_xtb_from_molecule_data(xyz, 'xyz', parameters=parameters)
