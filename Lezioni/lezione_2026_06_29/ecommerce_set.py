# ============================================================
# I SET (insiemi)
# ------------------------------------------------------------
# Un set è una collezione di elementi con due caratteristiche chiave:
#   1) NON ammette duplicati: aggiungere due volte lo stesso elemento
#      non ha effetto, ne resta una sola copia.
#   2) NON è ordinato: gli elementi non hanno una posizione/indice,
#      quindi NON si può fare prodotti[0] come con le liste.
# Si crea con set() (vuoto) oppure con le graffe: {1, 2, 3}.
# Metodi principali: add() per aggiungere, remove() per togliere.
# Vantaggio: la verifica "x è dentro?" e la rimozione sono molto veloci.
# Differenza con ecommerce.py: lì il carrello usava una list (ordinata,
# con duplicati e indici); qui usa un set.
# ============================================================

# Classe che rappresenta un singolo prodotto in vendita.
class Prodotto:
    # Costruttore: eseguito alla creazione dell'oggetto (es. Prodotto("Mele", 10.12)).
    # I type hint (str, float) indicano il tipo atteso ma non sono vincolanti in Python.
    def __init__(self, nome: str, prezzo: float):
        self.nome = nome      # attributo di istanza: nome del prodotto
        self.prezzo = prezzo  # attributo di istanza: prezzo del prodotto

    # __str__ definisce come l'oggetto viene mostrato con print() o str().
    # :.2f formatta il prezzo con esattamente 2 cifre decimali (es. 10.12 €).
    def __str__(self):
        return f"{self.nome} {self.prezzo:.2f} €"

# Classe che rappresenta il carrello: contiene un set di oggetti Prodotto.
class Carrello:
    # Ogni carrello parte vuoto. set() crea un insieme vuoto.
    # ATTENZIONE: {} crea un dizionario vuoto, NON un set: per il set vuoto
    # serve obbligatoriamente set().
    def __init__(self):
        self.prodotti: set[Prodotto] = set()

    # Aggiunge un prodotto con add() (nei set si usa add, non append).
    # Se il prodotto fosse già presente, il set lo ignorerebbe (niente duplicati).
    def aggiungi_prodotto(self, prodotto: Prodotto):
        self.prodotti.add(prodotto)

    # Rimuove il primo prodotto con il nome dato.
    # Si scorre il set con un for (senza indici, perché il set non è ordinato).
    def rimuovi_prodotto(self, nome: str):
        for prodotto in self.prodotti:
            if prodotto.nome == nome:
                self.prodotti.remove(prodotto)  # remove() toglie l'elemento dal set
                return prodotto                 # restituisce il prodotto rimosso

        return -1  # nessun prodotto trovato con quel nome

    # Somma i prezzi di tutti i prodotti nel carrello.
    def calcola_totale(self):
        tot = 0
        for prodotto in self.prodotti:
            tot += prodotto.prezzo

        return tot

    # Applica uno sconto al totale. percentuale è in forma decimale: 0.2 = 20%.
    # (1 - percentuale) è la frazione di prezzo da pagare (es. 0.8 = 80%).
    def applica_sconto(self, percentuale: float):
        return self.calcola_totale() * (1 - percentuale)

    # Rappresentazione testuale del carrello, usata da print().
    def __str__(self):
        if not self.prodotti:        # set vuoto → "Carrello vuoto"
            return "Carrello vuoto"

        # Costruzione della stringa riga per riga concatenando con +=.
        # Nota: scorrendo un set l'ordine dei prodotti non è garantito.
        out = "=" * 20 + " CARRELLO " + "=" * 20 + "\n"  # "=" * 20 ripete il carattere 20 volte
        for prodotto in self.prodotti:
            out += f" * {prodotto}\n"   # usa __str__ di Prodotto per ogni riga
        out += "_" * 50 + "\n"
        out += f"Totale: {self.calcola_totale()}\n"
        out += "=" * 50 + "\n"

        return out

# --- Programma di prova ---

# Creazione di tre oggetti Prodotto.
p1 = Prodotto("Mele", 10.12)
p2 = Prodotto("Pere", 7.22)
p3 = Prodotto("Banane", 8.37)

carrello = Carrello()
print(carrello)  # ancora vuoto → "Carrello vuoto"

# Aggiunta dei prodotti al carrello.
carrello.aggiungi_prodotto(p1)
carrello.aggiungi_prodotto(p2)
carrello.aggiungi_prodotto(p3)

print(carrello)  # mostra i 3 prodotti (in ordine non garantito) e il totale

carrello.rimuovi_prodotto("Mele")  # rimuove le Mele

print(carrello)  # restano Pere e Banane
