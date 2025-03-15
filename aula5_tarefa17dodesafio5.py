temperatura=int(input("Digite a temperatura atual: "))
if temperatura > 30:
    print("Está quente! ")
elif temperatura <= 30 and temperatura >= 10:
    print("Está agradavel! ")
else:
    print("Está frio! ")