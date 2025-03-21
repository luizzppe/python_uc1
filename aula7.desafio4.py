numero=int(input("Digite um numero que calcularei o fatorial: "))
fatorial=1
while numero>=1:
    fatorial= numero * fatorial
    numero=numero-1
else:
    print(f"{fatorial}")