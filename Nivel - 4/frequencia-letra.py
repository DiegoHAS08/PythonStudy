texto = input("Digite uma frase: ").lower()
frequencia = {}

for letra in texto:
    if letra.isalpha():
        frequencia[letra] = frequencia.get(letra, 0) + 1

print("Frequência de letras:", frequencia)
