from io import StringIO
import unittest
from unittest.mock import patch
import os

from src.tcolr.tcolr import TColr


def fixture(type, name):
    return os.path.join(os.path.dirname(__file__), 'fixtures', type, name)

def write_output(fname, output):
    with open(fname, 'w') as f:
        f.write(output)

def expected(expected):
    fixture_file = fixture('expected', expected)
    with open(fixture_file, 'r') as f:
        expected_output = f.read()
    return expected_output


class TestTColr(unittest.TestCase):
    def setUp(self):
        self.arguments = {
            'log_level': 'error',
            'config': fixture('config','config.yaml'),
            'input': 'input.txt'
        }
        self.tcolr = TColr(self.arguments)
        self.maxDiff = None

    @patch('sys.stdout', new_callable=StringIO)
    def test_basic(self, mock_stdout):
        self.tcolr.run({
            'input': fixture('inputs', 'basic.txt'),
            'config': fixture('config', 'basic.yaml')
        })
        output = mock_stdout.getvalue()
        write_output('_basic.txt', output)
        self.assertEqual(output, expected('basic.txt'))

    @patch('sys.stdout', new_callable=StringIO)
    def test_tcolr_ready_vars(self, mock_stdout):
        self.tcolr.run({
            'input': fixture('inputs', 'readyvars.txt'),
            'config': fixture('config', 'readyvars.yaml')
        })
        output = mock_stdout.getvalue()
        write_output('_readyvars.txt', output)
        self.assertEqual(output, expected('readyvars.txt'))


if __name__ == '__main__':
    unittest.main()