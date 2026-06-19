"""
Abbiamo una lista di dizionari "fattura2" composti così:

[
    {
        "data": "gg-mm-aaaa",
        "importo_euro": 12.34,
        "incassata": True/False,
        "tipologia": "progetto" / "consulenza",
    }
]

L'obiettivo è data una lista di fatture calcolare:
* Fattura più proficua (importo maggiore)
* Fattura meno proficua (importo minore)
* Numero di fatture per progetti e numero di fatture per consulenze
* Fatturato totale e fatturato medie
"""
# definiamo le funzioni
def min_max_fattura(lista_fatture: list[dict]) -> tuple[dict, dict]:
    indice_min = 0
    indice_max = 0

    for i in range(len(lista_fatture)):
        if lista_fatture[i]['importo'] > lista_fatture[indice_max]['importo']:
            indice_max = i

        if lista_fatture[i]['importo'] < lista_fatture[indice_min]['importo']:
            indice_min = i

    return lista_fatture[indice_min], lista_fatture[indice_max]

# TODO: rendere più generica per un numero qualsiasi di tipologie
def conta_tipolgie(lista_fatture: list[dict]) -> tuple[int, int]:
    n_progetti = 0
    n_consulenze = 0
    for fattura in lista_fatture:
        if fattura['tipologia'] == "progetto":
            n_progetti += 1
        else:
            n_consulenze += 1

    return n_progetti, n_consulenze

# lista fatture
lista_fatture = [
    {
        "data": "19-06-2026",
        "importo": 102.23,
        "incassata": False,
        "tipologia": "progetto"
    },
    {
        "data": "12-06-2026",
        "importo": 120.00,
        "incassata": True,
        "tipologia": "consulenza"
    },
    {
        "data": "11-06-2026",
        "importo": 1612.23,
        "incassata": True,
        "tipologia": "progetto"
    },
    {
        "data": "04-06-2026",
        "importo": 100.0,
        "incassata": False,
        "tipologia": "consulenza"
    },
    {
        "data": "29-05-2026",
        "importo": 2000.90,
        "incassata": True,
        "tipologia": "progetto"
    },
]



