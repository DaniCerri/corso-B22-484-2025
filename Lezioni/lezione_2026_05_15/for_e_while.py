data = ""
while len(data.split("/")) != 3:
    data = input("Inserisci la tua data di nascita (dd/MM/YYYY): ")
    if len(data.split("/")) != 3:
        print("La data inserita non va bene")

data_conv = [int(numero) for numero in data.split("/")]
print(data_conv)

# data_conv = []
# for numero in data.split("/"):
#     data_conv.append(int(numero))

"""
Adesso chiediamo la data di oggi, 
poi per ogni anno che c'è da quello di nascita a quello corrente
calcoliamo l'interesse che avrebbe avuto un conto da 1000€ con 
tasso del 4% annuo (vogliamo mantenere una lista dei progressi) 
"""
data_oggi = ""
while len(data_oggi.split("/")) != 3:
    data_oggi = input("Inserisci data di oggi (dd/MM/YYYY): ")
    if len(data_oggi.split("/")) != 3:
        print("La data inserita non va bene")
data_oggi_conv = [int(numero) for numero in data_oggi.split("/")]
print(data_oggi_conv)

interesse = 0.04
capitale = 1000
lista_capitali = [1000]
print(data_oggi_conv[-1] - data_conv[-1])
for i in range(data_oggi_conv[-1] - data_conv[-1]):
    capitale *= (1 + interesse)
    lista_capitali.append(capitale)

print([f"{capitale:.2f} €" for capitale in lista_capitali])
print(f"Interesse complessivo: {lista_capitali[-1] / lista_capitali[0] -1:.2%}")

