import csv

with open("dados.csv", newline="", encoding="utf-8") as f:
    leitor = csv.reader(f)
    for linha in leitor:
        print(linha)
