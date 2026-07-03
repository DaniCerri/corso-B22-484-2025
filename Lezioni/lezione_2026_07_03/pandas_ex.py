# Per installare pandas, nel terminale lanciamo il comando
# 'pip install pandas'
import pandas as pd

diz = {
    "colore": ['rosso', 'blu', 'rosso', 'verde'],
    "marca": ['Ferrari', 'Fiat', 'Ferrari', 'Lamborghini'],
    "costo": [120000, 18000, 2500000, 450678]
}

df = pd.DataFrame(diz)

# Stampare alcune caratteristiche del DataFrame:
# * Tutti i nomi delle colonne
# print(df.columns.tolist())
# * Tutte le tipologie di elementi nelle colonne
# df.info()
# * Stampare una descrizione numerica del DataFrame
# print(df.describe())


df_ordini = pd.read_csv("tech_orders.csv", index_col='OrderID')
print(df_ordini.sample(5))

# 1. Quante e quali colonne ci sono?
# 1. How many columns are there? What are those columns?
colonne = df_ordini.columns.tolist()
print(f"N° colonne: {len(colonne)}")
print(colonne)

# 2. Ci sono valori mancanti?
# 2. Is there any missing value?

# 3. I dati sono tutti letti del tipo giusto?
# 3. Is all the data read with the right conversion?
df_ordini.info()

