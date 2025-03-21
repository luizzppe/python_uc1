""" a variavel "numero" recebe o numero que o usuario deseja calcular o fatorial
definindo a variavel "fatorial" como 1 (o expoente neutro damultiplicação) para realizar as multiplicações de "numero"
enquanto numero for maior ou igual a um faça:
"fatorial" é igual a "numero" vezes "fatorial"
"numero" é igual a "numero" menos 1
se nao
mostre a função (nesse caso o valor) de fatorial final
"""

numero=int(input("Digite um numero que calcularei o fatorial: "))
fatorial=1
while numero>=1:
    fatorial= numero * fatorial
    numero=numero-1
else:
    print(f"{fatorial}")


