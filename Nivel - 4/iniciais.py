texto = input("Digite seu nome completo: ")
iniciais = "".join([palavra[0].upper() for palavra in texto.split()])
print("Iniciais:", iniciais)
