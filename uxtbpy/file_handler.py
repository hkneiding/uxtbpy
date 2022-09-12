class FileHandler:

    """Class for handling all IO/file handling tasks."""

    @staticmethod
    def read_file(file_path):
        """Reads a specified file.

        Args:
            file_path (string): The path to the input file.

        Raises:
            FileNotFoundError: If file not found.
            IsADirectoryError: If path points to a directory.

        Returns:
            string: The file content.
        """

        try:
            f = open(file_path, 'r')
        except FileNotFoundError:
            raise FileNotFoundError('The specified file does not exist.')
        except IsADirectoryError:
            raise IsADirectoryError('Cannot open directory.')

        with f:
            data = f.read()
            f.close()

            return data

    @staticmethod
    def write_file(file_path, data):
        """Writes the specified content into a file (overwrites).

        Args:
            file_path (string): The path to the output file.
            data (string): The file content to write.
        """

        f = open(file_path, 'w')
        f.write(data)
        f.close()
