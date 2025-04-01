class carro:
    def __init__(self, marca, modelo, ano):
        self.marca=marca
        self.modelo=modelo
        self.ano=ano
        self.ligado=False
    def ligar(self):
        if not self.ligado:
            self.ligado = True
            print(f"{self.marca} {self.modelo} foi ligado")
        else:
            print(f"{self.marca} {self.modelo} foi ligado")
    def desligar(self):
        if self.ligado:
            self.ligado = False
            print(f"{self.marca} {self.modelo} foi desligado")
        else:
            print(f"{self.marca} {self.modelo} foi desligado")
    def exibir_info(self):
        status = "ligado" if self.ligado else "desligado"
        print(f"{self.marca}{self.modelo}{self.ano} está {status}")



if __name__ == "__main__":
    #print(f"Criando um objeto em classe carros")
    meu_carro= carro("Nissan ", "370z ", 2011)
    #print(meu_carro)
    # meu_carro.ligar()
    # meu_carro.desligar()
    meu_carro.exibir_info()
    