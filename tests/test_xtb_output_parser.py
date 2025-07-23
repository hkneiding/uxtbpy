import unittest
from parameterized import parameterized

from uxtbpy.file_handler import FileHandler
from uxtbpy.xtb_output_parser import XtbOutputParser


SEROTONIN_OUTPUT_FILE = "./tests/files/serotonin.out"


class TestXtbOutputParser(unittest.TestCase):

    @parameterized.expand(
        [
            [SEROTONIN_OUTPUT_FILE, 131.186589],
        ]
    )
    def test_extract_polarizability(self, output_file, expected):

        output_data = FileHandler.read_file(output_file)
        result = XtbOutputParser().parse(output_data)
        self.assertEqual(result["polarizability"], expected)

    @parameterized.expand(
        [
            [SEROTONIN_OUTPUT_FILE, -9.6533],
        ]
    )
    def test_extract_homo_energy(self, output_file, expected):

        output_data = FileHandler.read_file(output_file)
        result = XtbOutputParser().parse(output_data)
        self.assertEqual(result["homo_energy"], expected)

    @parameterized.expand(
        [
            [SEROTONIN_OUTPUT_FILE, -6.1835],
        ]
    )
    def test_extract_lumo_energy(self, output_file, expected):

        output_data = FileHandler.read_file(output_file)
        result = XtbOutputParser().parse(output_data)
        self.assertEqual(result["lumo_energy"], expected)

    @parameterized.expand(
        [
            [
                SEROTONIN_OUTPUT_FILE,
                [
                    6,
                    6,
                    6,
                    6,
                    6,
                    6,
                    8,
                    6,
                    6,
                    7,
                    6,
                    6,
                    7,
                    1,
                    1,
                    1,
                    1,
                    1,
                    1,
                    1,
                    1,
                    1,
                    1,
                    1,
                    1,
                ],
            ],
        ]
    )
    def test_extract_atomic_numbers(self, output_file, expected):

        output_data = FileHandler.read_file(output_file)
        result = XtbOutputParser().parse(output_data)
        self.assertEqual(result["atomic_numbers"], expected)

    @parameterized.expand(
        [
            [
                SEROTONIN_OUTPUT_FILE,
                [
                    [1.48537742545851, 1.27512515137874, -0.03158693279875],
                    [0.16869681352769, 1.67021148325986, 0.01160869779818],
                    [-0.80762796564299, 0.68208930214415, 0.01680432881200],
                    [-0.47390461698037, -0.69228124271162, -0.02336211322538],
                    [0.86922449237798, -1.07101667113193, -0.06371446944804],
                    [1.83356088511015, -0.08432176143027, -0.06695182562317],
                    [3.16994424651572, -0.37791763604269, -0.10484918745623],
                    [-1.70347709686421, -1.41866898046314, -0.00168846903362],
                    [-2.69931793136278, -0.48614183277856, 0.04488307789706],
                    [-2.16993082508332, 0.77501619661316, 0.05766310941823],
                    [-1.86476822922914, -2.90028481402398, -0.06955742234236],
                    [-1.74928665894456, -3.40586514847725, -1.51282187672199],
                    [-2.03648088137563, -4.83059603172774, -1.56098058206502],
                    [2.28429969734342, 1.99887193889496, -0.03726962550319],
                    [-0.09516378646319, 2.71685498959369, 0.04139031468475],
                    [1.14911974673173, -2.11588916133038, -0.08911725322382],
                    [3.28701559998537, -1.33483768071412, -0.11879516435268],
                    [-3.76168565062429, -0.63607563757227, 0.07617190382162],
                    [-2.69642844510252, 1.63026909415453, 0.09850787861704],
                    [-2.84294705135557, -3.18929829481418, 0.31620944543198],
                    [-1.09961935045535, -3.38602217614314, 0.54113299216722],
                    [-0.75262324074595, -3.14367876854845, -1.90716801206746],
                    [-2.49468861913193, -2.89719324766491, -2.13080596625127],
                    [-1.34978460920199, -5.34537644053925, -1.01830733191282],
                    [-1.99485394848676, -5.16988262992533, -2.51587551662237],
                ],
            ],
        ]
    )
    def test_optimized_atomic_positions(self, output_file, expected):

        output_data = FileHandler.read_file(output_file)
        result = XtbOutputParser().parse(output_data)
        self.assertEqual(result["optimized_atomic_positions"], expected)

    @parameterized.expand(
        [
            [
                SEROTONIN_OUTPUT_FILE,
                "25\n\n"
                "C 1.48537742545851 1.27512515137874 -0.03158693279875\n"
                "C 0.16869681352769 1.67021148325986 0.01160869779818\n"
                "C -0.80762796564299 0.68208930214415 0.01680432881200\n"
                "C -0.47390461698037 -0.69228124271162 -0.02336211322538\n"
                "C 0.86922449237798 -1.07101667113193 -0.06371446944804\n"
                "C 1.83356088511015 -0.08432176143027 -0.06695182562317\n"
                "O 3.16994424651572 -0.37791763604269 -0.10484918745623\n"
                "C -1.70347709686421 -1.41866898046314 -0.00168846903362\n"
                "C -2.69931793136278 -0.48614183277856 0.04488307789706\n"
                "N -2.16993082508332 0.77501619661316 0.05766310941823\n"
                "C -1.86476822922914 -2.90028481402398 -0.06955742234236\n"
                "C -1.74928665894456 -3.40586514847725 -1.51282187672199\n"
                "N -2.03648088137563 -4.83059603172774 -1.56098058206502\n"
                "H 2.28429969734342 1.99887193889496 -0.03726962550319\n"
                "H -0.09516378646319 2.71685498959369 0.04139031468475\n"
                "H 1.14911974673173 -2.11588916133038 -0.08911725322382\n"
                "H 3.28701559998537 -1.33483768071412 -0.11879516435268\n"
                "H -3.76168565062429 -0.63607563757227 0.07617190382162\n"
                "H -2.69642844510252 1.63026909415453 0.09850787861704\n"
                "H -2.84294705135557 -3.18929829481418 0.31620944543198\n"
                "H -1.09961935045535 -3.38602217614314 0.54113299216722\n"
                "H -0.75262324074595 -3.14367876854845 -1.90716801206746\n"
                "H -2.49468861913193 -2.89719324766491 -2.13080596625127\n"
                "H -1.34978460920199 -5.34537644053925 -1.01830733191282\n"
                "H -1.99485394848676 -5.16988262992533 -2.51587551662237\n",
            ],
        ]
    )
    def test_optimized_xyz(self, output_file, expected):

        output_data = FileHandler.read_file(output_file)
        result = XtbOutputParser().parse(output_data)

        self.assertEqual(result["optimized_xyz"].strip(), expected.strip())

    @parameterized.expand(
        [
            [SEROTONIN_OUTPUT_FILE, 1.129],
        ]
    )
    def test_extract_dipole_moment(self, output_file, expected):

        output_data = FileHandler.read_file(output_file)
        result = XtbOutputParser().parse(output_data)
        self.assertEqual(result["dipole_moment"], expected)

    @parameterized.expand(
        [
            [SEROTONIN_OUTPUT_FILE, 176.2154593],
        ]
    )
    def test_extract_molecular_mass(self, output_file, expected):

        output_data = FileHandler.read_file(output_file)
        result = XtbOutputParser().parse(output_data)
        self.assertEqual(result["molecular_mass"], expected)

    @parameterized.expand(
        [
            [SEROTONIN_OUTPUT_FILE, 8130.0688],
        ]
    )
    def test_extract_enthalpy(self, output_file, expected):

        output_data = FileHandler.read_file(output_file)
        result = XtbOutputParser().parse(output_data)
        self.assertEqual(result["enthalpy"], expected)

    @parameterized.expand(
        [
            [SEROTONIN_OUTPUT_FILE, 49.0254],
        ]
    )
    def test_extract_heat_capacity(self, output_file, expected):

        output_data = FileHandler.read_file(output_file)
        result = XtbOutputParser().parse(output_data)
        self.assertEqual(result["heat_capacity"], expected)

    @parameterized.expand(
        [
            [SEROTONIN_OUTPUT_FILE, 106.7954],
        ]
    )
    def test_extract_entropy(self, output_file, expected):

        output_data = FileHandler.read_file(output_file)
        result = XtbOutputParser().parse(output_data)
        self.assertEqual(result["entropy"], expected)

    @parameterized.expand(
        [
            [SEROTONIN_OUTPUT_FILE, 0.201767942942],
        ]
    )
    def test_extract_zpve(self, output_file, expected):

        output_data = FileHandler.read_file(output_file)
        result = XtbOutputParser().parse(output_data)
        self.assertEqual(result["zpve"], expected)

    @parameterized.expand(
        [
            [SEROTONIN_OUTPUT_FILE, -37.441567112416],
        ]
    )
    def test_extract_energy(self, output_file, expected):

        output_data = FileHandler.read_file(output_file)
        result = XtbOutputParser().parse(output_data)
        self.assertEqual(result["energy"], expected)

    @parameterized.expand(
        [
            [SEROTONIN_OUTPUT_FILE, -37.226843080132],
        ]
    )
    def test_extract_enthalpy_energy(self, output_file, expected):

        output_data = FileHandler.read_file(output_file)
        result = XtbOutputParser().parse(output_data)
        self.assertEqual(result["enthalpy_energy"], expected)

    @parameterized.expand(
        [
            [SEROTONIN_OUTPUT_FILE, -37.277585026853],
        ]
    )
    def test_extract_free_energy(self, output_file, expected):

        output_data = FileHandler.read_file(output_file)
        result = XtbOutputParser().parse(output_data)
        self.assertEqual(result["free_energy"], expected)

    @parameterized.expand(
        [
            [SEROTONIN_OUTPUT_FILE, 3.469772220532],
        ]
    )
    def test_extract_homo_lumo_gap(self, output_file, expected):

        output_data = FileHandler.read_file(output_file)
        result = XtbOutputParser().parse(output_data)
        self.assertEqual(result["homo_lumo_gap"], expected)

    @parameterized.expand(
        [
            [
                SEROTONIN_OUTPUT_FILE,
                [
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    39.67,
                    75.07,
                    79.77,
                    141.97,
                    188.84,
                    209.09,
                    268.66,
                    317.98,
                    322.92,
                    361.86,
                    390.07,
                    405.10,
                    422.40,
                    433.79,
                    464.61,
                    486.20,
                    567.90,
                    584.52,
                    625.72,
                    691.10,
                    716.88,
                    753.86,
                    789.24,
                    805.09,
                    809.64,
                    841.99,
                    850.35,
                    896.12,
                    917.20,
                    953.01,
                    969.61,
                    1034.66,
                    1068.13,
                    1085.38,
                    1113.67,
                    1127.67,
                    1139.73,
                    1146.56,
                    1189.70,
                    1219.00,
                    1224.71,
                    1246.32,
                    1274.39,
                    1295.24,
                    1316.57,
                    1320.70,
                    1364.71,
                    1374.59,
                    1405.66,
                    1434.43,
                    1479.40,
                    1495.04,
                    1504.35,
                    1565.23,
                    1580.61,
                    1586.30,
                    1632.32,
                    2821.55,
                    2956.63,
                    2968.29,
                    2999.71,
                    3057.11,
                    3079.98,
                    3114.03,
                    3150.14,
                    3378.70,
                    3413.32,
                    3490.05,
                    3531.13,
                ],
            ],
        ]
    )
    def test_extract_vibrational_frequencies(self, output_file, expected):

        output_data = FileHandler.read_file(output_file)
        result = XtbOutputParser().parse(output_data)
        self.assertEqual(result["vibrational_frequencies"], expected)

    @parameterized.expand(
        [
            [
                SEROTONIN_OUTPUT_FILE,
                [
                    [
                        0,
                        1.504,
                        0,
                        0,
                        0,
                        1.308,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0.969,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                    ],
                    [
                        1.504,
                        0,
                        1.335,
                        0,
                        0.108,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0.968,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                    ],
                    [
                        0,
                        1.335,
                        0,
                        1.249,
                        0,
                        0,
                        0,
                        0,
                        0,
                        1.170,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                    ],
                    [
                        0,
                        0,
                        1.249,
                        0,
                        1.323,
                        0,
                        0,
                        1.209,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                    ],
                    [
                        0,
                        0.108,
                        0,
                        1.323,
                        0,
                        1.444,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0.964,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                    ],
                    [
                        1.308,
                        0,
                        0,
                        0,
                        1.444,
                        0,
                        1.053,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                    ],
                    [
                        0,
                        0,
                        0,
                        0,
                        0,
                        1.053,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0.894,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                    ],
                    [
                        0,
                        0,
                        0,
                        1.209,
                        0,
                        0,
                        0,
                        0,
                        1.577,
                        0,
                        1.017,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                    ],
                    [
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        1.577,
                        0,
                        1.197,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0.970,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                    ],
                    [
                        0,
                        0,
                        1.170,
                        0,
                        0,
                        0,
                        0,
                        0,
                        1.197,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0.948,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                    ],
                    [
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        1.017,
                        0,
                        0,
                        0,
                        0.987,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0.974,
                        0.970,
                        0,
                        0,
                        0,
                        0,
                    ],
                    [
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0.987,
                        0,
                        1.023,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0.970,
                        0.977,
                        0,
                        0,
                    ],
                    [
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        1.023,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0.969,
                        0.968,
                    ],
                    [
                        0.969,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                    ],
                    [
                        0,
                        0.968,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                    ],
                    [
                        0,
                        0,
                        0,
                        0,
                        0.964,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                    ],
                    [
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0.894,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                    ],
                    [
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0.970,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                    ],
                    [
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0.948,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                    ],
                    [
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0.974,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                    ],
                    [
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0.970,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                    ],
                    [
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0.970,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                    ],
                    [
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0.977,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                    ],
                    [
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0.969,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                    ],
                    [
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0.968,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                    ],
                ],
            ],
        ]
    )
    def test_extract_wiberg_index_matrix(self, output_file, expected):

        output_data = FileHandler.read_file(output_file)
        result = XtbOutputParser().parse(output_data)
        self.assertEqual(result["wiberg_index_matrix"], expected)

    @parameterized.expand(
        [
            [
                SEROTONIN_OUTPUT_FILE,
                [
                    12.15,
                    12.14,
                    11.57,
                    12.01,
                    12.38,
                    11.24,
                    10.74,
                    7.3,
                    10.46,
                    12.13,
                    10.02,
                    9.96,
                    2.07,
                    10.36,
                    11.38,
                    11.04,
                    6.5,
                    11.81,
                    5.18,
                    11.87,
                    5.03,
                    10.85,
                    8.05,
                    10.8,
                    11.16,
                    11.54,
                    11.47,
                    11.35,
                    3.32,
                    4.52,
                    3.08,
                    10.7,
                    3.29,
                    3.17,
                    3.63,
                    9.81,
                    6.73,
                    6.93,
                    7.5,
                    3.21,
                    9.33,
                    5.14,
                    3.47,
                    2.72,
                    4.95,
                    5.65,
                    4.77,
                    6.67,
                    2.49,
                    4.68,
                    10.27,
                    9.08,
                    4.71,
                    11.53,
                    10.67,
                    10.3,
                    2.01,
                    1.87,
                    11.28,
                    2.09,
                    11.67,
                    11.62,
                    11.7,
                    1.74,
                    1.68,
                    1.78,
                    1.68,
                    1.82,
                    1.82,
                    1.85,
                    1.87,
                    1.53,
                    2.06,
                    1.87,
                    1.86,
                ],
            ],
        ]
    )
    def test_extract_reduced_masses(self, output_file, expected):

        output_data = FileHandler.read_file(output_file)
        result = XtbOutputParser().parse(output_data)
        self.assertEqual(result["reduced_masses"], expected)

    @parameterized.expand(
        [
            [
                SEROTONIN_OUTPUT_FILE,
                [
                    0.04,
                    0.01,
                    0.05,
                    0.07,
                    0.01,
                    0.05,
                    1.3,
                    4.54,
                    0.18,
                    1.1,
                    1.09,
                    2.61,
                    43.66,
                    2.26,
                    6.33,
                    11.37,
                    71.26,
                    9.87,
                    68.04,
                    3.54,
                    99.53,
                    2.28,
                    6.21,
                    5.2,
                    3.64,
                    3.49,
                    13.69,
                    2.1,
                    4.76,
                    40.69,
                    9.95,
                    0.78,
                    0.02,
                    0.17,
                    36.0,
                    37.0,
                    38.0,
                    39.0,
                    40.0,
                    22.36,
                    10.64,
                    60.83,
                    45.0,
                    46126.65,
                    9.76,
                    52.65,
                    4.64,
                    2.61,
                    16.34,
                    29.47,
                    30.86,
                    7.94,
                    5.46,
                    93.84,
                    1.75,
                    2.01,
                    60.0,
                    61.0,
                    62.0,
                    63.0,
                    64.0,
                    0.95,
                    66.24,
                    39.01,
                    40.82,
                    31.93,
                    25.67,
                    21.78,
                    17.69,
                    15.81,
                    12.7,
                    9.04,
                ],
            ],
        ]
    )
    def test_extract_ir_intensities(self, output_file, expected):

        output_data = FileHandler.read_file(output_file)
        result = XtbOutputParser().parse(output_data)
        self.assertEqual(result["ir_intensities"], expected)

    @parameterized.expand(
        [
            [
                SEROTONIN_OUTPUT_FILE,
                [
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                ],
            ],
        ]
    )
    def test_extract_raman_intensities(self, output_file, expected):

        output_data = FileHandler.read_file(output_file)
        result = XtbOutputParser().parse(output_data)
        self.assertEqual(result["raman_intensities"], expected)

    @parameterized.expand(
        [
            [
                SEROTONIN_OUTPUT_FILE,
                [
                    2.924,
                    2.909,
                    3.087,
                    3.12,
                    2.91,
                    2.846,
                    1.659,
                    3.055,
                    3.037,
                    2.777,
                    3.805,
                    3.732,
                    2.63,
                    0.926,
                    0.926,
                    0.925,
                    0.805,
                    0.926,
                    0.86,
                    0.924,
                    0.924,
                    0.923,
                    0.924,
                    0.86,
                    0.86,
                ],
            ],
        ]
    )
    def test_extract_atomic_coordination_numbers(self, output_file, expected):

        output_data = FileHandler.read_file(output_file)
        result = XtbOutputParser().parse(output_data)
        self.assertEqual(result["atomic_coordination_numbers"], expected)

    @parameterized.expand(
        [
            [
                SEROTONIN_OUTPUT_FILE,
                [
                    -0.058,
                    -0.053,
                    0.034,
                    -0.019,
                    -0.079,
                    0.133,
                    -0.403,
                    -0.031,
                    -0.009,
                    -0.104,
                    -0.063,
                    0.028,
                    -0.342,
                    0.048,
                    0.029,
                    0.022,
                    0.293,
                    0.031,
                    0.156,
                    0.046,
                    0.037,
                    0.004,
                    0.031,
                    0.135,
                    0.134,
                ],
            ],
        ]
    )
    def test_extract_atomic_partial_charges(self, output_file, expected):

        output_data = FileHandler.read_file(output_file)
        result = XtbOutputParser().parse(output_data)
        self.assertEqual(result["atomic_partial_charges"], expected)

    @parameterized.expand(
        [
            [
                SEROTONIN_OUTPUT_FILE,
                [
                    29.441,
                    29.321,
                    27.139,
                    28.299,
                    29.963,
                    25.089,
                    20.906,
                    28.729,
                    28.21,
                    23.273,
                    21.713,
                    20.191,
                    28.812,
                    2.351,
                    2.602,
                    2.708,
                    0.742,
                    2.567,
                    1.358,
                    2.366,
                    2.483,
                    2.998,
                    2.573,
                    1.509,
                    1.512,
                ],
            ],
        ]
    )
    def test_extract_atomic_dispersion_coefficients(self, output_file, expected):

        output_data = FileHandler.read_file(output_file)
        result = XtbOutputParser().parse(output_data)
        self.assertEqual(result["atomic_dispersion_coefficients"], expected)

    @parameterized.expand(
        [
            [
                SEROTONIN_OUTPUT_FILE,
                [
                    8.898,
                    8.879,
                    8.54,
                    8.713,
                    8.976,
                    8.209,
                    6.172,
                    8.79,
                    8.712,
                    7.165,
                    6.634,
                    6.414,
                    7.972,
                    2.398,
                    2.522,
                    2.573,
                    1.353,
                    2.506,
                    1.826,
                    2.405,
                    2.464,
                    2.708,
                    2.508,
                    1.925,
                    1.926,
                ],
            ],
        ]
    )
    def test_extract_atomic_polarizabilities(self, output_file, expected):

        output_data = FileHandler.read_file(output_file)
        result = XtbOutputParser().parse(output_data)
        self.assertEqual(result["atomic_polarizabilities"], expected)
