class Carro:
    def __init__(self, modelo, ano):
        self.modelo = modelo
        self.ano = ano
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 10
        print(f"{self.modelo} acelerou. Velocidade atual: {self.velocidade} km/h.")

    def frear(self):
        if self.velocidade > 0:
            self.velocidade -= 10
        print(f"{self.modelo} freou. Velocidade atual: {self.velocidade} km/h.")

carro1 = Carro("Fusca", 1980)
carro1.acelerar()
carro1.frear()
