"""
Una nuova struttura dati che ci consente di memorizzare un elenco di informazioni (come le liste e tuple)
MA ha due differenze principali:
  1. Gli elementi dentro i dizionari NON sono ordinati
  2. Siccome gli elementi non hanno ordine non possiamo identificarli con la loro posizione
     Per identificare un elemento si usa la "chiave"

===> I dizionari sono elenchi di coppie chiave-valore

Una chiave in python ha delle restrizioni:
    1. può essere solamente di tipo stringa o numero (meglio intero)
    2. non ci possono essere due chiavi duplicate nello stesso dizionario
"""

dizionario_prova = {
    "nome": "Daniele",
    "linguaggi": ["Python", "C++", "Javascript"],
    "anni_eseperienza": 6,
}

# Nei dizionari al posto dell'indice, per ottenere un certo elemento, mettiamo la sua chiave
print(dizionario_prova['nome'])

# Per ottenere l'elenco di chiavi si usa
print(list(dizionario_prova.keys()))  # il metodo .keys() non dà una lista
# NON facciamo cose tipo -> list(dizionario_prova.keys())[0]

# Per ottenere l'elenco di valori si usa
print(dizionario_prova.values())

# Possiamo sfruttare il metodo .item() per ottenere le coppie chiave-valore per un for
for chiave, valore in dizionario_prova.items():
    print(f"{chiave} -> {valore}")

# Per aggiungere una nuova coppia chiave-valore base usare
dizionario_prova['CHIAVE_NUOVA'] = "VALORE NUOVO"
print(dizionario_prova)



