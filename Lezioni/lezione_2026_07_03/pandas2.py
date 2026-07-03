import pandas as pd

df_ordini = pd.read_csv("tech_orders.csv", index_col='OrderID')

# print(f"Stampiamo la colonna Categoria: {df_ordini['Categoria']}")
# print(f"Stampiamo la colonna Categoria e Prodotto: \n{df_ordini[['Categoria', 'Prodotto']]}")

# Facciamo una nuova colonna "Spesa_No_Sconto" in cui ogni valore è dato da
# Prezzo unitario * quantità
df_ordini['Spesa_No_Sconto'] = df_ordini['Prezzo_Unitario'] * df_ordini['Quantita']
print(df_ordini[['Prezzo_Unitario', 'Quantita', 'Spesa_No_Sconto']].sample(5))

# Fate la colonna Prezzo_Finale in cui si applica lo sconto 'Sconto_Applicato'
# al Spesa_No_Sconto

# Fate la colonna Risparmio in cui si calcola il valore in € dello sconto

