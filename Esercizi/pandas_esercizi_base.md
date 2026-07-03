# Guida Pratica a Pandas: 10 Esercizi di Base
Dataset di riferimento: tech_orders_expanded.csv

---

## Parte 1: Versione Italiana

### Esercizio 1: Importazione e Prima Ispezione
- Obiettivo: Imparare a caricare un file CSV in Python e visualizzare le prime righe del DataFrame per capire come è organizzata la tabella.
- Parte Guidata:

```python
import pandas as pd

# Caricamento del dataset
df = pd.read_csv("../../../../Scaricati/tech_orders_expanded.csv")

# Visualizzazione delle prime 5 righe
print(df.head())
```
- Da fare in autonomia:
  1. Visualizza le prime 10 righe del DataFrame modificando il parametro del metodo head().
  2. Visualizza le ultime 5 righe del DataFrame utilizzando il metodo tail().

### Esercizio 2: Dimensioni e Tipi di Dato
- Obiettivo: Scoprire quante righe e colonne contiene il dataset e quali tipi di dati (interi, decimali, testi) sono presenti.
- Parte Guidata:
```python
# Controlliamo il numero di righe e colonne
print("Dimensioni della tabella:", df.shape)

# Controllo dei tipi di dato e delle celle piene
df.info()
```
- Da fare in autonomia:
  1. Utilizza il metodo describe() per generare un riassunto statistico automatico (media, minimo, massimo) delle colonne numeriche.
  2. Rispondi alla domanda: qual è il prezzo unitario minimo presente nel dataset?

### Esercizio 3: Selezione di Colonne
- Obiettivo: Imparare ad estrarre una singola colonna oppure una serie specifica di colonne dal dataset principale.
- Parte Guidata:
```python
# Selezione di una singola colonna
colonna_prodotti = df["Prodotto"]
print(colonna_prodotti.head())
```
- Da fare in autonomia:
  1. Crea una nuova tabella chiamata dettagli_clienti contenente solo le colonne Cliente_ID, Citta_Destinazione e Metodo_Pagamento.
  2. Stampa a schermo le prime 8 righe della nuova tabella dettagli_clienti.

### Esercizio 4: Ordinamento dei Dati
- Obiettivo: Ordinare la tabella in base ai valori di una colonna, sia in ordine crescente che decrescente.
- Parte Guidata:
```python
# Ordinamento per prezzo unitario dal più alto al più basso
df_ordinato = df.sort_values(by="Prezzo_Unitario", ascending=False)
print(df_ordinato[["Prodotto", "Prezzo_Unitario"]].head())
```
- Da fare in autonomia:
  1. Ordina il dataset in base alla colonna Quantita dal numero più piccolo al più grande (ordine crescente).
  2. Ordina il dataset in ordine alfabetico (dalla A alla Z) basandoti sulla colonna Citta_Destinazione.

### Esercizio 5: Filtri con una Condizione
- Obiettivo: Selezionare solo le righe che rispettano un certo criterio logico.
- Parte Guidata:
```python
# Filtriamo per mantenere solo gli ordini pagati con PayPal
ordini_paypal = df[df["Metodo_Pagamento"] == "PayPal"]
print(ordini_paypal[["OrderID", "Metodo_Pagamento"]].head())
```
- Da fare in autonomia:
  1. Filtra il dataset per mostrare solo gli ordini della categoria "Laptop".
  2. Filtra il dataset per selezionare solo gli ordini con una Quantita maggiore o uguale a 2.

### Esercizio 6: Filtri con Condizioni Multiple
- Obiettivo: Combinare due condizioni logiche usando l'operatore AND (&) e l'operatore OR (|).
- Parte Guidata:
```python
# Ordini della categoria Laptop che costano meno di 1200 euro
filtro_combinato = (df["Categoria"] == "Laptop") & (df["Prezzo_Unitario"] < 1200)
print(df[filtro_combinato][["Prodotto", "Prezzo_Unitario"]])
```
- Da fare in autonomia:
  1. Trova tutti gli ordini spediti a "Milano" oppure a "Roma" usando l'operatore OR (|).
  2. Trova tutti gli ordini pagati con "Carta di Credito" che hanno uno Sconto_Applicato maggiore di 0.05.

