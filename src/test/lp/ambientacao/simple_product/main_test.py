import sys
import unittest
from unittest.mock import patch, call
from io import StringIO
from lp.ambientacao.simple_product import main


class MyTestCase(unittest.TestCase):
    @patch('builtins.print')
    def test_input_one(self, mocked_print):
        stdin = sys.stdin
        sys.stdin = StringIO('3\n9\n')

        main.run()

        assert mocked_print.mock_calls == [call('PROD = 27')]

        sys.stdin = stdin

    @patch('builtins.print')
    def test_input_two(self, mocked_print):
        stdin = sys.stdin
        sys.stdin = StringIO('-30\n10\n')

        main.run()

        assert mocked_print.mock_calls == [call('PROD = -300')]

        sys.stdin = stdin

    @patch('builtins.print')
    def test_input_three(self, mocked_print):
        stdin = sys.stdin
        sys.stdin = StringIO('0\n9\n')

        main.run()

        assert mocked_print.mock_calls == [call('PROD = 0')]

        sys.stdin = stdin


if __name__ == '__main__':
    unittest.main()
