def celsius_para_f(c):
    return (c * 9/5) + 32

def f_para_celsius(f):
    return (f - 32) * 5/9

while True:
    escolha = input("Converter (C/F) ou 'sair': ").lower()
    if escolha == "sair":
        break
    valor = float(input("Digite a temperatura: "))
    if escolha == "c":
        print(f"{valor}°C = {celsius_para_f(valor):.2f}°F")
    elif escolha == "f":
        print(f"{valor}°F = {f_para_celsius(valor):.2f}°C")
    else:
        print("Opção inválida.")
