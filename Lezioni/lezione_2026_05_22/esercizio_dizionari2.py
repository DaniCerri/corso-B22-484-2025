"""
Gestiamo una gelateria e abbiamo un dizionario con i gusti
All'interno del dizionario salviamo come chiave i nomi dei gusti e come
valori un nuovo dizionario con parametri prezzo (al kg) e quantità (kg)

Simuliamo una giornata lavorativa, riceviamo dei clienti e ne gestiamo gli ordini
"""
dizionario_gusti = {
    "Cioccolato": {
        "prezzo": 16,
        "quantita": 0.7
    },
    "Fragola": {
        "prezzo": 19,
        "quantita": 1.2
    },
    "Pistacchio": {
        "prezzo": 24,
        "quantita": 0.3
    },
    "Limone": {
        "prezzo": 18,
        "quantita": 0.8
    },
    "Fiordilatte": {
        "prezzo": 12,
        "quantita": 2.0
    }
}

while True:
    for chiave, valore in dizionario_gusti.items():
        print(f"{chiave}")
        print(f"  Prezzo del gusto {chiave}: {valore['prezzo']:.2f} €/kg")
        print(f"  Quantità del gusto {chiave}: {valore['quantita']:.2f} kg")
        print("-" * 60)

    gusto_scelto = input("Inserisci quale gusto vuoi: ")

    # 1. controlliamo se il gusto inserito è presente
    # passiamo direttamente al prossimo ciclo con la keyword "continue"
    if "il gusto non c'è":
        continue


