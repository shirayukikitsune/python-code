import sys
import unittest
from unittest.mock import patch, call
from io import StringIO
from lp.ambientacao.circle_area import main


class MyTestCase(unittest.TestCase):
    @patch('builtins.print')
    def test_input_one(self, mocked_print):
        stdin = sys.stdin
        sys.stdin = StringIO('2.00\n')

        main.run()

        assert mocked_print.mock_calls == [call('A=12.5664')]

        sys.stdin = stdin

    @patch('builtins.print')
    def test_input_two(self, mocked_print):
        stdin = sys.stdin
        sys.stdin = StringIO('100.64\n')

        main.run()

        assert mocked_print.mock_calls == [call('A=31819.3103')]

        sys.stdin = stdin

    @patch('builtins.print')
    def test_input_three(self, mocked_print):
        stdin = sys.stdin
        sys.stdin = StringIO('150.00\n')

        main.run()

        assert mocked_print.mock_calls == [call('A=70685.7750')]

        sys.stdin = stdin


if __name__ == '__main__':
    unittest.main()
