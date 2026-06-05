"""
Rivediamo la funzione per il calcolo della media
con il type hinting
"""
def calcola_media(lista_numeri: list[int | float])->float:
    """
    Funzione che calcola la media di una lista di numeri
    :param lista_numeri: lista con dentro solamente numeri
    :return: media aritmetica
    """
    return sum(lista_numeri) / len(lista_numeri)

def stampa_riga(tipo: str, valore: int | float, n_cifre: int | None)->None:
    if not n_cifre is None:
        valore = round(valore, n_cifre)
    print(f"{tipo}: {valore}")

def processo_completo(lista_num: list[int | float], n_c: int | None)->None:
    media = calcola_media(lista_num)
    minimo = min(lista_num)
    massimo = max(lista_num)
    print("-" * 50)
    print(lista_num)
    stampa_riga("Media", media, n_c)
    stampa_riga("Min", minimo, None)
    stampa_riga("Max", massimo, None)

if __name__ == "__main__":
    processo_completo([1, 2, 3], 4)

