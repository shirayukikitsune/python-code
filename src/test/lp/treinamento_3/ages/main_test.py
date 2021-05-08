import unittest
from os.path import dirname, abspath

from commons.io.utils import run_tests_with_io
from lp.treinamento_3.ages import main


class EvenSquareTestCase(unittest.TestCase):
    @run_tests_with_io(abspath(dirname(__file__)) + '/cases')
    def test_inputs(self):
        main.run()


if __name__ == '__main__':
    unittest.main()
