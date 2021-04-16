import unittest

from commons.io.utils import run_tests_with_io
from lp.ambientacao.circle_area import main


class CircleAreaTestCase(unittest.TestCase):
    @run_tests_with_io('tests/1002')
    def test_inputs(self):
        main.run()


if __name__ == '__main__':
    unittest.main()
