#MEU CODIGO ERRADO:

"""
if idade >= 21:
    renda=int(input("Digite sua renda: "))
else:
    print("Você não pode pegar um emprestimo")
if renda >= 2000:
        sujo=(input("Você tem o nome sujo? (responda com sim ou não): "))
    if sujo == "sim":
        print("Você não pode pegar um emprestimo! ")
    elif sujo == "não":
        print("Você pode pegar um emprestimo!")
else:
    print("Você não pode pegar um emprestimo")
"""

#CODIGO QUE VOCÊ FEZ E ME ENSINOU:

"""idade=int(input("Digite sua idade: "))
if idade <= 21 :
    print ("Negado")
else :
    renda=float(input("Digite sua renda :"))
    if (renda < 2000) :
        print ("Negado")
    else :
        sujo=input("Possui nome sujo <s/n> ? ")
        if (sujo == "s") :
            print ("Negado")
        else :
            print ("Aprovado")"""

#SEU CODIGO COM FRASES MAIORES:

idade=int(input("Digite sua idade: "))
if idade <= 21 :
    print ("Você não pode pegar um emprestimo! (idade minima não atingida) ")
else :
    renda=float(input("Digite sua renda: "))
    if (renda < 2000) :
        print ("Você não pode pegar um emprestimo! (renda minima insuficiente) ")
    else :
        sujo=input("Possui nome sujo? (responda com sim ou não): ")
        if (sujo == "sim") :
            print ("Você não pode pegar um emprestimo! (seu nome está sujo) ")
        else :
            print ("Você pode pegar um emprestimo! ")  