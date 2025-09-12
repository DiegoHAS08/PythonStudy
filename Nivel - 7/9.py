class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def aumento(self, percentual):
        self.salario += self.salario * (percentual / 100)
        print(f"{self.nome} recebeu aumento. Novo salário: R$ {self.salario:.2f}")

f1 = Funcionario("Carlos", 2000)
f1.aumento(10)
