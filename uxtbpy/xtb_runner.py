import os
import datetime
import subprocess
import warnings

from .tools import change_directory
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

        # remember the directory from which the program was launched from 
        self._root_directory = os.getcwd()

        # set up working directory if it does not exist already
        self._xtb_directory = xtb_directory
        if not os.path.isdir(self._xtb_directory):
            os.makedirs(self._xtb_directory, exist_ok=True)

        # validate output format
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
        if b'xtb: not found' in result.stderr:
            raise RuntimeError('No valid version of xTB found. Please make sure you have xTB installed and it is accessible via "xtb".')

    def run_xtb(self, file_path: str, parameters: list = []):

        """Executes xtb with the given file and parameters.

        Arguments:
            file_path (str): The (relative/absolute) path to the molecule file.
            parameters (list[str]): The parameters to append to the xtb call.

        Returns:
            str: The xtb output.
        """
        
        self._check_xtb_available()

        # get absolute path
        if os.path.exists(file_path):
            file_path = os.path.abspath(file_path)
        else:
            raise FileNotFoundError('The specified file does not exist.')

        # change to xtb directory
        with change_directory(self._xtb_directory):
            
            # run xtb
            result = subprocess.run(['xtb' + ' ' + file_path + ' ' + ' '.join(parameters)], 
                                    stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

            # check if xtb calculation failed
            if result.returncode != 0:
                
                # make logs directory if not found
                if not os.path.isdir('./logs/'):
                    os.mkdir('./logs/')

                # read input file
                with open(file_path, 'r') as fh:
                    input_ = fh.read()

                # build string to log
                log = 'Input:\n\n' + input_ + '\n\nOutput:\n\n' + result.stdout.decode('utf-8')

                # log xtb output
                log_file_path = './logs/' + datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S') + '.log'
                FileHandler.write_file(log_file_path, log)
                # exit
                raise RuntimeError('xTB calculation failed with message: "' + result.stderr.decode('utf-8').rstrip() + '".\n' +
                                'Writing output to "' + log_file_path + '".', result.stdout.decode('utf-8'))
        
        # return output
        if self._output_format == 'raw':
            return result.stdout.decode('utf-8')
        elif self._output_format == 'dict':
            return XtbOutputParser().parse(result.stdout.decode('utf-8'))

    def run_xtb_from_molecule_data(self, molecule_data: str, file_extension: str, parameters: list = []):

        """Executes xtb with the given molecule data and parameters.

        Arguments:
            molecule_data (str): The contents of the molecule file.
            file_extension (str): The file extension corresponding to the formatting of the molecule file.
            parameters (list[str]): The parameters to append to the xtb call.

        Returns:
            str: The xtb output.
        """

        file_path = self._xtb_directory + 'mol.' + file_extension
        FileHandler.write_file(file_path, molecule_data)

        return self.run_xtb(file_path, parameters=parameters)

    def run_xtb_from_xyz(self, xyz: str, parameters: list = []):

        """Executes xtb with the given xyz data and parameters.

        Arguments:
            xyz (str): The xyz formatted data of the molecule.
            parameters (list[str]): The parameters to append to the xtb call.

        Returns:
            str: The xtb output.
        """

        return self.run_xtb_from_molecule_data(xyz, 'xyz', parameters=parameters)