### Esercizio 7: Gestione dei Valori Mancanti
- Obiettivo: Trovare le celle vuote all'interno della tabella e riempirle con un valore predefinito.
- Parte Guidata:
```python
# Controlliamo quante celle vuote ci sono per ogni colonna
print("Celle vuote prima della pulizia:")
print(df.isnull().sum())

# Riempiamo i valori mancanti nello sconto con lo 0.0
df["Sconto_Applicato"] = df["Sconto_Applicato"].fillna(0.0)
```
- Da fare in autonomia:
  1. Controlla di nuovo il numero di celle vuote con df.isnull().sum() per verificare che non ci siano più valori mancanti nella colonna degli sconti.
  2. Prova a creare una copia del dataset e a usare il metodo dropna() per eliminare direttamente le righe che contengono celle vuote. Controlla quante righe rimangono.

### Esercizio 8: Creazione di Nuove Colonne
- Obiettivo: Eseguire calcoli matematici tra le colonne esistenti per generare nuove metriche e arricchire il dataset.
- Parte Guidata:
```python
# Creiamo la colonna del fatturato lordo moltiplicando il prezzo per la quantità
df["Fatturato_Lordo"] = df["Prezzo_Unitario"] * df["Quantita"]
print(df[["Prodotto", "Prezzo_Unitario", "Quantita", "Fatturato_Lordo"]].head())
```
- Da fare in autonomia:
  1. Crea una nuova colonna chiamata Valore_Sconto moltiplicando il Fatturato_Lordo per la colonna Sconto_Applicato.
  2. Crea una colonna chiamata Fatturato_Netto sottraendo il Valore_Sconto dal Fatturato_Lordo.

### Esercizio 9: Conteggi e Frequenze
- Obiettivo: Contare quante volte appare ogni elemento in una colonna testuale per scoprire gli elementi più comuni.
- Parte Guidata:
```python
# Contiamo il numero di ordini per ciascun metodo di pagamento
conteggio_pagamenti = df["Metodo_Pagamento"].value_counts()
print(conteggio_pagamenti)
```
- Da fare in autonomia:
  1. Utilizza il metodo value_counts() sulla colonna Citta_Destinazione per scoprire qual è la città che riceve il maggior numero di ordini.
  2. Utilizza value_counts() sulla colonna Categoria per vedere quanti ordini ha ricevuto ogni singola categoria di prodotto.

### Esercizio 10: Raggruppamento Dati (groupby)
- Obiettivo: Suddividere i dati in categorie e calcolare somme o medie per ciascun gruppo.
- Parte Guidata:
```python
# Calcoliamo il totale del fatturato lordo per ogni categoria
fatturato_per_categoria = df.groupby("Categoria")["Fatturato_Lordo"].sum()
print(fatturato_per_categoria)
```
- Da fare in autonomia:
  1. Raggruppa il dataset per Metodo_Pagamento e calcola il prezzo unitario medio usando il metodo mean().
  2. Raggruppa per Stato_Spedizione e calcola il totale dei pezzi venduti (somma della colonna Quantita).

---

## Part 2: English Version

### Exercise 1: Importing and First Inspection
- Objective: Learn how to load a CSV file into Python and display the first rows of the DataFrame to understand the table structure.
- Guided Part:
```python
import pandas as pd

# Loading the dataset
df = pd.read_csv("tech_orders_expanded.csv")

# Displaying the first 5 rows
print(df.head())
```
- On Your Own:
  1. Display the first 10 rows of the DataFrame by changing the parameter inside the head() method.
  2. Display the last 5 rows of the DataFrame using the tail() method.

### Exercise 2: Dimensions and Data Types
- Objective: Find out how many rows and columns the dataset contains and what data types (integers, decimals, text) are present.
- Guided Part:
```python
# Checking table dimensions (rows, columns)
print("Table dimensions:", df.shape)

# Checking data types and non-null counts
df.info()
```
- On Your Own:
  1. Use the describe() method to generate an automatic statistical summary (mean, min, max) of the numerical columns.
  2. Answer the question: what is the minimum unit price in the dataset?

