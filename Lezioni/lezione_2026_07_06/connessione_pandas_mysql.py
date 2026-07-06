import pandas as pd
from sqlalchemy import create_engine

# =============================================================================
# CONFIGURAZIONE DEI PARAMETRI DI CONNESSIONE
# =============================================================================
# Inserisci qui i dati di accesso al tuo database MySQL
USER = "dev_user"  # "il_tuo_utente"
PASSWORD = "password_sicura" #"la_tua_password"
HOST = "localhost"          # Es. "127.0.0.1" oppure l'IP del server remoto
PORT = "3306"               # La porta di default di MySQL è 3306
DATABASE = "db_prova_pandas"
ENGINE = "pymysql"
LINGUAGGIO = "mysql"
# Creazione della stringa di connessione (Connection String) per MySQL tramite pymysql
connection_string = f"{LINGUAGGIO}+{ENGINE}://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"
print(connection_string)
try:
    # Creazione del motore SQLAlchemy
    engine = create_engine(connection_string)
    print("Motore SQLAlchemy creato correttamente.")
except Exception as e:
    print(f"Errore durante la creazione del motore: {e}")

# =============================================================================
# 1. LETTURA DAL DATABASE (SELECT -> DATAFRAME PANDAS)
# =============================================================================
def leggi_da_db():
    print("\n--- Lettura dati in corso ---")
    
    # Metodo A: Esecuzione di una query SQL personalizzata (Consigliato per filtri e join)
    query_sql = """SELECT 
    c.titolo AS corso,
    c.durata_ore || ' ore' AS durata_totale,
    m.numero_ordine AS n_modulo,
    m.titolo_modulo
FROM corsi c
INNER JOIN moduli m ON c.id_corso = m.corso_id
WHERE c.id_corso = 101 -- Filtra per il corso di Python
ORDER BY m.numero_ordine ASC;"""
    
    try:
        df_da_query = pd.read_sql_query(query_sql, con=engine)
        print("Lettura tramite query completata con successo!")
        print(df_da_query.head())
        return df_da_query
    except Exception as e:
        print(f"Errore durante la lettura tramite query: {e}")
        
    # Metodo B: Caricamento automatico di un'intera tabella (Senza scrivere SQL)
    # try:
    #     df_tabella = pd.read_sql_table("la_tua_tabella", con=engine)
    #     print("Lettura intera tabella completata!")
    #     return df_tabella
    # except Exception as e:
    #     print(f"Errore durante la lettura della tabella: {e}")

# =============================================================================
# 2. SCRITTURA NEL DATABASE (DATAFRAME PANDAS -> TABELLA SQL)
# =============================================================================
def scrivi_nel_db(df_da_salvare):
    print("\n--- Scrittura dati in corso ---")
    
    # PARAMETRO CHIAVE: if_exists
    # - 'fail': (Default) Se la tabella esiste, restituisce un errore.
    # - 'append': Aggiunge le righe alla tabella esistente.
    # - 'replace': Cancella la vecchia tabella (DROP) e ne crea una nuova.
    
    nome_tabella_destinazione = "nuova_tabella_clienti"
    
    try:
        df_da_salvare.to_sql(
            name=nome_tabella_destinazione,
            con=engine,
            if_exists='append',  # Modifica in 'replace' o 'fail' a seconda delle esigenze
            index=False          # Imposta False per evitare di salvare l'indice di pandas come colonna SQL
        )
        print(f"Dati scritti correttamente nella tabella '{nome_tabella_destinazione}'!")
    except Exception as e:
        print(f"Errore durante la scrittura nel database: {e}")

# =============================================================================
# BLOCCO DI TEST (ESEMPIO DI UTILIZZO)
# =============================================================================
if __name__ == "__main__":
    # Nota: Assicurati di aver installato i pacchetti necessari prima di eseguire lo script:
    # pip install pandas sqlalchemy pymysql
    
    # 1. Esegui la lettura (decommenta se la tabella esiste già)
    df = leggi_da_db()
    # print(df)
    # # 2. Esempio di creazione e scrittura di un DataFrame di test
    # df_test = pd.DataFrame({
    #     'nome': ['Mario Rossi', 'Luigi Bianchi', 'Anna Verdi'],
    #     'email': ['mario@esempio.com', 'luigi@esempio.com', 'anna@esempio.com'],
    #     'eta': [34, 28, 42]
    # })
    #
    # print("\nDataFrame di test creato:")
    # print(df_test)
    
    # Prova a scrivere il DataFrame di test nel DB
    # scrivi_nel_db(df_test)
