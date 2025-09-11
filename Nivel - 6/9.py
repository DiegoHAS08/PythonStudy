produtos = [
    {"nome": "Teclado", "preco": 100},
    {"nome": "Mouse", "preco": 50},
    {"nome": "Monitor", "preco": 800}
]

for p in produtos:
    print(f"{p['nome']} - R$ {p['preco']}")
