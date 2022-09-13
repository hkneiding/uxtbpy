import os
import datetime
import subprocess

from .file_handler import FileHandler
from .xtb_output_parser import XtbOutputParser

class XtbRunner:

    """Adapter class for running xtb jobs"""

    def __init__(self, working_directory: str = './.temp/', output_format: str = 'raw'):
        
        """Constructor

            Arguments:
                working_directory (str): The path to the directory in which temporary files will be created 
                 from the xtb calculations.
                output_format (str): The format to output the result of xtb calculations.
        """

        # set up working directory if it does not exist already
        self._working_directory = working_directory
        if not os.path.isdir(self._working_directory):
            os.mkdir(self._working_directory)
        # change to working directory
        os.chdir(os.getcwd() + '/' + self._working_directory)

        # validate output format
        supported_output_formats = ['raw', 'dict']
        if output_format not in supported_output_formats:
            print('Warning: Output format "' + output_format + '" not recognised. Defaulting to "raw".')
            self._output_format = 'raw'
        else:
            self._output_format = output_format

    def run_xtb(self, file_path: str, parameters: str = ''):

        """Executes xtb with the given file and parameters

        Arguments:
            file_path (str): The path to the molecule file.
            parameters (list[str]): The parameters to append to the xtb call.

        Returns:
            str: The xtb output.
        """

        # run xtb
        result = subprocess.run(['xtb', file_path, *parameters], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        # check if xtb calculation failed
        if result.returncode != 0:
            print('xTB calculation failed with message: "' + result.stderr.decode('utf-8').rstrip() + '".')

            log_file_path = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S') + '.log'
            print('Writing output to "' + log_file_path + '".')
            FileHandler.write_file(log_file_path, result.stdout.decode('utf-8'))
            return

        # return output
        if self._output_format == 'raw':
            return result.stdout.decode('utf-8')
        elif self._output_format == 'dict':
            return XtbOutputParser(result.stdout.decode('utf-8')).parse()

    def run_xtb_from_molecule_data(self, molecule_data: str, file_extension: str, parameters: str = ''):

        """Executes xtb with the given molecule data and parameters

        Arguments:
            molecule_data (str): The contents of the molecule file.
            file_extension (str): The file extension corresponding to the formatting of the molecule file.
            parameters (list[str]): The parameters to append to the xtb call.

        Returns:
            str: The xtb output.
        """

        file_path = 'mol.' + file_extension
        FileHandler.write_file(file_path, molecule_data)

        return self.run_xtb(file_path, parameters=parameters)

    def run_xtb_from_xyz(self, xyz: str, parameters: str = ''):

        """Executes xtb with the given xyz data and parameters

        Arguments:
            xyz (str): The xyz formatted data of the molecule.
            parameters (list[str]): The parameters to append to the xtb call.

        Returns:
            str: The xtb output.
        """

        return self.run_xtb_from_molecule_data(xyz, 'xyz', parameters=parameters)
