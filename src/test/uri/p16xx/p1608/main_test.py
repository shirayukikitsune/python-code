import unittest
from os.path import abspath, dirname

from commons.io.utils import run_tests_with_io
from uri.p16xx.p160x.p1608 import main


class P1608TestCase(unittest.TestCase):
    @run_tests_with_io(abspath(dirname(__file__)) + '/cases')
    def test_inputs(self):
        main.run()


if __name__ == '__main__':
    unittest.main()
