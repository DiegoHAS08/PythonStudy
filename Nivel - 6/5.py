alunos = [
    ["Ana", [8, 7, 9]],
    ["Bruno", [6, 5, 7]],
    ["Clara", [9, 8, 10]]
]

for nome, notas in alunos:
    media = sum(notas) / len(notas)
    print(f"{nome} - Média: {media:.2f}")
