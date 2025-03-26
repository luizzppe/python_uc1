vetor=[10, 20, 30, 40, 50]
def imprimir_vetor ():
    print("Vetor é:", vetor)


def iterando_imprimindo (vetor):
    for elemento in vetor:
        print("Elemento é:", elemento)


def soma_vetores ():
    seg_vetor=[2, 4, 5, 5, 7]
    soma = sum(seg_vetor)
    print("Soma dos elementos:",soma)


def menor_e_maior_valor():
    terceiro_vet=[10,50,30,1]
    maior=max(terceiro_vet)
    menor=min(terceiro_vet)
    print("Maior valor é:",maior)
    print("Menor valor é:", menor)


def inverter_ordem():
    quarto_vetor= [1,2,3,4,5,6,7,8]
    vetor_invertido = quarto_vetor[::-1]
    print("Vetor invertido é:",vetor_invertido)


def multiplicar_por_dois():
    quinto_vetor=[2,4,6,8,10,12,1]
    multiplicador = 2
    vetor_mult = [elementos * multiplicador for elementos in quinto_vetor]
    print("Vetor muliplicado:",vetor_mult)


def contar_valor_3():
    sexto_vetor=[2,4,3,3,3,5,5,6,7,3,3,]
    ocorrencias = sexto_vetor.count(3)
    print("O valor 3 aparece",ocorrencias,"Vezes")


def ordenar_vet():
    setimo_vetor=[2,5,6,32,4,5,6,74,10]
    vetor_ordenado = sorted(setimo_vetor)
    print("Vetor ordenado é:", vetor_ordenado)


def remover_duplicados():
    oitavo_vetor=[1,1,1,1,2,3,3,4,5,6,7,8,15,15]
    vetor_sem_duplicados=list(dict.fromkeys(oitavo_vetor))
    print("Vetor sem duplicados é:", vetor_sem_duplicados)
    

def separar_pares_comp():
    nono_vetor=[1,2,3,4,5,6,7,8,9,10]
    pares= [num for num in nono_vetor if num % 2 == 0]
    impares= [num for num in nono_vetor if num % 2 == 1]
    print("Pares:",pares)
    print("Impares:",impares)


def media_acima():
    decimo_vetor=[1,2,3,4,5,6,7,8,9,10]
    media=sum(decimo_vetor) / len(decimo_vetor)
    acima_media = [num for num in decimo_vetor if num>media]
    print("Media:",media)
    print("Elementos acima da media:",acima_media)


if __name__ == "__main__":
    imprimir_vetor()
    iterando_imprimindo(vetor)
    soma_vetores()
    menor_e_maior_valor()
    inverter_ordem()
    multiplicar_por_dois()
    contar_valor_3()
    ordenar_vet()
    remover_duplicados()
    separar_pares_comp()
    media_acima()
