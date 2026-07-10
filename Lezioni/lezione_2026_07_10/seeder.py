"""
Definiamo "seeder" un file che si occupa di istanziare dei dati iniziali
all'interno del database che siano uguali per tutti.
Per fare questo seeder ci appoggeremo alla libreria random con seed 42

In questo file generiamo una serie di dati da inserire nel DB
"""
import pandas as pd
import random
from datetime import datetime, timedelta
import db_connection as db

random.seed(42)

# 1. Facciamo le funzioni che creano i dati casuali
lista_nomi = ['Daniele', 'Luca', 'Marco', 'Ilaria', 'Giulia', 'Sofia']
lista_cognomi = ['Rossi', 'Gialli', 'Verdi', 'Blu', 'Bianchi', 'Neri']
citta_provincia_regione = [
    ('Torino', 'TO', 'Piemonte'),
    ('Roma', 'RM', 'Lazio'),
    ('Milano', 'MI', 'Lombardia'),
    ('Palermo', 'PA', 'Sicilia'),
    ('Pisa', 'PI', 'Toscana'),
    ('Napoli', 'NA', 'Campania'),
    ('Venezia', 'VE', 'Veneto')
]
categorie_via = ['Via', 'Corso', 'Piazza', 'Viale']
lista_ruoli = ['Impiegato', 'Manager', 'Direttore', 'Segretario', 'Consulente', 'Commerciale']
lista_categorie = [
    ('Elettronica', 'Prodotti elettronici e accessori'),
    ('Abbigliamento', 'Vestiti e accessori moda'),
    ('Casa', 'Articoli per la casa e arredamento'),
    ('Sport', 'Attrezzatura sportiva e outdoor'),
    ('Libri', 'Libri, riviste e materiale editoriale'),
    ('Alimentari', 'Cibo e bevande'),
    ('Giocattoli', 'Giochi e giocattoli per bambini')
]
stati_consegna = ['da spedire', 'spedito', 'consegnato']
def genera_persone(n: int) -> pd.DataFrame:
    """
    Genera utilizzando le liste definite sopra n persone verosimili
    :param n: numero di persone uniche da ottenere
    :return: DataFrame con tutte le persone
    """
    # facciamo il range da 1 a n+1 così che il primo id delle persone sia automaticamente 1
    # e gli altri a seguire
    diz_persone = {
        "id": [], "cognome": [], "nome": [], "telefono": [],
        "email": [], "indirizzo": [], "citta": [], "provincia": [],
        "regione": [], "credito": []
    }
    for i in range(1, n+1):
        diz_persone['id'].append(i)
        # estraiamo un cognome casuale con la libreria random
        cognome = random.choice(lista_cognomi)
        diz_persone['cognome'].append(cognome) # Lo aggiungiamo alla sua colonna
        nome = random.choice(lista_nomi)
        diz_persone['nome'].append(nome)
        citta, provincia, regione = random.choice(citta_provincia_regione)
        diz_persone['citta'].append(citta)
        diz_persone['regione'].append(regione)
        diz_persone['provincia'].append(provincia)
        mail = f"{nome}.{cognome}{random.randint(0, 100)}@email.com"
        diz_persone['email'].append(mail)
        credito = random.random() * random.randint(0, 100)
        credito = round(credito, 2)
        diz_persone['credito'].append(credito)

        telefono = [str(random.randint(0, 9)) for n in range(10)]
        telefono = "".join(n for n in telefono)
        diz_persone['telefono'].append(telefono)

        indirizzo = (f"{random.choice(categorie_via)} {random.choice(citta_provincia_regione)[0]} "
                     f"{random.randint(0, 200)}")
        diz_persone['indirizzo'].append(indirizzo)

    return pd.DataFrame(diz_persone)

def genera_uffici(n: int) -> pd.DataFrame:
    """
    Genera n uffici verosimili collocati in una delle citta disponibili
    :param n: numero di uffici da ottenere
    :return: DataFrame con tutti gli uffici
    """
    diz_uffici = {
        "id": [], "nome": [], "telefono": [], "citta": [], "regione": []
    }
    for i in range(1, n+1):
        diz_uffici['id'].append(i)
        citta, provincia, regione = random.choice(citta_provincia_regione)
        diz_uffici['nome'].append(f"Ufficio {citta}")
        diz_uffici['citta'].append(citta)
        diz_uffici['regione'].append(regione)

        telefono = [str(random.randint(0, 9)) for _ in range(10)]
        telefono = "".join(telefono)
        diz_uffici['telefono'].append(telefono)

    return pd.DataFrame(diz_uffici)

def genera_impiegati(n: int, n_uffici: int) -> pd.DataFrame:
    """
    Genera n impiegati con riferimento a un ufficio e a un responsabile interno
    :param n: numero di impiegati da ottenere
    :param n_uffici: numero massimo di uffici gia' generati (per la FK ufficio_id)
    :return: DataFrame con tutti gli impiegati
    """
    diz_impiegati = {
        "id": [], "nome": [], "cognome": [], "ruolo": [],
        "responsabile_id": [], "stipendio": [], "ufficio_id": []
    }
    for i in range(1, n+1):
        diz_impiegati['id'].append(i)
        diz_impiegati['nome'].append(random.choice(lista_nomi))
        diz_impiegati['cognome'].append(random.choice(lista_cognomi))
        diz_impiegati['ruolo'].append(random.choice(lista_ruoli))

        # il primo impiegato non ha responsabile, gli altri hanno un id piu' piccolo
        if i == 1:
            diz_impiegati['responsabile_id'].append(None)
        else:
            diz_impiegati['responsabile_id'].append(random.randint(1, i-1))

        stipendio = round(random.uniform(1000, 9999.99), 2)
        diz_impiegati['stipendio'].append(stipendio)

        diz_impiegati['ufficio_id'].append(random.randint(1, n_uffici))

    return pd.DataFrame(diz_impiegati)

