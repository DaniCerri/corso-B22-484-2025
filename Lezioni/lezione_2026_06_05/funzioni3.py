"""
In questo file facciamo delle funzioni utili per il prossimo esercizio

1. deviazione_standard(lista_numeri: list[int | float])->float
   m = media
   rad_quadrata(
     media(
       somma(
         (e - m per ogni e in lista) ** 2
       )
     )
   )
2. massima_distanza(lista_numeri: list[int | float])->int | float
3. media_geometrica(lista_numeri: list[int | float])->float
4. aggrega(matrice_numeri: list[list[int | float]]) -> list[int | float]
    questa funzione restituisce una lista contenente le somme delle righe
    della matrice
"""
import funzioni2

def deviazione_standard(lista_numeri: list[int | float])->float:
    media = funzioni2.calcola_media(lista_numeri)
    scarti = [(elemento - media) ** 2 for elemento in lista_numeri]
    varianza = funzioni2.calcola_media(scarti)
    return varianza ** 0.5

def massima_distanza(lista_numeri: list[int | float])->int | float:
    massimo = max(lista_numeri)
    minimo = min(lista_numeri)
    return massimo - minimo

def media_geometrica(lista_numeri: list[int | float])->float:
    prodotto = 1
    for elemento in lista_numeri:
        prodotto *= elemento
    return prodotto ** (1 / len(lista_numeri))
