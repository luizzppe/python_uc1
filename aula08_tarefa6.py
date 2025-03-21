def fatorial(n):
    if n < 0:
        return "Numero invalido para o calculos de fatorial"
    elif n == 0:
        return 1
    else:
        resultado=1
        for i in range(1, n+1):
            resultado*=i
        return resultado
def test_fatorial():
    numero=int(input("Digite um numero para que seja calculado o fatorial: "))
    resultado=fatorial(numero)
    print(f"\n\n O fatorial de {numero} ({numero}!) é igual à {resultado}\n\n")

if __name__ == "__main__":
    test_fatorial()
