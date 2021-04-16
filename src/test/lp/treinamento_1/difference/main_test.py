import unittest

from commons.io.utils import run_tests_with_io
from lp.treinamento_1.difference import main


class DifferenceTestCase(unittest.TestCase):
    @run_tests_with_io('tests/1007')
    def test_inputs(self):
        main.run()


if __name__ == '__main__':
    unittest.main()
