import csv

with open("saida.csv", "w", newline="", encoding="utf-8") as f:
    escritor = csv.writer(f)
    escritor.writerow(["Nome", "Idade"])
    escritor.writerow(["Diego", 20])
    escritor.writerow(["Maria", 25])
