while True:
    frase = input("Digite uma frase (ou 'sair'): ")
    if frase.lower() == "sair":
        break
    contador = 0
    for letra in frase.lower():
        if letra in "aeiou":
            contador += 1
    print("Número de vogais:", contador)
