primeiro_lado=int(input("Insira três lados de um triângulo e direi se ele é equilátero, isósceles ou escaleno. Insira o valor do primeiro lado: "))
segundo_lado=int(input("Insira o valor do segundo lado: "))
terceiro_lado=int(input("Insira o valor do terceiro lado: "))
if terceiro_lado == segundo_lado == primeiro_lado:
    print("Esse triângulo é equilátero!")
elif terceiro_lado == segundo_lado != primeiro_lado or terceiro_lado == primeiro_lado != segundo_lado or primeiro_lado == segundo_lado != terceiro_lado:
    print("Esse triângulo é isósceles!")
else:
    print("Esse triângulo é escaleno!")