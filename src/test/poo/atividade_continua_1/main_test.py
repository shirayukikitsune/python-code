import sys
import unittest
from os.path import abspath, dirname

from src.library.commons.testing.utils import run_tests_with_io
from src.main.poo.atividade_continua_1 import numeros


class AtividadeContinua1TestCase(unittest.TestCase):
    @run_tests_with_io(abspath(dirname(__file__)) + '/cases-is-prime')
    def test_eh_primo(self):
        for line in sys.stdin:
            n = int(line)
            print(numeros.eh_primo(n))

    @run_tests_with_io(abspath(dirname(__file__)) + '/cases-prime-list')
    def test_lista_primos(self):
        n = int(input())
        print(numeros.lista_primos(n))

    @run_tests_with_io(abspath(dirname(__file__)) + '/cases-count-primes')
    def test_conta_primos(self):
        i = 0
        for line in sys.stdin:
            n = map(int, line.split())
            if i % 2 == 0:
                n = list(n)
            i += 1
            print(numeros.conta_primos(n))

    @run_tests_with_io(abspath(dirname(__file__)) + '/cases-is-armstrong')
    def test_eh_armstrong(self):
        for line in sys.stdin:
            n = int(line)
            print(numeros.eh_armstrong(n))

    @run_tests_with_io(abspath(dirname(__file__)) + '/cases-is-almost-armstrong')
    def test_eh_quase_armstrong(self):
        for line in sys.stdin:
            n = int(line)
            print(numeros.eh_quase_armstrong(n))


if __name__ == '__main__':
    unittest.main()
