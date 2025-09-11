with open("saida.txt", "r") as arquivo:
    texto = arquivo.read()
    palavras = texto.split()
    print(f"O arquivo tem {len(palavras)} palavras.")
