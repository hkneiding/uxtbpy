import unittest
from parameterized import parameterized

from uxtbpy.file_handler import FileHandler


SEROTONIN_OUTPUT_FILE = './tests/files/serotonin.out'

class TestFileHandler(unittest.TestCase):

    @parameterized.expand([

        [
            SEROTONIN_OUTPUT_FILE
        ]

    ])
    def test_read_file(self, file_path):

        result = FileHandler.read_file(file_path)

        f = open(file_path, 'r')
        expected = f.read()
        f.close()

        self.assertEqual(result, expected)

    @parameterized.expand([

        [
            './tests/files/not-existing-file',
            FileNotFoundError
        ],

        [
            './tests/files/',
            IsADirectoryError
        ],

    ])
    def test_read_file_with_invalid_input(self, file_path, expected_error):

        self.assertRaises(expected_error, FileHandler.read_file, file_path)

    @parameterized.expand([

        [
            'TG9yZW0gaXBzdW0gZG9sb3Igc2l0IGFtZXQsIGNvbnNlY3RldHVyIGFkaXBpc2NpbmcgZWxpdCwgc2'
            'VkIGRvIGVpdXNtb2QgdGVtcG9yIGluY2lkaWR1bnQgdXQgbGFib3JlIGV0IGRvbG9yZSBtYWduYSBh'
            'bGlxdWEuIFV0IGVuaW0gYWQgbWluaW0gdmVuaWFtLCBxdWlzIG5vc3RydWQgZXhlcmNpdGF0aW9uIH'
            'VsbGFtY28gbGFib3JpcyBuaXNpIHV0IGFsaXF1aXAgZXggZWEgY29tbW9kbyBjb25zZXF1YXQuIER1'
            'aXMgYXV0ZSBpcnVyZSBkb2xvciBpbiByZXByZWhlbmRlcml0IGluIHZvbHVwdGF0ZSB2ZWxpdCBlc3'
            'NlIGNpbGx1bSBkb2xvcmUgZXUgZnVnaWF0IG51bGxhIHBhcmlhdHVyLiBFeGNlcHRldXIgc2ludCBv'
            'Y2NhZWNhdCBjdXBpZGF0YXQgbm9uIHByb2lkZW50LCBzdW50IGluIGN1bHBhIHF1aSBvZmZpY2lhIG'
            'Rlc2VydW50IG1vbGxpdCBhbmltIGlkIGVzdCBsYWJvcnVtLg=='
        ]

    ])
    def test_write_file(self, content):

        tmp_file_path = '/tmp/nbo2graph-test-file.txt'

        FileHandler.write_file(tmp_file_path, content)
        result = FileHandler.read_file(tmp_file_path)
        self.assertEqual(content, result)
