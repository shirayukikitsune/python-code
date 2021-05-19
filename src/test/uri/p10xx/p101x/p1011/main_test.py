import unittest
from os.path import dirname, abspath

from commons.io.utils import run_tests_with_io
from uri.p10xx.p101x.p1011 import main


class SphereTestCase(unittest.TestCase):
    @run_tests_with_io(abspath(dirname(__file__)) + '/cases')
    def test_inputs(self):
        main.run()


if __name__ == '__main__':
    unittest.main()
