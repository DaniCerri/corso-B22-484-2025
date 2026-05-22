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
    # Usiamo il for SOLAMENTE per stampare il menu
    for chiave, valore in dizionario_gusti.items():
        print(f"{chiave}")
        print(f"  Prezzo del gusto {chiave}: {valore['prezzo']:.2f} €/kg")
        print(f"  Quantità del gusto {chiave}: {valore['quantita']:.2f} kg")
        print("-" * 60)

        # Tornando a sinistra, il for si è concluso
    gusto_scelto = input("Inserisci quale gusto vuoi: ")

    # 1. controlliamo se il gusto inserito è presente
    # passiamo direttamente al prossimo ciclo con la keyword "continue"
    if gusto_scelto not in dizionario_gusti.keys():
        print("Non hai selezionato un gusto tra quelli presenti")
        continue

    # Se abbiamo fatto il continue questo blocco per il giro corrente verrà saltato
    # 2. Per il gusto selezionato facciamo inserire la quantità
    while True:
        quantita = float(input(f"Inserisci la quantità di {gusto_scelto} "
                               f"(0 - {dizionario_gusti[gusto_scelto]['quantita']} kg): "))
        if 0 < quantita <= dizionario_gusti[gusto_scelto]['quantita']:
            break
        print("Non c'è abbastanza gelato, seleziona una quantità minore")

    # 3. Togliamo dalla quantità del gusto quella comprata
    dizionario_gusti[gusto_scelto]['quantita'] -= quantita

    # 4. Stampiamo al cliente quanto deve pagare
    prezzo = quantita * dizionario_gusti[gusto_scelto]['prezzo']
    print(f"Prezzo da pagare: {prezzo:.2f} €")

    print()
    print()

# TODO: Facciamo in modo che se di un gusto la quantità è 0, non lo stampi nel menu