import os
import datetime
import subprocess

from .file_handler import FileHandler
from .xtb_output_parser import XtbOutputParser

class XtbRunner:

    """Adapter class for running xtb jobs"""

    def __init__(self, xtb_directory: str = './.temp/', output_format: str = 'raw'):
        
        """Constructor

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
            os.mkdir(self._xtb_directory)

        # validate output format
        supported_output_formats = ['raw', 'dict']
        if output_format not in supported_output_formats:
            print('Warning: Output format "' + output_format + '" not recognised. Defaulting to "raw".')
            self._output_format = 'raw'
        else:
            self._output_format = output_format

    def run_xtb(self, file_name: str, parameters: list = []):

        """Executes xtb with the given file and parameters

        Arguments:
            file_name (str): The name of the molecule file in the xtb directory.
            parameters (list[str]): The parameters to append to the xtb call.

        Returns:
            str: The xtb output.
        """
        
        # change to xtb directory
        os.chdir(self._xtb_directory)
        
        # run xtb
        result = subprocess.run(['xtb', file_name, *parameters], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # check if xtb calculation failed
        if result.returncode != 0:
            
            # log xtb output
            log_file_path = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S') + '.log'
            FileHandler.write_file(log_file_path, result.stdout.decode('utf-8'))
            # exit
            raise RuntimeError('xTB calculation failed with message: "' + result.stderr.decode('utf-8').rstrip() + '".\n' +
                               'Writing output to "' + log_file_path + '".')
        
        # change to root directory
        os.chdir(self._root_directory)

        # return output
        if self._output_format == 'raw':
            return result.stdout.decode('utf-8')
        elif self._output_format == 'dict':
            return XtbOutputParser().parse(result.stdout.decode('utf-8'))

    def run_xtb_from_molecule_data(self, molecule_data: str, file_extension: str, parameters: list = []):

        """Executes xtb with the given molecule data and parameters

        Arguments:
            molecule_data (str): The contents of the molecule file.
            file_extension (str): The file extension corresponding to the formatting of the molecule file.
            parameters (list[str]): The parameters to append to the xtb call.

        Returns:
            str: The xtb output.
        """

        file_path = self._xtb_directory + 'mol.' + file_extension
        FileHandler.write_file(file_path, molecule_data)

        return self.run_xtb('mol.' + file_extension, parameters=parameters)

    def run_xtb_from_xyz(self, xyz: str, parameters: list = []):

        """Executes xtb with the given xyz data and parameters

        Arguments:
            xyz (str): The xyz formatted data of the molecule.
            parameters (list[str]): The parameters to append to the xtb call.

        Returns:
            str: The xtb output.
        """

        return self.run_xtb_from_molecule_data(xyz, 'xyz', parameters=parameters)
