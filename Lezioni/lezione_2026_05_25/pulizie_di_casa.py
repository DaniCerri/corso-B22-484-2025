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

