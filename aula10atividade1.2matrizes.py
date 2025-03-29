# matriz = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# print("Elemento (0,0):",matriz[0][0])
# print("Elemento (2,1):",matriz[2][1])
#     for linha in matriz:
#         print(f"|", end=" ")
#     for elemento in linha:
#         print(elemento, end=' | ')  
#     print()
# matriz = [[int(input(f"Digite o valor para [{i}][{j}]: ")) for j in range(4)] for i in range(4)]

# for linha in matriz:
#     print(linha)
# matriz = []
# for i in range(4):
#     linha=[]
#     for j in range(4):
#         valor=int(input(f"Digite o valor para [{i}][{j}]: "))
#         linha.append(valor)
#     matriz.append(linha)
# for linha in matriz:
#     print(linha)
matriz_4_4 = [
    [1,2,3,4],
    [5,4,3,2],
    [6,7,8,9],
    [1,4,8,9]
]
#soma=0
"""-----------------------------------------------"""
# for i in range(4):
#     for j in range(4):
#         soma=soma + matriz_4_4[i][j]
"""-----------------------------------------------"""
# for i in range(4):
#     soma=soma + sum(matriz_4_4[i])
"""-----------------------------------------------"""
# for linha in matriz_4_4:
#     soma=soma + sum(linha)
"""-----------------------------------------------"""
#print(f"Soma dos elementos: {soma}")
"""-----------------------------------------------"""
# for i, linha in enumerate(matriz_4_4):
#     print(f"Maior valor da linha {i} é {max(linha)}")
"""-----------------------------------------------"""
# for i in range(4):
#     maior=matriz_4_4 [i][0]
#     for j in range(4):
#         if matriz_4_4[i][j] > maior:
#             maior = matriz_4_4[i][j]
#     print(f"Maior valor da linha {i} é {maior}")
"""-----------------------------------------------"""
# lista_pares=[]
# lista_impares=[]
# impares=0
# pares = 0
# for i in range(4):
#     for j in range(4):
#         if matriz_4_4[i][j] %2 == 0:
#             pares +=1
#             lista_pares.append(matriz_4_4[i][j])
#         else:
#             impares=impares+1
#             lista_impares.append(matriz_4_4[i][j])
# print(f"A quantidade de numeros pares é {pares}")
# print(f"A quantidade de numeros impares é {impares}")
# print(f"Os numeros pares são {lista_pares}")
# print(f"Os numeros impares são {lista_impares}")
"""-----------------------------------------------"""
# num = int(input("Digite o numero para multiplicaçao: "))
# linha_escolhida=int(input("Digite a linha a ser multiplicada (0,3): "))
# matriz_4_4[linha_escolhida] = [num * valor for valor in matriz_4_4[linha_escolhida]]
# for linha in matriz_4_4:
#     print(linha) 
"""-----------------------------------------------"""
num = int(input("Digite o numro para multiplicaçao: "))
linha_escolhida = int(input("Digite a linha para ser multiplicada (0,3): "))

for j in range (4):
    matriz_4_4[linha_escolhida] [j] *= num
for linha in matriz_4_4:
    print(linha)
