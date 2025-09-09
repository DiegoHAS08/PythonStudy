agenda = {
    "segunda": [],
    "terça": [],
    "quarta": [],
    "quinta": [],
    "sexta": [],
}

while True:
    dia = input("Digite o dia da semana (ou 'sair'): ").lower()
    if dia == "sair":
        break
    if dia in agenda:
        tarefa = input(f"Digite a tarefa para {dia}: ")
        agenda[dia].append(tarefa)
    else:
        print("Dia inválido.")

print("Agenda completa:", agenda)