### Exercise 3: Column Selection
- Objective: Learn how to extract a single column or a specific subset of columns from the main dataset.
- Guided Part:
```python
# Selecting a single column
colonna_prodotti = df["Prodotto"]
print(colonna_prodotti.head())
```
- On Your Own:
  1. Create a new table called dettagli_clienti containing only the columns Cliente_ID, Citta_Destinazione, and Metodo_Pagamento.
  2. Print the first 8 rows of the new dettagli_clienti table.

### Exercise 4: Sorting Data
- Objective: Sort the table based on column values, in either ascending or descending order.
- Guided Part:
```python
# Sorting by unit price from highest to lowest
df_ordinato = df.sort_values(by="Prezzo_Unitario", ascending=False)
print(df_ordinato[["Prodotto", "Prezzo_Unitario"]].head())
```
- On Your Own:
  1. Sort the dataset by the Quantita column from smallest to largest (ascending order).
  2. Sort the dataset alphabetically (from A to Z) based on the Citta_Destinazione column.

### Exercise 5: Filtering with a Single Condition
- Objective: Select only rows that meet a specific logical criterion.
- Guided Part:
```python
# Filtering to keep only PayPal orders
ordini_paypal = df[df["Metodo_Pagamento"] == "PayPal"]
print(ordini_paypal[["OrderID", "Metodo_Pagamento"]].head())
```
- On Your Own:
  1. Filter the dataset to show only orders from the "Laptop" category.
  2. Filter the dataset to select only orders where Quantita is greater than or equal to 2.

### Exercise 6: Filtering with Multiple Conditions
- Objective: Combine two logical conditions using the AND (&) and OR (|) operators.
- Guided Part:
```python
# Laptop category orders that cost less than 1200 euros
filtro_combinato = (df["Categoria"] == "Laptop") & (df["Prezzo_Unitario"] < 1200)
print(df[filtro_combinato][["Prodotto", "Prezzo_Unitario"]])
```
- On Your Own:
  1. Find all orders shipped to "Milano" or "Roma" using the OR operator (|).
  2. Find all orders paid with "Carta di Credito" that have a Sconto_Applicato greater than 0.05.

### Exercise 7: Handling Missing Values
- Objective: Find empty cells in the table and fill them with a default value.
- Guided Part:
```python
# Checking how many empty cells exist per column
print("Empty cells before cleaning:")
print(df.isnull().sum())

# Filling missing values in discount with 0.0
df["Sconto_Applicato"] = df["Sconto_Applicato"].fillna(0.0)
```
- On Your Own:
  1. Check the empty cell counts again with df.isnull().sum() to confirm that there are no more missing values in the discount column.
  2. Try creating a copy of the dataset and use the dropna() method to remove rows with empty cells directly. Check how many rows remain.

### Exercise 8: Creating New Columns
- Objective: Perform mathematical calculations between existing columns to generate new metrics and enrich the dataset.
- Guided Part:
```python
# Creating the gross revenue column by multiplying price by quantity
df["Fatturato_Lordo"] = df["Prezzo_Unitario"] * df["Quantita"]
print(df[["Prodotto", "Prezzo_Unitario", "Quantita", "Fatturato_Lordo"]].head())
```
- On Your Own:
  1. Create a new column called Valore_Sconto by multiplying Fatturato_Lordo by the Sconto_Applicato column.
  2. Create a column called Fatturato_Netto by subtracting Valore_Sconto from Fatturato_Lordo.

### Exercise 9: Value Counts and Frequencies
- Objective: Count how many times each item appears in a text column to discover the most common elements.
- Guided Part:
```python
# Counting the number of orders for each payment method
conteggio_pagamenti = df["Metodo_Pagamento"].value_counts()
print(conteggio_pagamenti)
```
- On Your Own:
  1. Use the value_counts() method on the Citta_Destinazione column to find out which city receives the highest number of orders.
  2. Use value_counts() on the Categoria column to see how many orders each product category received.

### Exercise 10: Grouping Data (groupby)
- Objective: Split data into categories and calculate sums or averages for each group.
- Guided Part:
```python
# Calculating total gross revenue for each category
fatturato_per_categoria = df.groupby("Categoria")["Fatturato_Lordo"].sum()
print(fatturato_per_categoria)
```
- On Your Own:
  1. Group the dataset by Metodo_Pagamento and calculate the average unit price using the mean() method.
  2. Group by Stato_Spedizione and calculate the total items sold (sum of the Quantita column).
