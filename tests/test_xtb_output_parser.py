import unittest
from parameterized import parameterized

from uxtbpy.file_handler import FileHandler
from uxtbpy.xtb_output_parser import XtbOutputParser


SEROTONIN_OUTPUT_FILE = './tests/files/serotonin.out'

class TestXtbOutputParser(unittest.TestCase):

    @parameterized.expand([

        [
            SEROTONIN_OUTPUT_FILE,
            131.186589
        ],
    ])
    def test_extract_polarisability(self, output_file, expected):

        output_data = FileHandler.read_file(output_file)
        result = XtbOutputParser().parse(output_data)
        self.assertEqual(result['polarisability'], expected)

    @parameterized.expand([

        [
            SEROTONIN_OUTPUT_FILE,
            -9.6533
        ],
    ])
    def test_extract_homo_energy(self, output_file, expected):

        output_data = FileHandler.read_file(output_file)
        result = XtbOutputParser().parse(output_data)
        self.assertEqual(result['homo_energy'], expected)

    @parameterized.expand([

        [
            SEROTONIN_OUTPUT_FILE,
            -6.1835
        ],
    ])
    def test_extract_lumo_energy(self, output_file, expected):

        output_data = FileHandler.read_file(output_file)
        result = XtbOutputParser().parse(output_data)
        self.assertEqual(result['lumo_energy'], expected)

    @parameterized.expand([

        [
            SEROTONIN_OUTPUT_FILE,
            [6, 6, 6, 6, 6, 6, 8, 6, 6, 7, 6, 6, 7, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        ],
    ])
    def test_extract_atomic_numbers(self, output_file, expected):

        output_data = FileHandler.read_file(output_file)
        result = XtbOutputParser().parse(output_data)
        self.assertEqual(result['atomic_numbers'], expected)

    @parameterized.expand([

        [
            SEROTONIN_OUTPUT_FILE,
            [
                [ 1.48537742545851,  1.27512515137874, -0.03158693279875],
                [ 0.16869681352769,  1.67021148325986,  0.01160869779818],
                [-0.80762796564299,  0.68208930214415,  0.01680432881200],
                [-0.47390461698037, -0.69228124271162, -0.02336211322538],
                [ 0.86922449237798, -1.07101667113193, -0.06371446944804],
                [ 1.83356088511015, -0.08432176143027, -0.06695182562317],
                [ 3.16994424651572, -0.37791763604269, -0.10484918745623],
                [-1.70347709686421, -1.41866898046314, -0.00168846903362],
                [-2.69931793136278, -0.48614183277856,  0.04488307789706],
                [-2.16993082508332,  0.77501619661316,  0.05766310941823],
                [-1.86476822922914, -2.90028481402398, -0.06955742234236],
                [-1.74928665894456, -3.40586514847725, -1.51282187672199],
                [-2.03648088137563, -4.83059603172774, -1.56098058206502],
                [ 2.28429969734342,  1.99887193889496, -0.03726962550319],
                [-0.09516378646319,  2.71685498959369,  0.04139031468475],
                [ 1.14911974673173, -2.11588916133038, -0.08911725322382],
                [ 3.28701559998537, -1.33483768071412, -0.11879516435268],
                [-3.76168565062429, -0.63607563757227,  0.07617190382162],
                [-2.69642844510252,  1.63026909415453,  0.09850787861704],
                [-2.84294705135557, -3.18929829481418,  0.31620944543198],
                [-1.09961935045535, -3.38602217614314,  0.54113299216722],
                [-0.75262324074595, -3.14367876854845, -1.90716801206746],
                [-2.49468861913193, -2.89719324766491, -2.13080596625127],
                [-1.34978460920199, -5.34537644053925, -1.01830733191282],
                [-1.99485394848676, -5.16988262992533, -2.51587551662237]
            ]
        ],
    ])
    def test_optimised_atomic_positions(self, output_file, expected):

        output_data = FileHandler.read_file(output_file)
        result = XtbOutputParser().parse(output_data)
        self.assertEqual(result['optimised_atomic_positions'], expected)

    @parameterized.expand([

        [
            SEROTONIN_OUTPUT_FILE,
            '25\n\n'
            'C 1.48537742545851 1.27512515137874 -0.03158693279875\n'
            'C 0.16869681352769 1.67021148325986 0.01160869779818\n'
            'C -0.80762796564299 0.68208930214415 0.01680432881200\n'
            'C -0.47390461698037 -0.69228124271162 -0.02336211322538\n'
            'C 0.86922449237798 -1.07101667113193 -0.06371446944804\n'
            'C 1.83356088511015 -0.08432176143027 -0.06695182562317\n'
            'O 3.16994424651572 -0.37791763604269 -0.10484918745623\n'
            'C -1.70347709686421 -1.41866898046314 -0.00168846903362\n'
            'C -2.69931793136278 -0.48614183277856 0.04488307789706\n'
            'N -2.16993082508332 0.77501619661316 0.05766310941823\n'
            'C -1.86476822922914 -2.90028481402398 -0.06955742234236\n'
            'C -1.74928665894456 -3.40586514847725 -1.51282187672199\n'
            'N -2.03648088137563 -4.83059603172774 -1.56098058206502\n'
            'H 2.28429969734342 1.99887193889496 -0.03726962550319\n'
            'H -0.09516378646319 2.71685498959369 0.04139031468475\n'
            'H 1.14911974673173 -2.11588916133038 -0.08911725322382\n'
            'H 3.28701559998537 -1.33483768071412 -0.11879516435268\n'
            'H -3.76168565062429 -0.63607563757227 0.07617190382162\n'
            'H -2.69642844510252 1.63026909415453 0.09850787861704\n'
            'H -2.84294705135557 -3.18929829481418 0.31620944543198\n'
            'H -1.09961935045535 -3.38602217614314 0.54113299216722\n'
            'H -0.75262324074595 -3.14367876854845 -1.90716801206746\n'
            'H -2.49468861913193 -2.89719324766491 -2.13080596625127\n'
            'H -1.34978460920199 -5.34537644053925 -1.01830733191282\n'
            'H -1.99485394848676 -5.16988262992533 -2.51587551662237\n'
        ],
    ])
    def test_optimised_xyz(self, output_file, expected):

        output_data = FileHandler.read_file(output_file)
        result = XtbOutputParser().parse(output_data)

        self.assertEqual(result['optimised_xyz'].strip(), expected.strip())

    @parameterized.expand([

        [
            SEROTONIN_OUTPUT_FILE,
            1.129
        ],
    ])
    def test_extract_dipole_moment(self, output_file, expected):

        output_data = FileHandler.read_file(output_file)
        result = XtbOutputParser().parse(output_data)
        self.assertEqual(result['dipole_moment'], expected)

    @parameterized.expand([

        [
            SEROTONIN_OUTPUT_FILE,
            176.2154593
        ],
    ])
    def test_extract_molecular_mass(self, output_file, expected):

        output_data = FileHandler.read_file(output_file)
        result = XtbOutputParser().parse(output_data)
        self.assertEqual(result['molecular_mass'], expected)

    @parameterized.expand([

        [
            SEROTONIN_OUTPUT_FILE,
            8130.0688
        ],
    ])
    def test_extract_enthalpy(self, output_file, expected):

        output_data = FileHandler.read_file(output_file)
        result = XtbOutputParser().parse(output_data)
        self.assertEqual(result['enthalpy'], expected)

    @parameterized.expand([

        [
            SEROTONIN_OUTPUT_FILE,
            49.0254
        ],
    ])
    def test_extract_heat_capacity(self, output_file, expected):

        output_data = FileHandler.read_file(output_file)
        result = XtbOutputParser().parse(output_data)
        self.assertEqual(result['heat_capacity'], expected)

    @parameterized.expand([

        [
            SEROTONIN_OUTPUT_FILE,
            106.7954
        ],
    ])
    def test_extract_entropy(self, output_file, expected):

        output_data = FileHandler.read_file(output_file)
        result = XtbOutputParser().parse(output_data)
        self.assertEqual(result['entropy'], expected)

    @parameterized.expand([

        [
            SEROTONIN_OUTPUT_FILE,
            0.201767942942
        ],
    ])
    def test_extract_zpve(self, output_file, expected):

        output_data = FileHandler.read_file(output_file)
        result = XtbOutputParser().parse(output_data)
        self.assertEqual(result['zpve'], expected)

    @parameterized.expand([

        [
            SEROTONIN_OUTPUT_FILE,
            -37.441567112416
        ],
    ])
    def test_extract_energy(self, output_file, expected):

        output_data = FileHandler.read_file(output_file)
        result = XtbOutputParser().parse(output_data)
        self.assertEqual(result['energy'], expected)

    @parameterized.expand([

        [
            SEROTONIN_OUTPUT_FILE,
            -37.226843080132
        ],
    ])
    def test_extract_enthalpy_energy(self, output_file, expected):

        output_data = FileHandler.read_file(output_file)
        result = XtbOutputParser().parse(output_data)
        self.assertEqual(result['enthalpy_energy'], expected)

    @parameterized.expand([

        [
            SEROTONIN_OUTPUT_FILE,
            -37.277585026853
        ],
    ])
    def test_extract_free_energy(self, output_file, expected):

        output_data = FileHandler.read_file(output_file)
        result = XtbOutputParser().parse(output_data)
        self.assertEqual(result['free_energy'], expected)

    @parameterized.expand([

        [
            SEROTONIN_OUTPUT_FILE,
            3.469772220532
        ],
    ])
    def test_extract_homo_lumo_gap(self, output_file, expected):

        output_data = FileHandler.read_file(output_file)
        result = XtbOutputParser().parse(output_data)
        self.assertEqual(result['homo_lumo_gap'], expected)

    @parameterized.expand([

        [
            SEROTONIN_OUTPUT_FILE,
            [
                0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                39.67, 75.07, 79.77, 141.97, 188.84, 209.09,
                268.66, 317.98, 322.92, 361.86, 390.07, 405.10,
                422.40, 433.79, 464.61, 486.20, 567.90, 584.52,
                625.72, 691.10, 716.88, 753.86, 789.24, 805.09,
                809.64, 841.99, 850.35, 896.12, 917.20, 953.01,
                969.61, 1034.66, 1068.13, 1085.38, 1113.67, 1127.67,
                1139.73, 1146.56, 1189.70, 1219.00, 1224.71, 1246.32,
                1274.39, 1295.24, 1316.57, 1320.70, 1364.71, 1374.59,
                1405.66, 1434.43, 1479.40, 1495.04, 1504.35, 1565.23,
                1580.61, 1586.30, 1632.32, 2821.55, 2956.63, 2968.29,
                2999.71, 3057.11, 3079.98, 3114.03, 3150.14, 3378.70,
                3413.32, 3490.05, 3531.13
            ]
        ],
    ])
    def test_extract_vibrational_frequencies(self, output_file, expected):

        output_data = FileHandler.read_file(output_file)
        result = XtbOutputParser().parse(output_data)
        self.assertEqual(result['vibrational_frequencies'], expected)

    @parameterized.expand([

        [
            SEROTONIN_OUTPUT_FILE,
            [
                [0, 1.504, 0, 0, 0, 1.308, 0, 0, 0, 0, 0, 0, 0, 0.969, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [1.504, 0, 1.335, 0, 0.108, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.968, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 1.335, 0, 1.249, 0, 0, 0, 0, 0, 1.170, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 1.249, 0, 1.323, 0, 0, 1.209, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0.108, 0, 1.323, 0, 1.444, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.964, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [1.308, 0, 0, 0, 1.444, 0, 1.053, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 1.053, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.894, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 1.209, 0, 0, 0, 0, 1.577, 0, 1.017, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1.577, 0, 1.197, 0, 0, 0, 0, 0, 0, 0, 0.970, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 1.170, 0, 0, 0, 0, 0, 1.197, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.948, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1.017, 0, 0, 0, 0.987, 0, 0, 0, 0, 0, 0, 0, 0.974, 0.970, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.987, 0, 1.023, 0, 0, 0, 0, 0, 0, 0, 0, 0.970, 0.977, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1.023, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.969, 0.968],
                [0.969, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0.968, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0.964, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0.894, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0.970, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0.948, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.974, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.970, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.970, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.977, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.969, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.968, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            ]
        ],
    ])
    def test_extract_wiberg_index_matrix(self, output_file, expected):

        output_data = FileHandler.read_file(output_file)
        result = XtbOutputParser().parse(output_data)
        self.assertEqual(result['wiberg_index_matrix'], expected)
