"""
Definiamo "seeder" un file che si occupa di istanziare dei dati iniziali
all'interno del database che siano uguali per tutti.
Per fare questo seeder ci appoggeremo alla libreria random con seed 42

In questo file generiamo una serie di dati da inserire nel DB
"""
import pandas as pd
import random
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

if __name__ == "__main__":
    print(genera_persone(10)[['email', 'indirizzo']])

