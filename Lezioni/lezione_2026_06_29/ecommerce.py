# Classe che rappresenta un singolo prodotto in vendita.
class Prodotto:
    # Costruttore: viene eseguito alla creazione dell'oggetto (es. Prodotto("Mele", 10.12)).
    # I type hint (str, float) indicano il tipo atteso ma non sono vincolanti in Python.
    def __init__(self, nome: str, prezzo: float):
        self.nome = nome      # attributo di istanza: nome del prodotto
        self.prezzo = prezzo  # attributo di istanza: prezzo del prodotto

    # __str__ definisce come l'oggetto viene mostrato con print() o str().
    # :.2f formatta il prezzo con esattamente 2 cifre decimali (es. 10.12 €).
    def __str__(self):
        return f"{self.nome} {self.prezzo:.2f} €"

# Classe che rappresenta il carrello: contiene una lista di oggetti Prodotto.
class Carrello:
    # Ogni carrello parte vuoto. La lista è un attributo di istanza:
    # ogni Carrello ha la propria lista, separata dagli altri.
    def __init__(self):
        self.prodotti: list[Prodotto] = []

    # Aggiunge un prodotto in coda alla lista con append().
    def aggiungi_prodotto(self, prodotto: Prodotto):
        self.prodotti.append(prodotto)

    # Rimuove il primo prodotto con il nome dato.
    # enumerate() fornisce sia l'indice i che il prodotto a ogni giro.
    def rimuovi_prodotto(self, nome: str):
        for i, prodotto in enumerate(self.prodotti):
            if prodotto.nome == nome:
                return self.prodotti.pop(i)  # pop(i) rimuove e restituisce l'elemento trovato

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
        if not self.prodotti:        # lista vuota → "Carrello vuoto"
            return "Carrello vuoto"

        # Costruzione della stringa riga per riga concatenando con +=.
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

print(carrello)  # mostra i 3 prodotti e il totale

carrello.rimuovi_prodotto("Mele")  # rimuove le Mele

print(carrello)  # restano Pere e Banane
