import unittest
from parameterized import parameterized

from . import SEROTONIN_XYZ
from uxtbpy.stda_runner import StdaRunner
from uxtbpy.subprocess_error import SubprocessError


class TestStdaRunner(unittest.TestCase):

    @parameterized.expand(
        [
            [SEROTONIN_XYZ, dict],
        ]
    )
    def test_run_from_file(self, file_path, expected_output_format):

        stda_runner = StdaRunner()
        self.assertEqual(
            type(stda_runner.run_from_file(file_path)), expected_output_format
        )

    @parameterized.expand(
        [
            ["./this/path/does/not/exist", FileNotFoundError],
        ]
    )
    def test_run_from_file_with_missing_file(self, file_path, expected_error):

        stda_runner = StdaRunner()
        self.assertRaises(expected_error, stda_runner.run_from_file, file_path)

    @parameterized.expand(
        [
            ["O 0 0 0\nO 0 0 1", SubprocessError],
            ["\n\nO 0 0 0\nO 0 0 1", SubprocessError],
            ["2\n\nO 0 0 0\nO 0 0", SubprocessError],
        ]
    )
    def test_run_from_xyz_with_invalid_input(self, input, expected_error):

        stda_runner = StdaRunner()
        self.assertRaises(expected_error, stda_runner.run_from_xyz, input)
