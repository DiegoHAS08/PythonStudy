import random

def jogar():
    numero = random.randint(1, 20)
    tentativas = 0
    while True:
        chute = int(input("Adivinhe o número (1 a 20): "))
        tentativas += 1
        if chute == numero:
            print(f"Parabéns! Você acertou em {tentativas} tentativas.")
            break
        elif chute < numero:
            print("Muito baixo!")
        else:
            print("Muito alto!")

jogar()
