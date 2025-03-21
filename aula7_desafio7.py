""" "numero" recebe a informaçao do usuario
se o modulo de "numero" por 2 for igual a 0
mostre esse numero é par 
mas se o modulo de "numero" por 2 for 1 
mostre esse numero é impar
"""

numero=int(input("Digite um numero e direi se ele é par ou impar: "))
if numero%2==0:
    print("Esse numero é par!")
elif numero%2==1:
    print("Esse numero é impar!")
