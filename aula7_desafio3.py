n1=int(input("Digite um número: "))
n2=int(input("Digite um número: "))
n3=int(input("Digite um número: "))
n4=int(input("Digite um número: "))
n5=int(input("Digite um número: "))
if n1>n2 and n3 and n4 and n5:
    print(f"{n1}")
elif n2> n1 and n3 and n4 and n5:
    print(f"{n2}")
elif n3> n4 and n5 and n1 and n2:
    print(f"{n3}")
elif n4> n3 and n2 and n1 and n5:
    print(f"{n4}")
elif n5> n4 and n3 and n2 and n1:
    print(f"{n5}")