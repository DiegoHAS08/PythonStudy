frase = input("Digite uma frase: ")
palavras = frase.split()
frequencia = {}

for palavra in palavras:
    palavra = palavra.lower()
    frequencia[palavra] = frequencia.get(palavra, 0) + 1

print("Frequência de palavras:", frequencia)
