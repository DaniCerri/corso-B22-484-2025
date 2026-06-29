import random
random.seed(42)

class Libro:
    def __init__(self, titolo: str, autore: str, pagine: int) -> None:
        """
        Genera un codice randomico per il libro creato
        :param titolo:
        :param autore:
        :param pagine:
        """
        self.titolo = titolo
        self.autore = autore
        self.pagine = pagine
        self.codice = random.randint(100, 999)

    def descrizione(self):
        desc = f"[{self.codice}]: {self.titolo} - {self.autore} ({self.pagine} pag)"
        print(desc)  # Se la vogliamo stampare
        # return desc  # Se la vogliamo restituire

libro2 = Libro("Il piccolo principe", "Antoine", 547)
libro1 = Libro("Il signore degli anelli", "JRR Tolkien", 1200)

libro1.descrizione()
libro2.descrizione()
