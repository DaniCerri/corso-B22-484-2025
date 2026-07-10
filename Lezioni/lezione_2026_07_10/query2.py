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
# Qual e' lo stipendio medio di tutti gli impiegati?
# =========================================================


# =========================================================
# Domanda 2
# Qual e' lo stipendio massimo presente nel DataFrame?
# =========================================================


# =========================================================
# Domanda 3
# Elenca le regioni uniche in cui si trovano gli uffici.
# =========================================================

