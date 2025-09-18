import json

dados = {"nome": "Diego", "idade": 20, "cidade": "Brasília"}
with open("dados.json", "w", encoding="utf-8") as f:
    json.dump(dados, f, ensure_ascii=False, indent=4)
