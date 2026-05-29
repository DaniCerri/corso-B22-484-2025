# Definiamo una funzione che si chiama "calcola_media"
# che prende in input una lista di numeri E LA CHIAMA LISTA_NUMERI
def calcola_media(lista_numeri):
    media = sum(lista_numeri) / len(lista_numeri)
    return media

def stampa_riga(tipo, valore, n_cifre):
    if not n_cifre is None:
        valore = round(valore, n_cifre)
    print(f"{tipo}: {valore}")

def processo_completo(lista_num, n_c):
    media = calcola_media(lista_num)
    minimo = min(lista_num)
    massimo = max(lista_num)
    print("-" * 50)
    print(lista_num)
    stampa_riga("Media", media, n_c)
    stampa_riga("Min", minimo, None)
    stampa_riga("Max", massimo, None)

lista = [1, 2, 3]
processo_completo(lista, 2)

lista2 = [5, 9, 6, 1]
processo_completo(lista2, 4)

processo_completo([1, 3, 9, 2, 2, 1], 3)
