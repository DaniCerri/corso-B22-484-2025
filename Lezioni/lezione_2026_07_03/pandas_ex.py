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
# * Tutte le tipologie di elementi nelle colonne
# * Stampare una descrizione numerica del DataFrame


