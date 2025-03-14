idade=int(input("Digite sua idade: "))
if idade >= 18:
    print("Você pode viajar sozinho")
elif idade == 17 or idade == 16:
    permissao = input("Você tem a autorização dos seus pais para poder viajar sozinho? (responda com sim ou não): ")

    if permissao == "sim":
        print("Você pode viajar sozinho")
    elif permissao == "não":
        print("Você não pode viajar sozinho")  
elif idade < 16:
    print("Você não pode viajar sozinho")
