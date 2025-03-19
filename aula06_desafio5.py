while True:
    nome = input("Digite seu nome (ou 'sair' para encerrar): ")
    if nome.lower() == "sair":
        print("Saindo")
        break
    else:
        print(f"Olá, {nome}!")

