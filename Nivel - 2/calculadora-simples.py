while True:
    operacao = input("Escolha uma operação (+, -, *, /) ou 'sair': ")
    if operacao.lower() == "sair":
        break
    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))
    if operacao == "+":
        print("Resultado:", a + b)
    elif operacao == "-":
        print("Resultado:", a - b)
    elif operacao == "*":
        print("Resultado:", a * b)
    elif operacao == "/":
        if b != 0:
            print("Resultado:", a / b)
        else:
            print("Não é possível dividir por zero.")
    else:
        print("Operação inválida.")
