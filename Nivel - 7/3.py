class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R$ {valor}. Saldo atual: R$ {self.saldo}")

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R$ {valor}. Saldo atual: R$ {self.saldo}")
        else:
            print("Saldo insuficiente.")

c1 = ContaBancaria("Diego", 500)
c1.depositar(200)
c1.sacar(100)
