class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def __str__(self):
        return f"'{self.titulo}' de {self.autor}"

l1 = Livro("Dom Casmurro", "Machado de Assis")
print(l1)
