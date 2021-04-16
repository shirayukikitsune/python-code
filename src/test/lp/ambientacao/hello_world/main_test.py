import unittest

from commons.io.utils import run_tests_with_io
from lp.ambientacao.hello_world import main


class HelloWorldTestCase(unittest.TestCase):
    @run_tests_with_io('tests/1000')
    def test_inputs(self):
        main.activity()


if __name__ == '__main__':
    unittest.main()
