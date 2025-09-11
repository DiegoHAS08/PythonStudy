import json

dados = {
    "nome": "Diego",
    "idade": 18,
    "cidade": "Brasília"
}

with open("dados.json", "w") as f:
    json.dump(dados, f, indent=4)

print("Arquivo JSON criado!")