def genera_categorie() -> pd.DataFrame:
    """
    Genera tutte le categorie definite nella lista lista_categorie
    :return: DataFrame con tutte le categorie
    """
    diz_categorie = {
        "id": [], "categoria": [], "descrizione": []
    }
    for i, (categoria, descrizione) in enumerate(lista_categorie, start=1):
        diz_categorie['id'].append(i)
        diz_categorie['categoria'].append(categoria)
        diz_categorie['descrizione'].append(descrizione)

    return pd.DataFrame(diz_categorie)

def genera_articoli(n: int, n_categorie: int) -> pd.DataFrame:
    """
    Genera n articoli con riferimento a una categoria
    :param n: numero di articoli da ottenere
    :param n_categorie: numero massimo di categorie gia' generate (per la FK categoria_id)
    :return: DataFrame con tutti gli articoli
    """
    diz_articoli = {
        "id": [], "prezzo": [], "rimanenza": [], "categoria_id": []
    }
    for i in range(1, n+1):
        diz_articoli['id'].append(i)
        prezzo = round(random.uniform(1, 999.99), 2)
        diz_articoli['prezzo'].append(prezzo)
        # rimanenza e' TINYINT UNSIGNED, quindi 0-255
        diz_articoli['rimanenza'].append(random.randint(0, 255))
        diz_articoli['categoria_id'].append(random.randint(1, n_categorie))

    return pd.DataFrame(diz_articoli)

def genera_ordini(n: int, n_clienti: int, n_impiegati: int) -> pd.DataFrame:
    """
    Genera n ordini con riferimento a cliente e impiegato
    :param n: numero di ordini da ottenere
    :param n_clienti: numero massimo di clienti gia' generati (per la FK cliente_id)
    :param n_impiegati: numero massimo di impiegati gia' generati (per la FK impiegato_id)
    :return: DataFrame con tutti gli ordini
    """
    diz_ordini = {
        "id": [], "cliente_id": [], "impiegato_id": [], "data_ordine": [],
        "indirizzo_spedizione": [], "stato_consegna": []
    }
    for i in range(1, n+1):
        diz_ordini['id'].append(i)
        diz_ordini['cliente_id'].append(random.randint(1, n_clienti))
        diz_ordini['impiegato_id'].append(random.randint(1, n_impiegati))

        # generiamo una data casuale negli ultimi due anni
        giorni_indietro = random.randint(0, 730)
        data_ordine = datetime.now() - timedelta(days=giorni_indietro)
        diz_ordini['data_ordine'].append(data_ordine)

        indirizzo = (f"{random.choice(categorie_via)} {random.choice(citta_provincia_regione)[0]} "
                     f"{random.randint(0, 200)}")
        diz_ordini['indirizzo_spedizione'].append(indirizzo)

        diz_ordini['stato_consegna'].append(random.choice(stati_consegna))

    return pd.DataFrame(diz_ordini)

def genera_ordini_dettaglio(n: int, n_ordini: int, n_articoli: int) -> pd.DataFrame:
    """
    Genera n righe di dettaglio ordine. La coppia (ordine_id, articolo_id) e' PK
    quindi deve essere unica
    :param n: numero massimo di righe da generare
    :param n_ordini: numero massimo di ordini gia' generati (per la FK ordine_id)
    :param n_articoli: numero massimo di articoli gia' generati (per la FK articolo_id)
    :return: DataFrame con tutti i dettagli degli ordini
    """
    diz_dettaglio = {
        "ordine_id": [], "articolo_id": [], "quantita": [], "prezzo": []
    }
    coppie_gia_viste = set()
    tentativi = 0
    while len(coppie_gia_viste) < n and tentativi < n * 10:
        ordine_id = random.randint(1, n_ordini)
        articolo_id = random.randint(1, n_articoli)
        tentativi += 1
        if (ordine_id, articolo_id) in coppie_gia_viste:
            continue
        coppie_gia_viste.add((ordine_id, articolo_id))

        diz_dettaglio['ordine_id'].append(ordine_id)
        diz_dettaglio['articolo_id'].append(articolo_id)
        diz_dettaglio['quantita'].append(random.randint(1, 20))
        prezzo = round(random.uniform(1, 999.99), 2)
        diz_dettaglio['prezzo'].append(prezzo)

    return pd.DataFrame(diz_dettaglio)


if __name__ == "__main__":
    print(genera_persone(10))
    print(genera_uffici(5))
    print(genera_impiegati(10, 5))
    print(genera_categorie())
    print(genera_articoli(8, 7))
    print(genera_ordini(15, 10, 10))
    print(genera_ordini_dettaglio(20, 15, 8))

