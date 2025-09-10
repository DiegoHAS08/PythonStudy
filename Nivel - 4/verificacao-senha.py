senha = input("Digite sua senha: ")

tem_maiuscula = any(c.isupper() for c in senha)
tem_minuscula = any(c.islower() for c in senha)
tem_numero = any(c.isdigit() for c in senha)
tem_especial = any(c in "!@#$%^&*()_+-=[]{};:,.<>?" for c in senha)

if len(senha) >= 8 and tem_maiuscula and tem_minuscula and tem_numero and tem_especial:
    print("Senha forte!")
else:
    print("Senha fraca!")
