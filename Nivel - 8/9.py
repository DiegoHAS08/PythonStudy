class Circulo:
    def __init__(self, raio):
        self._raio = raio

    @property
    def raio(self):
        return self._raio

    @raio.setter
    def raio(self, novo_raio):
        if novo_raio > 0:
            self._raio = novo_raio
        else:
            print("Raio inválido!")

c = Circulo(5)
print(c.raio)
c.raio = 10
print(c.raio)
