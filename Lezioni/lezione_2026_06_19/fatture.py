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
* Fatturato totale e fatturato medio
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

def fatturato_totale(lista_fatture: list[dict], incassate: bool) -> float:
    """
    Funzione che calcola il fatturato totale, opzionalmente solo delle fatture incassate
    :param lista_fatture: lista di dizionari "fattura"
    :param incassate: True -> conta solo le fatture da incassare, False -> conta tutte le fatture
    :return: somma degli importi delle fatture considerate
    """
    tot = 0
    for fattura in lista_fatture:
        # L'idea è mettere in relazione con uno o più operatori logici il valore di "incassata"
        # del dizionario fattura corrente e il parametro "incassate" passato alla funzione in modo che
        # l'espressione risultate sia sempre vera se incassate è False e vera solamente se fattura['incassata'] è
        # True quando incassate è True
        if fattura['incassata'] or not incassate:
            tot += fattura['importo']

    return tot
    # return sum(fattura['importo'] for fattura in lista_fatture if fattura['incassata'] or not incassate)

def media_fatture(lista_fatture: list[dict]) -> float:
    totale = fatturato_totale(lista_fatture)
    return totale / len(lista_fatture)

"""
Utilizzando le funzioni già fatte dove possibile facciamo 3 nuove funzioi
1. calcola quanto ancora dobbiamo incassare in totale -> vedi funzione fatturato_totale
2. calcola dato il fatturato totale, coef inps, coef irpef, coef di redditività quanto bisogna pagare di tasse (totale)
   suggerimenti: usiamo la funzione appena modificata, a quel punto basta applicare la regole dei coeff percentuali
3. sapendo che le tasse sono basate sul fatturato e non sull'incassato, facciamo una funzione che ci
   dice se abbiamo incassato abbastanza per pagare le tasse o se siamo sotto:
       o stampate il debito/credito che avanza dal pagamento 
       o stampare True se siamo in negativo, False altrimenti -> ci sono 3 casi possibili
"""

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



