d3=d1 = {"a": 1, "b": 2}
d2= {"b": 3, "c": 4}
print(f"Dicionarios originais:")
print(f"D1             :{d1}")
print(f"D2             :{d2}")

d1.update(d2)
d2.update(d3)
print(f"Dicionarios atualizados:")
print(f"D1             :{d1}")
print(f"D2             :{d2}")