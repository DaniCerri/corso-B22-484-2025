"""
Vogliamo fare uno script per calcolare perimetro e area di un rettangolo
Conosciamo base e altezza
"""
base = 74
altezza = 3.3

area = base * altezza
perimetro = (base + altezza) * 2

stringa = "L'area è ", area # ---> Questa cosa NON dà una stringa
print(stringa)
print("L'area è ", area)
print("-" * 50)
stringa = f"L'area è: {area}"
print(stringa)
print(f"L'area è: {area}")
print(f"Il perimetro è: {perimetro}")

