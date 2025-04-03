class bibloteca:
    def __init__(self) :
        pass
    def adicionar(self):
        pass
    def listar (self):
        pass
    def emprestar (self):
        pass
    def devolver (self):
        pass

class livro():
    livros = {}
    def livro(self,titulo,autor,ano,status):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.status = status

if __name__ == "__main__":
    menu1 = input("Qual é o nome do livro que vc deseja: ")
    menu2 = input ("\nOq vc deseja fazer com o livro? \n1 - Adicionar o livro \n2 - Listar as opções de livro \n3 - Emprestar o livro\n4 - Devolver o livro\n Insira o número correspondente: ")
