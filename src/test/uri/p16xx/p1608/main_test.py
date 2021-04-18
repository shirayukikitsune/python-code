import unittest

from commons.io.utils import run_tests_with_io
from uri.p1608 import main


class P1608TestCase(unittest.TestCase):
    @run_tests_with_io('tests/1608')
    def test_inputs(self):
        main.run()


if __name__ == '__main__':
    unittest.main()
