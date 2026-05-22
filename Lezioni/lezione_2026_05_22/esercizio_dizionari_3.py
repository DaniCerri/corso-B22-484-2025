"""
Prendiamo un testo (una stringa) e facciamo un dizionario
che conti ogni carattere quante volte compare

Non facciamolo case sensitive -> A = a etc
"""

stringa = "Ciao come state? Tutto bene?"
dizionario_caratteri = {}

# Per ogni carattere nella stringa
for carattere in stringa.lower():
    # Vogliamo fare in modo che il dizionario abbia la coppia carattere: conteggio
    # Ci sono due possibilità:
    #    1. abbiamo nel dizionario già la coppia carattere: conteggio
    #        -> Vuol dire che eseguendo il for abbiamo già incontrato almeno una volta il carattere
    #        -> Dobbiamo incrementare di 1 il contatore
    #    2. non abbiamo ancora visto questo carattere
    #        -> Creiamo la nuova coppia nel dizionario
    #        -> Il contatore va messo a 1 (la prima, e finora unica, volta in cui abbiamo trovato il carattere)

    # Questa riga prova a prendere il valore nel dizionario che ha chiave il carattere attuale
    # Se non lo trova, restituisce 0
    conteggio = dizionario_caratteri.get(carattere, 0) + 1

    # if carattere not in dizionario_caratteri.keys():
    #     conteggio = 0 + 1
    # else:
    #     conteggio = dizionario_caratteri[carattere] + 1z

    # con la riga sotto creiamo la coppia carattere conteggio se non c'era, altrimenti la aggiorniamo
    dizionario_caratteri[carattere] = conteggio

# Vogliamo ottenere un dizionario che avrà come chiavi i caratteri e come valori i conteggio
print(dizionario_caratteri)

