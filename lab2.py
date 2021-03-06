class Cliente:
     def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

class Conta:
    def __init__(self, clientes, numero, saldo = 0):
        self.saldo = 0
        self.clientes = clientes
        self.numero = numero
        self.operacoes = []
        self.deposito(saldo)
    def resumo(self):
        print("CC N°%s Saldo: %10.2f" %
               (self.numero, self.saldo))
    def pode_sacar(self, valor):
        return self.saldo >= valor
    def saque(self, valor):
        if self.pode_sacar(valor):
            self.saldo -= valor
            self.operacoes.append(["SAQUE", valor])
            return True
        else:
            print("Saldo insuficiente!")
            return False
    def deposito(self, valor):
        self.saldo += valor
        self.operacoes.append(["DEPÓSITO", valor])
    def extrato(self):
        print("Extrato CC N° %s\n" % self.numero)
        for o in self.operacoes:
            print("%10s   %10.2f" % (o[0],o[1]))
        print("\n      Saldo: %10.2f\n" % self.saldo)


class ContaEspecial(Conta):
    def __init__(self, clientes, numero, saldo = 0, limite=0):
        Conta.__init__(self, clientes, numero, saldo)
        self.limite = limite
    def pode_sacar(self, valor):
        return self.saldo + self.limite >= valor
    def extrato(self):
        Conta.extrato(self)
        print("\n     Limite: %10.2f\n" % self.limite)
        print("\n Disponivel: %10.2f\n" % (self.limite + self.saldo))

Danilo = Cliente("Danilo", "1111-2222")

conta = ContaEspecial([Danilo], 3432, 5000, 1000)
conta.extrato()
conta.saque(6000)
conta.saque(10000)
conta.saque(12000)
conta.extrato()