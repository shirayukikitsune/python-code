import unittest
from os.path import dirname, abspath

from commons.io.utils import run_tests_with_io
from lp.treinamento_3.sum_of_consecutive_odd_numbers_1 import main


class MultiplesTestCase(unittest.TestCase):
    @run_tests_with_io(abspath(dirname(__file__)) + '/cases')
    def test_inputs(self):
        main.run()


if __name__ == '__main__':
    unittest.main()
