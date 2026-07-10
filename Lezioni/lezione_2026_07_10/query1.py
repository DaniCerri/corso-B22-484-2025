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
print(df)

# =========================================================
# Domanda 1
# Quante righe di dettaglio ci sono in totale?
# =========================================================


# =========================================================
# Domanda 2
# Qual e' il prezzo di vendita medio considerando tutte le righe?
# =========================================================


# =========================================================
# Domanda 3
# Elenca le categorie uniche presenti nel DataFrame.
# =========================================================

