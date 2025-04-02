class veiculo:
    def __init__(self,marca,modelo,ano,cor,placa):
        self.marca=marca
        self.modelo=modelo
        self.ano=ano
        self.cor=cor
        self.placa=placa

    def exibir_info(self):
        print(f"{self.marca}{self.modelo}({self.ano}), {self.cor} {self.placa}")


class carro(veiculo):
    def __init__(self,marca,modelo,ano,portas,cor,placa):
        super().__init__(marca,modelo,ano,cor,placa)
        self.portas=portas
        self.placa=placa
    def exibir_info(self):
        super().exibir_info()
        print(f"Esse carro tem {self.portas} portas.")


if __name__ == "__main__":
    meucarro=carro("toyota ", "corolla ", 2020, 4, "vermelho", "kpw2442")
    meucarro.exibir_info()