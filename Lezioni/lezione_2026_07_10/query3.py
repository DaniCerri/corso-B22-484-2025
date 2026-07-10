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
# Qual e' il credito medio considerando tutte le righe?
# =========================================================


# =========================================================
# Domanda 2
# Qual e' il totale ordine massimo presente nel DataFrame?
# =========================================================


# =========================================================
# Domanda 3
# Filtra e mostra solo le righe con stato_consegna 'consegnato'.
# =========================================================

