nome=str(input("Digit seu nome (deve possuir mais que três letras): "))
senha=str(input("Digite sua senha (deve ser uma senha forte e deve ter 6 caracteres ou mais): "))
if len(nome) < 3:
    print("acesso negado (nome muito pequeno)")
elif len(senha) < 6:
    print("acesso negado (senha muito pequena)")
elif senha == "123456":
    print("acesso negado (senha fraca)")
elif senha == "senha":
    print("acesso negado (senha fraca)")
else:
    print("acesso liberado")
