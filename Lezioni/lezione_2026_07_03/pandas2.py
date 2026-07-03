import pandas as pd

df_ordini = pd.read_csv("tech_orders.csv", index_col='OrderID')

# print(f"Stampiamo la colonna Categoria: {df_ordini['Categoria']}")
# print(f"Stampiamo la colonna Categoria e Prodotto: \n{df_ordini[['Categoria', 'Prodotto']]}")

# Facciamo una nuova colonna "Spesa_No_Sconto" in cui ogni valore è dato da
# Prezzo unitario * quantità
df_ordini['Spesa_No_Sconto'] = df_ordini['Prezzo_Unitario'] * df_ordini['Quantita']

# Fate la colonna Prezzo_Finale in cui si applica lo sconto 'Sconto_Applicato'
# al Spesa_No_Sconto
df_ordini['Prezzo_Finale'] = df_ordini['Spesa_No_Sconto'] * (1 - df_ordini['Sconto_Applicato'])

# Fate la colonna Risparmio in cui si calcola il valore in € dello sconto
df_ordini['Risparmio'] = df_ordini['Spesa_No_Sconto'] - df_ordini['Prezzo_Finale']
pd.set_option('display.max_columns', None)
# print(df_ordini[['Prezzo_Unitario', 'Quantita', 'Spesa_No_Sconto',
#                  'Sconto_Applicato', 'Prezzo_Finale', 'Risparmio']].sample(5))

# Per filtrare all'interno di un dataframe con una o più condizioni si usa la seguente sintassi:
# Prendiamo tutte le righe in cui il valore della colonna "Categoria" è "Monitor"
# print(df_ordini[df_ordini['Categoria'] == 'Monitor'])

# Stampare tutti gli ordini con quantità maggiore di 1
# filtro = df_ordini['Quantita'] > 1

# Stampare tutti gli ordini con importo senza sconto > 1000
# filtro = df_ordini['Spesa_No_Sconto'] > 1000

# Stampare quanti ordini non hanno PayPal come metodo di pagamento
# filtro = df_ordini['Metodo_Pagamento'] != 'PayPal'

# Stampate anche tutte le righe che hanno uno Sconto_Applicato NaN
filtro = df_ordini['Sconto_Applicato'].isnull()
# print(df_ordini[filtro])

# Rimuoviamo i NAN
# Senza inplace=True, df_ordini.fillna(0.0) restituirebbe solamente una copia
# dell df modificato ma senza modificarlo effettivamente
df_ordini.fillna(0.0, inplace=True)
# print(df_ordini[filtro])

# Vogliamo tutti gli ordini in cui un monitor è stato pagato con carta di credito
condizione1 = df_ordini['Categoria'] == "Monitor"
condizione2 = df_ordini['Metodo_Pagamento'] == "Carta di Credito"
# Per unire i filtri non si usano gli operatori logici comuni,
# and -> &
# or -> |
# not -> ~ (su windows con layout italiano Alt + 126 del tastierino numerico)
filtro_unito = condizione1 & condizione2
print(df_ordini[filtro_unito][['Categoria', 'Prodotto', 'Metodo_Pagamento']])

