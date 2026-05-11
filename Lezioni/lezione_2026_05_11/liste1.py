lista_esempio = [6, 3, 0, 10, 29, 28, 12, 5]  # Con le quadre dichiariamo una lista
tupla_esempio = (4, 5, 7, 9, 45)  # Con le tonde dichiariamo una tupla

# Per sapere quanti elementi ci sono in una lista/tupla usiamo la funzione len()
print(f"Lista: {lista_esempio}, Lunghezza: {len(lista_esempio)}")
print(f"Tupla: {tupla_esempio}, Lunghezza: {len(tupla_esempio)}")

indice = 3  # ----> Otteniamo il quarto elemento. L'indice deve essere intero
# Per ottenere l'elemento a un certo indice di una lista/tupla, usiamo la sintassi
# lista/tupla[indice]
print(f"Elemento di indice {indice} della lista: {lista_esempio[indice]}")
print(f"Elemento di indice {indice} della tupla: {tupla_esempio[indice]}")

# In python è facile ottenere una sottosequenza di una lista/tupla
# la sintassi prevede di usare lista/tupla[indice_inizio:indice_fine]
# NB: l'indice_inizio è sempre compreso, l'indice_fine NO
i_inizio = 1
i_fine = 4
print(f"Lista da {i_inizio} a {i_fine}: {lista_esempio[i_inizio:i_fine]}")
print(f"Tupla da {i_inizio} a {i_fine}: {tupla_esempio[i_inizio:i_fine]}")

# Se la prima posizione è vuota, si parte dal primo elemento
# Se l'ultima posizione è vuota, si arriva fino all'ultimo (compreso)
print(f"Lista da inizio a {i_fine}: {lista_esempio[:i_fine]}")
print(f"Lista da {i_inizio} a fine: {lista_esempio[i_inizio:]}")

# Modifichiamo un elemento della lista
lista_esempio[5] = 290  # Assegnamo il valore 290 al sesto elemento della lista
print(f"Lista aggiornata: {lista_esempio}")
# NB: Non possiamo fare la stessa cosa con la tupla, darebbe errore

# Aggiungiamo un elemento alla lista
lista_esempio.append(999)  # Aggiungiamo al fondo della lista il numero 999
print(f"Lista aggiornata: {lista_esempio}")








