import pandas as pd
import db_connection as db
engine = db.crea_engine(True)
query = """
SELECT 
    i.id AS impiegato_id,
    i.nome,
    i.cognome,
    i.ruolo,
    i.stipendio,
    u.nome AS nome_ufficio,
    u.regione AS regione_ufficio,
    o.id AS ordine_id,
    od.quantita,
    od.prezzo AS prezzo_vendita
FROM impiegati i
JOIN uffici u ON i.ufficio_id = u.id
LEFT JOIN ordini o ON i.id = o.impiegato_id
LEFT JOIN ordini_dettaglio od ON o.id = od.ordine_id;
"""

df = pd.read_sql(query, engine)
print(df)

# =========================================================
# Domanda 1
# Filtra solo le righe degli impiegati con ruolo 'Manager' e stampale.
# =========================================================
filtro1 = df['ruolo'] == 'Manager'
print("DOMANDA 1")
print(df[filtro1][['impiegato_id', 'ruolo']])

# =========================================================
# Domanda 2
# Trova l'impiegato con lo stipendio piu' alto e stampa nome, cognome
# e il nome dell'ufficio in cui lavora.
# =========================================================
filtro2 = df['stipendio'] == df['stipendio'].max()
print("DOMANDA 2")
print(df[filtro2][['nome', 'cognome', 'nome_ufficio', 'stipendio']])

# =========================================================
# Domanda 3
# Filtra solo le righe degli impiegati che lavorano in un ufficio
# situato in Lombardia.
# =========================================================
filtro3 = df['regione_ufficio'] == 'Lombardia'
print("DOMANDA 3")
print(df[filtro3][['regione_ufficio', 'nome', 'cognome']])

# TODO: stampare tutti gli impiegati che hanno stipendio sopra la media e che
#  hanno l'ufficio in Lombardia
filtro4 = df['stipendio'] >= df['stipendio'].mean()
print("BONUS")
print(df[filtro3 & filtro4][['regione_ufficio', 'stipendio', 'nome', 'cognome']])