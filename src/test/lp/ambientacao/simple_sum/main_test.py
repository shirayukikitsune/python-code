import unittest

from commons.io.utils import run_tests_with_io
from lp.ambientacao.simple_sum import main


class SimpleSumTestCase(unittest.TestCase):
    @run_tests_with_io('tests/1003')
    def test_inputs(self):
        main.run()


if __name__ == '__main__':
    unittest.main()
