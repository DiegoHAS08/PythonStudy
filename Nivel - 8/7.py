class Conta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def __repr__(self):
        return f"Conta('{self.titular}', {self.saldo})"

c = Conta("Diego", 1000)
print(c)
