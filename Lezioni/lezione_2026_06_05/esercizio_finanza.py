# Matrice dei prezzi storici
# Righe: Azione Alpha, Azione Beta, Azione Gamma
# Colonne: Settimana 1, Settimana 2, Settimana 3, Settimana 4, Settimana 5

import funzioni3

def differenza(lista_numeri: list[int | float], tipo: str)->list[int | float]:
    """
    Calcola differenza assoluta o relativa dei valori della lista
    rispetto all'elemento precedente
    :param lista_numeri: lista dei numeri da utilizzare
    :param tipo: rel | abs, rel -> differenza relativa, abs -> differenza assoluta
    :return:
    """
    lista_differenze = [1] * len(lista_numeri)
    for i in range(1, len(lista_numeri)):
        prezzo_corrente = lista_numeri[i]
        prezzo_precedente = lista_numeri[i - 1]
        differenza_prezzi = prezzo_corrente - prezzo_precedente
        if tipo == "rel":
            differenza_prezzi = round(differenza_prezzi / prezzo_precedente + 1, 4)
        lista_differenze[i] = differenza_prezzi
    return lista_differenze

prezzi_storici = [
    [100.0, 102.0, 101.5, 103.0, 104.5],
    [45.0, 52.0, 41.0, 48.5, 39.0],
    [200.0, 210.0, 220.5, 231.5, 243.0]
]

nomi_asset = ["Azione Alpha", "Azione Beta", "Azione Gamma"]

lista_interessi = differenza(prezzi_storici[0], tipo="rel")
media_geom = funzioni3.media_geometrica(lista_interessi)
print(lista_interessi)
print(media_geom)