frase = input("Digite uma frase: ")
proibidas = ["chato", "feio", "bobo"]

for p in proibidas:
    frase = frase.replace(p, "***")

print("Texto filtrado:", frase)
