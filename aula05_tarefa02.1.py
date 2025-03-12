idade = int(input("Digite sua idade para saber se você pode digirir: "))
carteira = (input("Você possui carteira de habilitação? (responda com sim ou não): "))
if (idade >= 18) and (carteira == "sim"):
    print("Você pode dirigir!")
else:
    print("Desculpe, você não pode dirigir!")