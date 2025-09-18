with open("texto.txt", "r", encoding="utf-8") as f:
    texto = f.read()
    palavras = texto.split()
    print("Número de palavras:", len(palavras))
