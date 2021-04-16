import unittest

from commons.io.utils import run_tests_with_io
from lp.ambientacao.simple_product import main


class MyTestCase(unittest.TestCase):
    @run_tests_with_io('tests/1004')
    def test_inputs(self):
        main.run()


if __name__ == '__main__':
    unittest.main()
