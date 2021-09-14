import unittest
from src.main.poo.atividade_continua_2.atividade_conta import Conta, Erro


def _cria_conta() -> Conta:
    return Conta("John Doe", 1, 42, 0)


def _cria_conta_ativa() -> Conta:
    conta = _cria_conta()
    conta.ativa = True
    return conta


def _cria_conta_inativa_com_saldo(saldo) -> Conta:
    return Conta("John Doe", 1, 42, saldo)


def _cria_conta_ativa_com_saldo(saldo) -> Conta:
    conta = _cria_conta_inativa_com_saldo(saldo)
    conta.ativa = True
    return conta


class ContaTestCase(unittest.TestCase):

    def test_constructor_and_getter_properties(self):
        conta = _cria_conta()

        self.assertEqual(conta.titular, "John Doe")
        self.assertEqual(conta.agencia, 1)
        self.assertEqual(conta.numero, 42)
        self.assertEqual(conta.saldo, 0)
        self.assertEqual(conta.ativa, False)

        self.assertEqual(len(conta.tirar_extrato()), 1)
        self.assertEqual(conta.tirar_extrato()[0], ('saldo inicial', 0))

    def test_setter_ativa_changes_value(self):
        conta = _cria_conta()

        conta.ativa = True

        self.assertEqual(conta.ativa, True)

    def test_setter_ativa_asserts_type(self):
        conta = _cria_conta()

        for v in [1234, None, '', [1], (2, 3)]:
            conta.ativa = v
            self.assertEqual(conta.ativa, False)

    def test_depositar_happy_path(self):
        conta = _cria_conta_ativa()

        err = conta.depositar(50)

        self.assertIsNone(err)
        self.assertEqual(conta.saldo, 50)
        self.assertEqual(len(conta.tirar_extrato()), 2)
        self.assertEqual(conta.tirar_extrato()[1], ('deposito', 50))

    def test_depositar_inactive_account(self):
        conta = _cria_conta()

        err = conta.depositar(100)

        self.assertEqual(err, Erro.CONTA_INATIVA)
        self.assertEqual(conta.saldo, 0)
        self.assertEqual(len(conta.tirar_extrato()), 1)

    def test_depositar_invalid_value_type(self):
        conta = _cria_conta_ativa()

        err = conta.depositar('abc')

        self.assertEqual(err, Erro.VALOR_INVALIDO)
        self.assertEqual(conta.saldo, 0)
        self.assertEqual(len(conta.tirar_extrato()), 1)

    def test_depositar_invalid_value_number(self):
        conta = _cria_conta_ativa()

        err = conta.depositar(-100)

        self.assertEqual(err, Erro.VALOR_INVALIDO)
        self.assertEqual(conta.saldo, 0)
        self.assertEqual(len(conta.tirar_extrato()), 1)

    def test_sacar_happy_path(self):
        conta = _cria_conta_ativa_com_saldo(100)

        err = conta.sacar(35)

        self.assertIsNone(err)
        self.assertEqual(conta.saldo, 65)
        self.assertEqual(len(conta.tirar_extrato()), 2)
        self.assertEqual(conta.tirar_extrato()[1], ('saque', 35))

    def test_sacar_inactive_account(self):
        conta = _cria_conta()

        err = conta.sacar(100)

        self.assertEqual(err, Erro.CONTA_INATIVA)
        self.assertEqual(conta.saldo, 0)
        self.assertEqual(len(conta.tirar_extrato()), 1)

    def test_sacar_invalid_value_type(self):
        conta = _cria_conta_ativa()

        err = conta.sacar('abc')

        self.assertEqual(err, Erro.VALOR_INVALIDO)
        self.assertEqual(conta.saldo, 0)
        self.assertEqual(len(conta.tirar_extrato()), 1)

    def test_sacar_invalid_value_number(self):
        conta = _cria_conta_ativa()

        err = conta.sacar(-100)

        self.assertEqual(err, Erro.VALOR_INVALIDO)
        self.assertEqual(conta.saldo, 0)
        self.assertEqual(len(conta.tirar_extrato()), 1)

    def test_sacar_fail_above_balance(self):
        conta = _cria_conta_ativa_com_saldo(50)

        err = conta.sacar(100)

        self.assertEqual(err, Erro.SALDO_INSUFICIENTE)
        self.assertEqual(conta.saldo, 50)
        self.assertEqual(len(conta.tirar_extrato()), 1)

    def test_transferir_happy_path(self):
        conta_origem = _cria_conta_ativa_com_saldo(100)
        conta_destino = _cria_conta_ativa()

        err = conta_origem.transferir(conta_destino, 66)

        self.assertIsNone(err)
        self.assertEqual(conta_origem.saldo, 34)
        self.assertEqual(conta_destino.saldo, 66)
        self.assertEqual(len(conta_origem.tirar_extrato()), 2)
        self.assertEqual(conta_origem.tirar_extrato()[1], ('transferencia', 66))
        self.assertEqual(len(conta_destino.tirar_extrato()), 2)
        self.assertEqual(conta_destino.tirar_extrato()[1], ('deposito', 66))

    def assertTransferNotChanged(self, conta: Conta, conta_destino: Conta):
        self.assertEqual(conta.saldo, 100)
        self.assertEqual(len(conta.tirar_extrato()), 1)
        self.assertEqual(conta_destino.saldo, 0)
        self.assertEqual(len(conta_destino.tirar_extrato()), 1)

    def test_transferir_inactive_account(self):
        conta = _cria_conta_inativa_com_saldo(100)
        conta_destino = _cria_conta_ativa()

        err = conta.transferir(conta_destino, 100)

        self.assertEqual(err, Erro.CONTA_INATIVA)
        self.assertTransferNotChanged(conta, conta_destino)

    def test_transferir_inactive_target_account(self):
        conta = _cria_conta_ativa_com_saldo(100)
        conta_destino = _cria_conta()

        err = conta.transferir(conta_destino, 100)

        self.assertEqual(err, Erro.CONTA_DESTINO_INATIVA)
        self.assertTransferNotChanged(conta, conta_destino)

    def test_transferir_invalid_value_type(self):
        conta = _cria_conta_ativa_com_saldo(100)
        conta_destino = _cria_conta_ativa()

        err = conta.transferir(conta_destino, 'abc')

        self.assertEqual(err, Erro.VALOR_INVALIDO)
        self.assertTransferNotChanged(conta, conta_destino)

    def test_transferir_invalid_value_number(self):
        conta = _cria_conta_ativa_com_saldo(100)
        conta_destino = _cria_conta_ativa()

        err = conta.transferir(conta_destino, -100)

        self.assertEqual(err, Erro.VALOR_INVALIDO)
        self.assertTransferNotChanged(conta, conta_destino)

    def test_transferir_fail_above_balance(self):
        conta = _cria_conta_ativa_com_saldo(100)
        conta_destino = _cria_conta_ativa()

        err = conta.transferir(conta_destino, 1000)

        self.assertEqual(err, Erro.SALDO_INSUFICIENTE)
        self.assertTransferNotChanged(conta, conta_destino)

    def test_tirar_extrato(self):
        conta = _cria_conta_ativa_com_saldo(80)
        conta_2 = _cria_conta_ativa()
        conta.sacar(20)
        conta.depositar(140)
        conta.transferir(conta_2, 175)

        extrato = conta.tirar_extrato()

        self.assertEqual(len(extrato), 4)
        self.assertListEqual(extrato, [('saldo inicial', 80), ('saque', 20), ('deposito', 140), ('transferencia', 175)])


if __name__ == '__main__':
    unittest.main()
