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
