import unittest
from parameterized import parameterized


class TestXtbOutputParser(unittest.TestCase):

    @parameterized.expand([

        [
            True,
            True
        ],


    def test_graph_generator_settings_from_file(self, input_, expected):
        self.assertEqual(input_, expected)

