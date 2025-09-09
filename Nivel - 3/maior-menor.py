numeros = []
while True:
    entrada = input("Digite um número (ou 'sair'): ")
    if entrada.lower() == "sair":
        break
    numeros.append(float(entrada))

if numeros:
    print("Maior número:", max(numeros))
    print("Menor número:", min(numeros))
else:
    print("Nenhum número informado.")
