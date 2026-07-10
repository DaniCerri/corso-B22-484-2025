import pandas as pd
import db_connection as db

engine = db.crea_engine(True)

query = """
SELECT 
    o.id AS ordine_id,
    o.data_ordine,
    c.categoria,
    a.id AS articolo_id,
    od.quantita,
    od.prezzo AS prezzo_vendita,
    a.prezzo AS prezzo_listino
FROM ordini o
JOIN ordini_dettaglio od ON o.id = od.ordine_id
JOIN articoli a ON od.articolo_id = a.id
JOIN categorie c ON a.categoria_id = c.id;
"""

df = pd.read_sql(query, engine)
# print(df)
# print(df.columns)

# =========================================================
# Domanda 1
# Filtra solo le righe della categoria 'Elettronica' e stampale.
# =========================================================
filtro1 = df['categoria'] == "Elettronica"
elettronica = df[filtro1]
print("DOMANDA 1")
print(elettronica[['ordine_id', 'data_ordine', 'categoria']])


# =========================================================
# Domanda 2
# Aggiungi al DataFrame una colonna 'sconto' calcolata come
# prezzo_listino - prezzo_vendita.
# =========================================================
df['sconto'] = df['prezzo_listino'] - df['prezzo_vendita']
print("DOMANDA 2")
print(df[['prezzo_listino', 'prezzo_vendita', 'sconto']])

# =========================================================
# Domanda 3
# Trova la riga con il prezzo_vendita piu' alto e stampa a quale
# categoria appartiene.
# =========================================================
filtro2 = df['prezzo_vendita'] == df['prezzo_vendita'].max()
print("DOMANDA 3")
print(df[filtro2][['ordine_id', 'categoria', 'prezzo_vendita']])
