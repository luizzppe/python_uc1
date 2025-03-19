soma = 0

while True:
    numero = int(input("Digite um número (ou um número negativo para parar): "))
    
    if numero < 0:
        break
    
    soma += numero

print(f"A soma dos números positivos é: {soma}")
