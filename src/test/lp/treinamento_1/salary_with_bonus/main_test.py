from os.path import abspath,dirname
import unittest

from src.library.commons.testing.utils import run_tests_with_io
from src.main.lp.treinamento_1.salary_with_bonus import main


class SalaryWithBonusTestCase(unittest.TestCase):
    @run_tests_with_io(abspath(dirname(__file__)) + '/cases')
    def test_inputs(self):
        main.run()


if __name__ == '__main__':
    unittest.main()
