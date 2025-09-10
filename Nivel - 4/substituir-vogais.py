texto = input("Digite um texto: ")
for v in "aeiouAEIOU":
    texto = texto.replace(v, "*")
print("Resultado:", texto)
