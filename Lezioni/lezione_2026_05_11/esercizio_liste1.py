"""
Vogliamo arrivare ad avere una lista con dentro solamente numeri interi.
Partiamo da una lista disordinata e con elementi da correggere.

Regole:
  * ci sono dei numeri scritti in formato stringa che vanno convertiti
  * ci sono numeri float che vanno convertiti
  * le sottoliste vanno eliminate e i numeri messi nella lista principale
  * possono succedere situazione in cui due o più punti precedenti sono mischiati
"""

"""
Cose da scoprire: 
  * come eliminare un elemento di una lista (dato l'indice)
  * come aggiungere un elemento in mezzo alla lista
  * come invertire una lista
"""

lista = [
    1, 2.3, "2", "12.2", [1, 2, "3"], "1", 2.2, [2, "0.1", 0.1]
]

lista[1] = int(lista[1])
lista[2] = int(lista[2])
lista[3] = int(float(lista[3]))
# lista[3] = int(lista[3][:2])  # Equivalente alla prima
# lista[3] = int(lista[3].split(".")[0])  # Un po' più robusta della seconda

lista[-2] = int(lista[-2])
lista[-3] = int(lista[-3])

# TODO: stampare la lista
# TODO: stampare la lista invertita

