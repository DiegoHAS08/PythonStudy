soma = 0
cont = 0
while True:
    nota = input("Digite uma nota (ou 'sair'): ")
    if nota.lower() == "sair":
        break
    soma += float(nota)
    cont += 1
if cont > 0:
    print("A média das notas é:", soma / cont)
else:
    print("Nenhuma nota foi informada.")
