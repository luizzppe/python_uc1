n1=int(input("Digite um numero: "))
n2=int(input("Digite um numero: "))
n3=int(input("Digite um numero: "))
n4=int(input("Digite um numero: "))
n5=int(input("Digite um numero: "))
lista=[]
def soma_numeros():
    numeros=(n1,n2,n3,n4,n5)
    lista.append(numeros)
    soma=sum(numeros)
    print(f"A soma dos numeros é: {soma}") 
    print(lista)
    
    if __name__ == "__main__":
     soma_numeros()