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
budget = 10.2 # €

# TODO: BONUS si può fare anche una versione che se c'è poco budget
#  prenda meno elementi dell'ultimo articolo
#  posso prendere ad esempio 0.8/1.4 kg di pomodori oppure 1/3 confezioni di pasta

# TODO: BONUS BONUS: si può fare che utilizzi l'ultimo elemento frazionabile per riempire
#  il carrello fino alla fine del budget

