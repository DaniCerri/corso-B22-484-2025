"""
Abbiamo invitato a cena n persone per mangiare la carbonara.
Abbiamo la ricetta che prevede a persona
  * 100g di pasta
  * 50g di guanciale
  * 1 tuorlo
  * 20g di pecorino

Superati i 200g di pecorino, non ne possiamo più aggiungere per questioni
strumentali (non ci sta nella ciotola più grande di casa)

Abbiamo anche una dispensa da cui prendere la roba e dobbiamo fare la
lista di cose che mancano da prendere al supermercato.

L'obiettivo è avere la lista della spesa e la ricetta completa
"""
def adatta_ricetta(ricetta_a_persona, n_persone):
    for ingrediente, quantita in ricetta_a_persona.items():
        quantita *= n_persone
        if ingrediente == "pecorino":
            quantita = min(quantita, 200)
        ricetta_a_persona[ingrediente] = quantita * n_persone


# Ricetta per persona
ricetta = {
    "pasta": 100, # g
    "guanciale": 50, #g
    "tuorlo": 1, # pz
    "pecorino": 20 # g
}

dispensa = {
    "pasta": 450, # g
    "guanciale": 100, #g
    "tuorlo": 7, # pz
    "pecorino": 0 # g
}

n = 10