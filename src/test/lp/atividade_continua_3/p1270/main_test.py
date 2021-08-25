import unittest
from os.path import abspath, dirname

from commons.io.utils import run_tests_with_io
from lp.atividade_continua_3.p1270 import main


class DisplayingMultiplicationTableTestCase(unittest.TestCase):
    @run_tests_with_io(abspath(dirname(__file__)) + '/cases')
    def test_inputs(self):
        main.run()


if __name__ == '__main__':
    unittest.main()