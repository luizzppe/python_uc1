class conta:
    def __init__(self,numero,titular,saldo):
        self.numero=numero
        self.titular=titular
        self.saldo=saldo
        print(f"O titular de numero: {self.numero} cujo nome é {self.titular} tem um saldo de {self.saldo} reais.")
    
    def deposito(self,valor):
        print(f"Saldo inicial: {self.saldo}")
        self.saldo= self.saldo + valor
        print(f"Saldo final é: {self.saldo}")
    def saque(self,valors):
        print(f"Saldo inicial: {self.saldo}")
        self.saldo = self.saldo - valors
        if self.saldo <= -2000:
            print("Não pode extourar o limite!")
        else:
            print(f"Seu saldo agora é: {self.saldo}")
    
    def info(self):
        print(f"Informações do titular: ID:{self.numero} nome: {self.titular} saldo: {self.saldo} ")


class banco:
    def __init__(self):
        self.contas={}






if __name__ == "__main__":
    c1=conta ("000001,","Papagaio,",1000)
    # c1.info()
    # valor=float(input("Digite o valor para o deposito: "))
    # c1.deposito(valor)
    valors=float(input("DIgite o valor para o saque: "))
    c1.saque(valors)