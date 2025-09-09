def soma(a, b): return a + b
def sub(a, b): return a - b
def mult(a, b): return a * b
def div(a, b): return a / b if b != 0 else "Erro: divisão por zero"

while True:
    op = input("Escolha (+, -, *, /) ou 'sair': ")
    if op == "sair":
        break
    x = float(input("Digite o primeiro número: "))
    y = float(input("Digite o segundo número: "))

    if op == "+": print("Resultado:", soma(x, y))
    elif op == "-": print("Resultado:", sub(x, y))
    elif op == "*": print("Resultado:", mult(x, y))
    elif op == "/": print("Resultado:", div(x, y))
    else: print("Operação inválida.")
