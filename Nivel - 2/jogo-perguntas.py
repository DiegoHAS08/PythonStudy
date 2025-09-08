pontuacao = 0
respostas = {"Qual a capital do Brasil?": "Brasília",
             "Quantos estados existem no Brasil?": "26"}

for pergunta, resposta in respostas.items():
    resp = input(pergunta + " ")
    if resp.lower() == resposta.lower():
        print("Acertou!")
        pontuacao += 1
    else:
        print("Errou!")
print("Sua pontuação final:", pontuacao)
