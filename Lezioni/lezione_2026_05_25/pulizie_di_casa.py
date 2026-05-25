"""
Ci sono quattro coinquilini che devono pulire casa a turno
Per varie questioni capita che alcuni turni si scambino e quindi che qualcuno pulisca più degli altri
Vogliamo un programma che ci dica
  * quante volte ogni persona ha pulito in totale
  * quante volte una certa stanza è stata pulita

Sulla base di queste informazioni ci dica chi deve pulire la prossima volta e quale stanza
"""
diz_pulizie = {
    "Chiara": {"Cucina": 8, "Bagno": 3, "Salotto": 4},
    "Matteo": {"Cucina": 2, "Bagno": 1, "Salotto": 2},
    "Sofia": {"Cucina": 5, "Bagno": 6, "Salotto": 4},
    "Marco": {"Cucina": 3, "Bagno": 4, "Salotto": 5},
}

pulizie_totali_persona = {}
pulizie_totali_stanza = {}

for persona, pulizie in diz_pulizie.items():
    # Riempiamo il primo dizionario
    somma = sum(pulizie.values())
    pulizie_totali_persona[persona] = somma
    print(f"  * {persona} ha pulito {somma} volte")

    # Riempiamo il secondo dizionario
    for stanza, n_volte in pulizie.items():
        contatore = pulizie_totali_stanza.get(stanza, 0) + n_volte
        pulizie_totali_stanza[stanza] = contatore

print(pulizie_totali_stanza)

n_prossime_pulizie = 30

for i in range(n_prossime_pulizie):
    peggior_pulitore = min(pulizie_totali_persona, key=pulizie_totali_persona.get)
    stanza_meno_pulita = min(pulizie_totali_stanza, key=pulizie_totali_stanza.get)

    print(f"{i + 1}. {peggior_pulitore} deve pulire {stanza_meno_pulita}")

    pulizie_totali_persona[peggior_pulitore] += 1
    pulizie_totali_stanza[stanza_meno_pulita] += 1


