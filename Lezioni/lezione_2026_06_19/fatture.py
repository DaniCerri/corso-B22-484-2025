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
* Fattura più proficua
* Fattura meno proficua
* Numero di fatture per progetti e numero di fatture per consulenze
* Fatturato totale e fatturato medie
"""
# definiamo le funzioni


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



