compras = []
while True:
    item = input("Digite um item para a lista de compras (ou 'sair'): ")
    if item.lower() == "sair":
        break
    compras.append(item)
print("Sua lista de compras:", compras)
