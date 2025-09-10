texto = input("Digite uma palavra: ").lower()
vogais = "aeiou"
v = sum(1 for letra in texto if letra in vogais)
c = sum(1 for letra in texto if letra.isalpha() and letra not in vogais)

print("Vogais:", v)
print("Consoantes:", c)
