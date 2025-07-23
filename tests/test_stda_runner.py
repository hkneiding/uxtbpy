import unittest
from parameterized import parameterized

from . import SEROTONIN_XYZ
from uxtbpy.stda_runner import StdaRunner


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
