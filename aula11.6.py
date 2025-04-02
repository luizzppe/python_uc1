class veiculo:
    def __init__(self,marca,modelo,ano):
        self.marca=marca
        self.modelo=modelo
        self.ano=ano

    def exibir_info(self):
        super().exibir_info()
        print(f"{self.marca}{self.modelo}({self.ano})")


if __name__ == "__main__":
    veiculo.exibir_info()