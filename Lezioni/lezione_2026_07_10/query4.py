import pandas as pd
import db_connection as db

engine = db.crea_engine(True)

query = """
SELECT
    c.categoria,
    cl.provincia,
    cl.regione,
    o.id AS ordine_id,
    o.data_ordine,
    o.stato_consegna,
    a.id AS articolo_id,
    od.quantita,
    od.prezzo AS prezzo_vendita,
    a.prezzo AS prezzo_listino,
    (od.quantita * od.prezzo) AS fatturato_riga
FROM ordini o
JOIN ordini_dettaglio od ON o.id = od.ordine_id
JOIN articoli a ON od.articolo_id = a.id
JOIN categorie c ON a.categoria_id = c.id
JOIN clienti cl ON o.cliente_id = cl.id;
"""

df = pd.read_sql(query, engine)
print(df)

# =========================================================
# Domanda 1 (facile)
# Qual e' il fatturato totale complessivo sommando tutte le righe
# della colonna 'fatturato_riga'?
# =========================================================


# =========================================================
# Domanda 2 (facile-media)
# Filtra e mostra solo le righe con stato_consegna 'consegnato' e
# calcola il fatturato totale limitato a queste righe.
# =========================================================


# =========================================================
# Domanda 3 (media)
# Calcola il fatturato totale per ogni categoria usando groupby.
# =========================================================


# =========================================================
# Domanda 4 (difficile)
# Trova le 3 regioni con il fatturato totale piu' alto ordinate in
# modo decrescente.
# =========================================================


# =========================================================
# Domanda 5 (molto difficile)
# Costruisci una pivot table con categoria sulle righe e
# stato_consegna sulle colonne, mostrando la somma di 'fatturato_riga'
# per ogni combinazione. Riempi i valori mancanti con 0.
# =========================================================
