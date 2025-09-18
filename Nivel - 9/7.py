import json

with open("dados.json", "r", encoding="utf-8") as f:
    dados = json.load(f)
    print(dados["nome"], "-", dados["idade"])
