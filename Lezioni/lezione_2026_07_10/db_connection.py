import pandas as pd
from sqlalchemy import create_engine

# Inserisci qui i dati di accesso al tuo database MySQL
USER = "db484user"  # "il_tuo_utente"
PASSWORD = "db2026!" #"la_tua_password"
HOST = "localhost"          # Es. "127.0.0.1" oppure l'IP del server remoto
PORT = "3306"               # La porta di default di MySQL è 3306
DATABASE = "gestionale2026"
ENGINE = "pymysql"
LINGUAGGIO = "mysql"
# Creazione della stringa di connessione (Connection String) per MySQL tramite pymysql
connection_string = f"{LINGUAGGIO}+{ENGINE}://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"

def crea_engine(v: bool):
    """
    Crea l'engine di connessione al db
    :param v: T -> stampa eventuali messaggi di errore
    :return: engine di connessione
    """
    try:
        # Creazione del motore SQLAlchemy
        engine = create_engine(connection_string)
        return engine
    except Exception as e:
        if v:
            print(f"Errore: {e}")
        return -1