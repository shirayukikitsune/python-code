import sys
import unittest
from unittest.mock import patch, call
from io import StringIO
from lp.ambientacao.average_1 import main


class MyTestCase(unittest.TestCase):
    @patch('builtins.print')
    def test_input_one(self, mocked_print):
        stdin = sys.stdin
        sys.stdin = StringIO('5.0\n7.1\n')

        main.run()

        assert mocked_print.mock_calls == [call('MEDIA = 6.43182')]

        sys.stdin = stdin

    @patch('builtins.print')
    def test_input_two(self, mocked_print):
        stdin = sys.stdin
        sys.stdin = StringIO('0.0\n7.1\n')

        main.run()

        assert mocked_print.mock_calls == [call('MEDIA = 4.84091')]

        sys.stdin = stdin

    @patch('builtins.print')
    def test_input_three(self, mocked_print):
        stdin = sys.stdin
        sys.stdin = StringIO('10.0\n10.0\n')

        main.run()

        assert mocked_print.mock_calls == [call('MEDIA = 10.00000')]

        sys.stdin = stdin


if __name__ == '__main__':
    unittest.main()
