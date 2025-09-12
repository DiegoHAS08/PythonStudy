class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def area(self):
        return self.largura * self.altura

    def perimetro(self):
        return 2 * (self.largura + self.altura)

r1 = Retangulo(5, 3)
print("Área:", r1.area())
print("Perímetro:", r1.perimetro())
