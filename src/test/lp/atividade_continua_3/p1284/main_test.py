import unittest
from os.path import abspath, dirname

from src.library.commons.testing.utils import run_tests_with_io
from src.main.lp.atividade_continua_3.p1284 import main


class SecondChanceTestCase(unittest.TestCase):
    @run_tests_with_io(abspath(dirname(__file__)) + '/cases')
    def test_inputs(self):
        main.run()


if __name__ == '__main__':
    unittest.main()
