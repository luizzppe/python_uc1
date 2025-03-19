numero1= receba o valor enviado pelo usuario
se o numero1 modulo2 for igual a zero
mostre ao usuario que o numero é par
se o numero1 modulo2 for igual a um
mostre ao usuario que o numero é impar 


numero1=int(input("Digite um número para saber se ele é par ou impar: "))
if numero1 %2 == 0:
    print("Esse número é par!")
elif numero1 %2 == 1:
     print("Esse número é impar!")

P   N    RESULTADO      PROCESSO
1   5                   Leitura
2   5        1          Calculo
3   5        1          Verificando se é par ou impar
4   5        1          printando par
