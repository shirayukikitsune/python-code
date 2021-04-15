import sys
import unittest
from unittest.mock import patch, call
from io import StringIO
from lp.ac_zero.extremely_basic import main


class MyTestCase(unittest.TestCase):
    @patch('builtins.print')
    def test_input_one(self, mocked_print):
        stdin = sys.stdin
        sys.stdin = StringIO('10\n9\n')

        main.run()

        assert mocked_print.mock_calls == [call('X = 19')]

        sys.stdin = stdin

    @patch('builtins.print')
    def test_input_two(self, mocked_print):
        stdin = sys.stdin
        sys.stdin = StringIO('-10\n4\n')

        main.run()

        assert mocked_print.mock_calls == [call('X = -6')]

        sys.stdin = stdin

    @patch('builtins.print')
    def test_input_three(self, mocked_print):
        stdin = sys.stdin
        sys.stdin = StringIO('15\n-7\n')

        main.run()

        assert mocked_print.mock_calls == [call('X = 8')]

        sys.stdin = stdin


if __name__ == '__main__':
    unittest.main()
