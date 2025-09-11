alunos = [
    ["Ana", [8, 7, 9]],
    ["Bruno", [6, 5, 7]],
    ["Clara", [9, 8, 10]]
]

busca = input("Digite o nome do aluno: ")

for nome, notas in alunos:
    if nome.lower() == busca.lower():
        print(f"{nome} encontrado! Notas: {notas}")
        break
else:
    print("Aluno não encontrado.")
