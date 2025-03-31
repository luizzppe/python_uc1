pessoa= {"nome": "Papagaio", "idade": 49, "cidade": "Petropolis"}
# print(f"Dados antigos da pessoa: {pessoa}")
pessoa["idade"]=48
# print(f"Dados atualizados da pessoa: {pessoa}")
pessoa["email"]="luis.rodrigo@gmail.com"
# print(f"Email adicionado: {pessoa}")
del pessoa["cidade"]
# print(pessoa)
pessoa["sexo"]= "masculino"
# print(pessoa)
d1={"a": 1, "b": 2}
d2={"c": 3, "d": 4}
d1.update(d2)
d3={**d1, **d2}
print(d1,d2,d3)
