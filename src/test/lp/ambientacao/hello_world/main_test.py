import unittest
from unittest.mock import patch, call
from lp.ambientacao.hello_world import main


class MyTestCase(unittest.TestCase):
    @patch('builtins.print')
    def test_activity_output(self, mocked_print):
        main.activity()

        assert mocked_print.mock_calls == [call('Hello World!')]


if __name__ == '__main__':
    unittest.main()
