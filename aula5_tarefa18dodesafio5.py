idade=int(input("Digite a sua idade para saber se você pode votar: "))
if idade >= 18 and idade <= 69:
    print("Seu voto é obrigatorio!")
elif idade == 16 or idade == 17 or idade >= 70:
    print("Seu voto é opcional! ")
else:
    print("Você não pode votar! ")