import unittest

from commons.io.utils import run_tests_with_io
from lp.ambientacao.extremely_basic import main


class ExtremelyBasicTestCase(unittest.TestCase):
    @run_tests_with_io('tests/1001')
    def test_inputs(self):
        main.run()


if __name__ == '__main__':
    unittest.main()
