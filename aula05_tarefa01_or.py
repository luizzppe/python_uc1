print(" A | B | A OR B")
print("---|---|--------")
for A in [0, 1]:
    for B in [0, 1]:
        resultado = A or B
        print(f" {A} | {B} | {resultado} ")
