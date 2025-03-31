
aluno1={"ID": 123, "nome": "Pedro", "notas": [5, 4, 9]}
aluno2={"ID": 456, "nome": "Carol", "notas": [2, 1, 3]}
aluno3={"ID": 789, "nome": "Rodrigo", "notas": [10, 10, 2.5]}

media1= sum(aluno1["notas"]) / len (aluno1["notas"])
print(f"Media do Pedro é igual a {media1}")
aluno1["media"]=media1
print(f"Dados do aluno 1 são {aluno1}")
"""---------------------------------------------"""
media2= sum(aluno2["notas"]) / len (aluno2["notas"])
print(f"Media da Carol é igual a {media2}")
aluno2["media"]=media2
print(f"Dados do aluno 2 são {aluno2}")
"""-----------------------------------------------"""
media3= sum(aluno3["notas"]) / len (aluno3["notas"])
print(f"Media do Rodrigo é igual a {media3}")
aluno3["media"]=media3
print(f"Dados do aluno 3 são {aluno3}")
