from os.path import abspath,dirname
import unittest

from src.library.commons.testing.utils import run_tests_with_io
from src.main.lp.treinamento_1.salary import main


class SalaryTestCase(unittest.TestCase):
    @run_tests_with_io(abspath(dirname(__file__)) + '/cases')
    def test_inputs(self):
        main.run()


if __name__ == '__main__':
    unittest.main()
