try:
    x = int(input("Digite um número: "))
    y = int(input("Digite outro número: "))
    print("Resultado da divisão:", x / y)
except ZeroDivisionError:
    print("Erro: não é possível dividir por zero.")
except ValueError:
    print("Erro: você deve digitar apenas números.")
