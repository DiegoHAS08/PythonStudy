import random
numero = random.randint(1, 10)
chute = 0
while chute != numero:
    chute = int(input("Tente adivinhar o número (1 a 10): "))
    if chute < numero:
        print("Muito baixo!")
    elif chute > numero:
        print("Muito alto!")
print("Parabéns! Você acertou:", numero)
