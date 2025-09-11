with open("saida.txt", "r") as arquivo:
    linhas = [linha.strip() for linha in arquivo if linha.strip()]

print("Linhas não vazias:")
for l in linhas:
    print(l)
