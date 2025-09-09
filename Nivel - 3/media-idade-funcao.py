def media(lista):
    return sum(lista) / len(lista)

idades = []
while True:
    idade = input("Digite uma idade (ou 'sair'): ")
    if idade.lower() == "sair":
        break
    idades.append(int(idade))

if idades:
    print("A média das idades é:", media(idades))
