import unittest
from parameterized import parameterized

from uxtbpy.xtb_runner import XtbRunner
from uxtbpy.subprocess_error import SubprocessError


SEROTONIN_INPUT_FILE = "./tests/files/serotonin.xyz"


class TestXtbRunner(unittest.TestCase):

    @parameterized.expand(
        [
            ["invalid_output_format"],
        ]
    )
    def test_constructor_with_invalid_output_format(self, output_format):

        with self.assertWarns(Warning):
            xtb_runner = XtbRunner(output_format=output_format)
            self.assertEqual(xtb_runner._output_format, "raw")

    @parameterized.expand(
        [
            [SEROTONIN_INPUT_FILE, "raw", str],
            [SEROTONIN_INPUT_FILE, "dict", dict],
        ]
    )
    def test_run_from_file(self, file_path, output_format, expected_output_format):

        xtb_runner = XtbRunner(output_format=output_format)
        self.assertEqual(
            type(xtb_runner.run_from_file(file_path)), expected_output_format
        )

    @parameterized.expand(
        [
            ["./this/path/does/not/exist", FileNotFoundError],
        ]
    )
    def test_run_from_file_with_missing_file(self, file_path, expected_error):

        xtb_runner = XtbRunner()
        self.assertRaises(expected_error, xtb_runner.run_from_file, file_path)

    @parameterized.expand(
        [
            ["O 0 0 0\nO 0 0 1", SubprocessError],
            ["\n\nO 0 0 0\nO 0 0 1", SubprocessError],
            ["2\n\nO 0 0 0\nO 0 0", SubprocessError],
        ]
    )
    def test_run_from_xyz_with_invalid_input(self, input, expected_error):

        xtb_runner = XtbRunner()
        self.assertRaises(expected_error, xtb_runner.run_from_xyz, input)
