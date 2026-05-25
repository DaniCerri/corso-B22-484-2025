"""
Ci sono 4 amici che hanno fatto una vacanza insieme.
Per semplificare hanno deciso che a turno (casuale) ognuno pagava un pasto/evento per tutti
e segnava l'importo speso da dividere alla romana (in parti uguali per tutto).

Adesso hanno un elenco di debiti e crediti che ognuno ha verso gli altri, l'obiettivo è calcolare
il numero minimo di transazioni necessari per appianare tutti i debiti.
"""
# Se il valore è POSITIVO: la persona è in CREDITO verso quell'amico
# Se il valore è NEGATIVO: la persona è in DEBITO verso quell'amico
dizionario_vacanza = {
    "Daniele": {
        "Luca": 17.90,    # Luca deve dare 17.90€ a Daniele (saldo di 30.20 - 12.30)
        "Giulia": -15.36, # Daniele deve dare 15.36€ a Giulia
        "Marco": -34.91   # Daniele deve dare 34.91€ a Marco
    },
    "Luca": {
        "Daniele": -17.90,
        "Giulia": 10.00,
        "Marco": -5.00
    },
    "Giulia": {
        "Daniele": 15.36,
        "Luca": -10.00,
        "Marco": 12.00
    },
    "Marco": {
        "Daniele": 34.91,
        "Luca": 5.00,
        "Giulia": -12.00
    }
}
# Primo obiettivo: Avere un dizionario con saldo di ciascuno (somma di debiti e crediti per ciascuno)
dizionario_saldi = {}
for persona, situazione in dizionario_vacanza.items():
    saldo = sum(situazione.values())
    dizionario_saldi[persona] = round(saldo, 2)  # Arrotonda il saldo a 2 cifre decimali

print(dizionario_saldi)
# dizionario_saldi = {persona: sum(situazione.values()) for persona, situazione in dizionario_vacanza.items()}
# Secondo obiettivo: Utilizzare il dizionario ottenuto nel primo punto per calcolare le transazioni
# IDEA: prendiamo volta per volta la persona con debito maggiore e credito maggiore e le accoppiamo per il saldo
#       procediamo finché il saldo di tutti è a 0

while True:
    peggior_debitore = min(dizionario_saldi, key=dizionario_saldi.get)
    # Questa riga cerca la chiave che dà come risultato di dizionario_saldi.get(chiave) il numero più piccolo
    # è come se l'elenco di coppie chiave-valore del dizionario venisse ordinate in senso crescente in base ai valori
    # e poi si prende il primo elemento
    # [
    #     ("Daniele", -32),
    #     ("Luca", 23),
    #     ...
    # ]
    miglior_creditore = max(dizionario_saldi, key=dizionario_saldi.get)

    # Controllo per uscire => Quando abbiamo saldato tutti, quanto vale il credito del migliore creditore?
    if abs(dizionario_saldi[peggior_debitore]) < 0.01 or abs(dizionario_saldi[miglior_creditore]) < 0.01:
        # se quelli che hanno peggior debito o miglior credito sono praticamente nulli, vuol dire che abbiamo finito
        # usciamo dal while
        break

    # Calcolare l'importo da trasferire
    importo_debito = dizionario_saldi[peggior_debitore]
    importo_credito = dizionario_saldi[miglior_creditore]

    importo_saldo = min(abs(importo_debito), importo_credito)

    # Stampare la transazione
    print(f"{peggior_debitore} -> {miglior_creditore}: {importo_saldo:.2f}")

    # Aggiornare il dizionario
    dizionario_saldi[peggior_debitore] = round(importo_debito + importo_saldo, 2)
    dizionario_saldi[miglior_creditore] = round(importo_credito - importo_saldo, 2)

print(dizionario_saldi)