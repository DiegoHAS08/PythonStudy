import json

try:
    with open("dados.json", "r") as f:
        dados = json.load(f)
        print("Nome:", dados["nome"])
        print("Idade:", dados["idade"])
        print("Cidade:", dados["cidade"])
except FileNotFoundError:
    print("Arquivo 'dados.json' não encontrado.")
