lista = [1, 2.3, 9, 29, 10, 12.2, 10, 29, 21]

somma_totale = sum(lista)  # funzione che calcola la somma di una
# lista di numeri

media = sum(lista) / len(lista)

massimo = max(lista)  # dà il VALORE del massimo,
# per la posizione cercare "argmax"
argmax = lista.index(max(lista))  # NON è molto efficiente questo metodo

minimo = min(lista)
argmin = lista.index(min(lista))  # NON è molto efficiente questo metodo

# Calcoliamo la deviazione standard
scarti_quadrati = [(elemento - media) ** 2 for elemento in lista]
varianza = sum(scarti_quadrati) / len(scarti_quadrati)
dev_std = varianza ** 0.5

# Calcolo esplicito della somma
totale = 0
for elemento in lista:
    totale += elemento

# Calcolo esplicito del massimo
massimo = lista[0]
for elemento in lista[1:]:
    if elemento > massimo:
        massimo = elemento

# Calcolo esplicito del argmax
argmax = 0
for i in range(1, len(lista)):
    if lista[argmax] < lista[i]:
        argmax = i





