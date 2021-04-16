import unittest

from commons.io.utils import run_tests_with_io
from lp.ambientacao.average_1 import main


class Average1TestCase(unittest.TestCase):
    @run_tests_with_io('tests/1005')
    def test_inputs(self):
        main.run()


if __name__ == '__main__':
    unittest.main()
