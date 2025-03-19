numero=int(input("Digite um numero e calcularei o fatorial do mesmo: "))
fatorial= 1
while numero>1:
        fatorial = fatorial * numero
        numero= numero - 1
else:
        print(f"{fatorial}")
        