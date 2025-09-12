class Aluno:
    def __init__(self, nome, notas):
        self.nome = nome
        self.notas = notas

    def calcular_media(self):
        return sum(self.notas) / len(self.notas)

a1 = Aluno("Ana", [8, 7, 9])
print(f"Média de {a1.nome}: {a1.calcular_media():.2f}")
