with open("saida.txt", "r") as origem:
    conteudo = origem.read()

with open("copia.txt", "w") as destino:
    destino.write(conteudo)

print("Arquivo copiado para 'copia.txt'.")
