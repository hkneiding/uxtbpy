import os
import datetime
import subprocess

from .file_handler import FileHandler


class XtbRunner:

    """Adapter class for running xtb jobs"""

    def __init__(self, working_directory='./.temp/'):
        
        """Constructor"""

        self.working_directory = working_directory

        # set up working directory if it does not exist already
        if not os.path.isdir(self.working_directory):
            os.mkdir(self.working_directory)

        os.chdir(os.getcwd() + '/' + self.working_directory)

    def run_xtb_full(self, molecule_file_content, file_extension):
        return self.run_xtb(molecule_file_content, file_extension, parameters=['--ohess'])

    def run_xtb(self, molecule_file_content, file_extension, parameters=''):

        # write molecule data to file
        file_path = 'mol.' + file_extension
        FileHandler.write_file(file_path, molecule_file_content)

        # run xtb
        result = subprocess.run(['xtb', file_path, *parameters], stdout=subprocess.PIPE)
        
        # return output
        return result.stdout.decode('utf-8')
