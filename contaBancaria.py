from datetime import datetime
import pytz
from random import randint

class ContaCorrente():

    @staticmethod
    def _data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR.strftime('%d/%m/%Y %H:%M:%S')

    def __init__(self, nome, cpf, agencia, num_conta):
        self._nome = nome
        self._cpf = cpf
        self.__saldo = 0
        self._limite = None
        self._agencia = agencia
        self._num_conta = num_conta
        self._transacoes = []
        self._cartoes = []

    def consultar_saldo(self):
        print('Seu saldo atual é de R${:,.2f}'.format(self.__saldo))
        pass

    def depositar_dinheiro(self,valor):
        self.__saldo += valor
        self._transacoes.append((valor, self.__saldo, ContaCorrente._data_hora()))
        pass

    def _limite_conta(self):
        self.limite = -1000
        return self.limite

    def sacar_dinheiro(self,valor):
        if self.__saldo - valor < self._limite_conta():
            print("Você não tem saldo suficiente para este valor")
            self.consultar_saldo()
        else:
            self.__saldo -= valor
            self._transacoes.append((valor, self.__saldo, ContaCorrente._data_hora()))
        pass

    def consultar_historico_transacoes(self):
        print('Histórico de Transações')
        for transacao in self._transacoes:
            print(transacao)

    def transferir(self, valor, conta_destino):
        self.__saldo -= valor
        self._transacoes.append((-valor, self.__saldo, ContaCorrente._data_hora()))
        conta_destino.__saldo += valor
        conta_destino._transacoes.append((valor, conta_destino.__saldo, ContaCorrente._data_hora()))


class CartaoCredito:

    @staticmethod
    def _data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR.strftime('%d/%m/%Y %H:%M:%S')

    def __init__(self, titular, conta_corrente):
        self.numero = randint(100000000000000000000, 999999999999999999999)
        self.titular = titular
        self.validade = "{}/{}".format(CartaoCredito._data_hora().month, CartaoCredito._data_hora().year + 4)
        self.cod_seguranca = '{}{}{}'.format(randint(0,9),randint(0,9),randint(0,9))
        self.limite = 1000
        self.conta_corrente = conta_corrente
        conta_corrente._cartoes.append(self)