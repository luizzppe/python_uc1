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

"""
P  N  F    Proc
1  5  1    leitura
2  4  5    processamento
3  3  20   processamento
4  2  60   processamento
5  1  120  processamento
6  0  120  imprimindo o valor na tela
"""

