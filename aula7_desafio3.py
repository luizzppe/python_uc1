n1=recebe o valor
n2=recebe o valor
n3=recebe o valor
n4=recebe o valor
n5=recebe o valor
se n1 é maior do que todos os outros
mostre n1
se n2 é maior do que todos os outros
mostre n2
se n3 é maior do que todos os outros
mostre n3
se n4 é maior do que todos os outros
mostre n4
se n5 é maior do que todos os outros
mostre n5


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


P   n1  n2   n3  n4   n5  proc
1   3                     leitura
2   3    4                leitura
3   3    4   15           leitura
4   3    4   15   6       leitura
5   3    4   15   6   2   leitura
6   3    4   15   6   2   comparação
7   3    4   15   6   2   comparação
8   3    4   15   6   2   comparação
9   3    4   15   6   2   comparação
10  3    4   15   6   2   comparação
11  3    4   15   6   2   printar o maior

