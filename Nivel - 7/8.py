class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, titulo):
        self.livros.append(titulo)

    def listar_livros(self):
        print("Livros disponíveis:")
        for livro in self.livros:
            print("-", livro)

b = Biblioteca()
b.adicionar_livro("Dom Casmurro")
b.adicionar_livro("1984")
b.listar_livros()
