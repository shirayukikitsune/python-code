import unittest
from os.path import dirname, abspath

from src.library.commons.testing.utils import run_tests_with_io
from src.main.lp.ambientacao.hello_world import main


class HelloWorldTestCase(unittest.TestCase):
    @run_tests_with_io(abspath(dirname(__file__)) + '/cases')
    def test_inputs(self):
        main.activity()


if __name__ == '__main__':
    unittest.main()
