frase= "o rato roeu a roupa do rei de roma"
palavras=frase.split()
palavras2 = {"nao", "existe", "nenhuma", "comida", "azul", "existe"}
contagem={}
for palavra in palavras:
    contagem[palavra]= contagem.get(palavra, 0)+1

print(contagem)


contagem={}
for palavra in palavras2:
    contagem[palavra]=contagem.get(palavra,0)+1
    print (contagem)