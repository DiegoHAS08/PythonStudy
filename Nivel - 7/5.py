class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def exibir(self):
        print(f"Produto: {self.nome} | Preço: R$ {self.preco}")

p1 = Produto("Teclado", 100)
p1.exibir()
