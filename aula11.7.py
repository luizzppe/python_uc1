class animal:
    def fazer_som(self):
        pass
class cachorro(animal):
    def fazer_som(self):
        print("au au")
class gato(animal):
    def fazer_som(self):
        print("Miau")
def fazer_barulho(animal):
    animal.fazer_som()

meu_cachorro=cachorro()
meu_gato=gato()





if __name__ == "__main__":
    fazer_barulho(meu_cachorro)
    fazer_barulho(meu_gato)