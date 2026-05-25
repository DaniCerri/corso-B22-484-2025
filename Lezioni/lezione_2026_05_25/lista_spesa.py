"""
Vogliamo fare un calcolatore per la nostra lista della spesa.
Abbiamo a disposizione un dizionario con articoli e prezzi del supermecato.
Abbiamo inoltre la nostra lista con dentro gli articoli da comprare.

L'obiettivo è fare uno script che dato un budget ci dica quali elementi possiamo comprare e
quali no (per motivi di budget o perchè non ci sono al supermercato).
Stampiamo anche il totale complessivo
"""
listino_prezzi = {
    # nome-articolo: prezzo unitario
    "pane": 1.5,  # 1 kg di pane
    "latte": 1.2,  # 1 L di latte
    "yogurt": 2.99,  # 1 confezione da 250g
    "cioccolato": 1.80,  # 1 tavoletta 100g
    "pasta": 0.85,  # 1 confezione da 500g
    "mele": 2.20,  # 1 kg di mele
    "caffè": 3.5,  # confezione da 500g di caffè
    "pomodori": 2.0,   # 1 kg di pomodori
}

lista_spesa = [
    {"articolo": "pasta", "quantita": 3}, # 3 confezioni
    {"articolo": "avocado", "quantita": 5},  # 5 avocado
    {"articolo": "mele", "quantita": 0.5},  # 0.5 kg
    {"articolo": "pane", "quantita": 1.2},  # 1.2 kg
    {"articolo": "yogurt", "quantita": 2},  # 2 confezioni
    {"articolo": "pomodori", "quantita": 1.4},  # 1.4 kg
]

# budget = float(input("Inserisci il tuo budget: "))  # €
budget = 5.0 # €

totale = 0

for elemento in lista_spesa:
    articolo = elemento['articolo']
    quantita = elemento['quantita']

    # versione 1
    # Cerchiamo di prendere il prezzo dell'articolo
    # se l'articolo non è presente nel dizionario listino_prezzi, allora
    # lo impostiamo a None così da poter controllare subito dopo
    # prezzo_unitario = listino_prezzi.get(articolo, None)
    #
    # # Se il prezzo è None, vuol dire che l'articolo non è presente
    # if not prezzo_unitario:
    #     # stampiamo l'errore
    #     print(f"Articolo: {articolo} non presente nel listino")
    #     # passiamo al prossimo elemento nella lista
    #     continue

    # versione 2
    # prima controlli che l'articolo che vuoi comprare sia nelle chiavi, altrimenti passi al
    # prossimo articolo
    if articolo not in listino_prezzi.keys():
        # stampiamo l'errore
        print(f"Articolo: {articolo} non presente nel listino")
        # passiamo al prossimo elemento nella lista
        continue

    # Se arriviamo qua, siamo certi che l'articolo sia nel listino prezzi, altrimenti
    # avremmo fatto il continue subito prima e saremmo passati all'articolo successivo
    prezzo_unitario = listino_prezzi[articolo]

    # Se arriviamo qua sotto, vuol dire che non siamo entrati nell'if, quindi abbiamo il prezzo
    costo_totale = prezzo_unitario * quantita

    # Controlliamo di poterci permettere di comprare l'articolo
    if costo_totale + totale <= budget:
        totale += costo_totale
        print(f"  - {articolo} * {quantita} aggiunto: {costo_totale:.2f} €")

print(f"Costo spesa totale: {totale:.2f} €")


# TODO: BONUS si può fare anche una versione che se c'è poco budget
#  prenda meno elementi dell'ultimo articolo
#  posso prendere ad esempio 0.8/1.4 kg di pomodori oppure 1/3 confezioni di pasta

# TODO: BONUS BONUS: si può fare che utilizzi l'ultimo elemento frazionabile per riempire
#  il carrello fino alla fine del budget

