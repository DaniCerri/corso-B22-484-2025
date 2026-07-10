import pandas as pd
import db_connection as db
engine = db.crea_engine(True)
query = """
SELECT 
    cl.id AS cliente_id,
    cl.provincia,
    cl.regione,
    cl.credito,
    o.id AS ordine_id,
    o.stato_consegna,
    o.data_ordine,
    SUM(od.quantita * od.prezzo) AS totale_ordine
FROM clienti cl
JOIN ordini o ON cl.id = o.cliente_id
JOIN ordini_dettaglio od ON o.id = od.ordine_id
GROUP BY 
    cl.id, cl.provincia, cl.regione, cl.credito, o.id, o.stato_consegna, o.data_ordine;
"""

df = pd.read_sql(query, engine)
print(df)

# =========================================================
# Domanda 1
# Trova l'ordine con il totale_ordine piu' alto e stampa la provincia
# del cliente che l'ha effettuato.
# =========================================================


# =========================================================
# Domanda 2
# Filtra e mostra solo gli ordini dei clienti della regione 'Lazio'.
# =========================================================


# =========================================================
# Domanda 3
# Filtra e mostra solo gli ordini con stato_consegna 'consegnato' e un
# totale_ordine superiore a 100.
# =========================================================

