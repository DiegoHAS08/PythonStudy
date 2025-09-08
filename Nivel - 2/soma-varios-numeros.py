total = 0
while True:
    num = input("Digite um número para somar (ou 'sair' para encerrar): ")
    if num.lower() == "sair":
        break
    total += float(num)
print("A soma total é:", total)
