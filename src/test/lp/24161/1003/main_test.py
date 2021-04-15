import sys
import unittest
from unittest.mock import patch, call
from io import StringIO
from lp.ambientacao.simple_sum import main


class MyTestCase(unittest.TestCase):
    @patch('builtins.print')
    def test_input_one(self, mocked_print):
        stdin = sys.stdin
        sys.stdin = StringIO('30\n10\n')

        main.run()

        assert mocked_print.mock_calls == [call('SOMA = 40')]

        sys.stdin = stdin

    @patch('builtins.print')
    def test_input_two(self, mocked_print):
        stdin = sys.stdin
        sys.stdin = StringIO('-30\n10\n')

        main.run()

        assert mocked_print.mock_calls == [call('SOMA = -20')]

        sys.stdin = stdin

    @patch('builtins.print')
    def test_input_three(self, mocked_print):
        stdin = sys.stdin
        sys.stdin = StringIO('0\n0\n')

        main.run()

        assert mocked_print.mock_calls == [call('SOMA = 0')]

        sys.stdin = stdin


if __name__ == '__main__':
    unittest.main()
