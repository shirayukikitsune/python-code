import unittest
from os.path import dirname, abspath

from src.library.commons.testing.utils import run_tests_with_io
from src.main.lp.treinamento_3.ages import main


class EvenSquareTestCase(unittest.TestCase):
    @run_tests_with_io(abspath(dirname(__file__)) + '/cases')
    def test_inputs(self):
        main.run()


if __name__ == '__main__':
    unittest.main()
