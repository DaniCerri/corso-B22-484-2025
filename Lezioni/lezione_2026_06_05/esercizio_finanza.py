# Matrice dei prezzi storici
# Righe: Azione Alpha, Azione Beta, Azione Gamma
# Colonne: Settimana 1, Settimana 2, Settimana 3, Settimana 4, Settimana 5

import funzioni3
import funzioni2


def differenza(lista_numeri: list[int | float], tipo: str)->list[int | float]:
    """
    Calcola differenza assoluta o relativa dei valori della lista
    rispetto all'elemento precedente
    :param lista_numeri: lista dei numeri da utilizzare
    :param tipo: rel | abs, rel -> differenza relativa, abs -> differenza assoluta
    :return:
    """
    lista_differenze = [1] * len(lista_numeri)
    if tipo == "abs":
        lista_differenze[0] = 0

    for i in range(1, len(lista_numeri)):
        prezzo_corrente = lista_numeri[i]
        prezzo_precedente = lista_numeri[i - 1]
        differenza_prezzi = prezzo_corrente - prezzo_precedente
        if tipo == "rel":
            differenza_prezzi = round(differenza_prezzi / prezzo_precedente + 1, 4)
        lista_differenze[i] = differenza_prezzi
    return lista_differenze

def matrici_differenza(matrice: list[list[int | float]]) -> tuple[list[list[int | float]], list[list[int | float]]]:
    matrice_assoluta = [differenza(riga, "abs") for riga in matrice]
    matrice_relativa = [differenza(riga, "rel") for riga in matrice]

    return matrice_assoluta, matrice_relativa

prezzi_storici = [
    [100.0, 102.0, 101.5, 103.0, 104.5],
    [45.0, 52.0, 41.0, 48.5, 39.0],
    [200.0, 210.0, 220.5, 231.5, 243.0]
]

nomi_asset = ["Azione Alpha", "Azione Beta", "Azione Gamma"]

diff_prezzi_abs, diff_prezzi_rel = matrici_differenza(prezzi_storici)
valori_finali = funzioni3.aggrega(diff_prezzi_abs)

for i in range(len(prezzi_storici)):
    interesse_medio = funzioni3.media_geometrica(diff_prezzi_rel[i]) - 1
    media = funzioni2.calcola_media(prezzi_storici[i])
    dev_std = funzioni3.deviazione_standard(prezzi_storici[i])
    print(f"Prezzi      : {prezzi_storici[i]}")
    print(f"Abs         : {diff_prezzi_abs[i]}")
    print(f"Rel         : {diff_prezzi_rel[i]}")
    print(f"Delta Finale: {valori_finali[i]:.2f}")
    print(f"Massima variazione: {funzioni3.massima_distanza(diff_prezzi_rel[i]):.2%}")
    print(f"Interesse medio: {interesse_medio:.2%}")
    print(f"Dev Standard: {dev_std:.2f}")
    print(f"Media: {media:.2f}")
    print(f"Indice rischio: {dev_std / media:.2%}")
    print("-" * 50)
