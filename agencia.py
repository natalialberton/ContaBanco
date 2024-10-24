from random import randint

class Agencia:

    def __init__(self, telefone, cnpj, numero):
        self.telefone = telefone
        self.cnpj = cnpj
        self.numero = numero
        self.clientes = []
        self.caixa = 0
        self.emprestimos = []

    def verificar_caixa(self):
        if self.caixa < 1000000:
            print("Caixa abaixo do nível recomendado. Caixa atual: {}".format(self.caixa))
        else:
            print("O valor de caixa está ok. Caixa atual: {}",format(self.caixa))

    def emprestar_dinheiro(self, valor, cpf, juros):
        if self.caixa>valor:
            self.emprestimos.append((valor, cpf, juros))
            print("Empréstimo efetuado com sucesso")
        else:
            print("Empréstimo não é possível. Dinheiro não disponível no caixa")

    def adicionar_cliente(self, nome, cpf, patrimonio):
        self.clientes.append((nome,cpf,patrimonio))


class AgenciaVirtual(Agencia):
    
    def __init__(self, site, telefone, cnpj, numero):
        self.site = site
        super().__init__(telefone, cnpj, numero)

    def depositar_paypal(self, valor):
        self.caixa -= valor
        self.caixa_paypal += valor

    def sacar_paypal(self, valor):
        self.caixa_paypal -= valor
        self.caixa += valor


class AgenciaComum(Agencia):
    
    def __init__(self, telefone, cnpj):
        super().__init__(telefone, cnpj, randint(1001, 9999))
        self.caixa = 1000000


class AgenciaPremium(Agencia):
    
    def __init__(self, telefone, cnpj):
        super().__init__(telefone, cnpj, randint(1001, 9999))
        self.caixa = 1000000000

    def adicionar_cliente(self, nome, cpf, patrimonio):
        if patrimonio > 1000000:
            super().adicionar_cliente(nome, cpf, patrimonio)
        else:
            print("Cliente não possui o patrimônio mínimo necessário")


agencia1 = Agencia(22223333, 200000000, 4568)

agencia_virtual = AgenciaVirtual("www.agenciavirtual.com.br", 22224444, 1520000000000, 1000)
agencia_virtual.verificar_caixa()
print(agencia_virtual.__dict__)

agencia_comum = AgenciaComum(33334444, 22200000000000)
agencia_comum.verificar_caixa()
print(agencia_comum.__dict__)

agencia_premium = AgenciaPremium(333333, 3000000000000)
print('\nagencia_premium:')
print(agencia_premium.__dict__)