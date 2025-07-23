import unittest
from parameterized import parameterized

from . import SEROTONIN_STDA_STDOUT
from uxtbpy.file_handler import FileHandler
from uxtbpy.stda_output_parser import StdaOutputParser


class TestStdaOutputParser(unittest.TestCase):

    @parameterized.expand(
        [
            [
                SEROTONIN_STDA_STDOUT,
                [
                    [89.47625, 19.48166, 1.56491],
                    [19.48166, 41.53345, 1.49083],
                    [1.56491, 1.49083, 1.30622],
                ],
            ]
        ]
    )
    def test_extract_polarizability_tensor(self, output_file, expected):

        output_data = FileHandler.read_file(output_file)
        result = StdaOutputParser().parse(output_data)
        self.assertEqual(result["polarizability_tensor"], expected)

    @parameterized.expand(
        [
            [
                SEROTONIN_STDA_STDOUT,
                (
                    [632.8, 589.3, 579.0, 546.0, 436.0, 365.0],
                    [-232.96, -272.39, -283.26, -323.09, -551.72, -917.71],
                ),
            ]
        ]
    )
    def test_extract_specific_optical_rotations(self, output_file, expected):

        output_data = FileHandler.read_file(output_file)
        result = StdaOutputParser().parse(output_data)
        self.assertEqual(result["specific_optical_rotation_wavelengths"], expected[0])
        self.assertEqual(result["specific_optical_rotation_angles"], expected[1])

    @parameterized.expand(
        [
            [
                SEROTONIN_STDA_STDOUT,
                (
                    [
                        295.8,
                        276.3,
                        243.4,
                        234.7,
                        217.2,
                        213.5,
                        208.1,
                        203.8,
                        201.3,
                        195.4,
                        191.7,
                        187,
                        186.3,
                        183,
                        181.9,
                        179.6,
                        178.7,
                    ],
                    [
                        0.1227,
                        0.075,
                        0.0068,
                        0.0286,
                        0.0121,
                        0.0209,
                        0.4527,
                        0.0057,
                        0.0119,
                        0.0105,
                        0.0229,
                        0.3176,
                        0.0332,
                        0.097,
                        0.6049,
                        0.3039,
                        0.148,
                    ],
                ),
            ]
        ]
    )
    def test_extract_excitations(self, output_file, expected):

        output_data = FileHandler.read_file(output_file)
        result = StdaOutputParser().parse(output_data)
        self.assertEqual(result["excitation_wavelenghts"], expected[0])
        self.assertEqual(result["excitation_oscillator_strengths"], expected[1])
