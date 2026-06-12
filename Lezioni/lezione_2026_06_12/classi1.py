class Cane:
    # definiamo il metodo "costruttore"
    # Nome OBBLIGATORIO del costruttore
    def __init__(self, nome, data_nascita, razza):
        # Creiamo l'attributo nome nella classe (con il self) e ci mettiamo
        # il valore della variabile nome
        self.nome = nome
        self.data_nascita = data_nascita
        self.razza = razza
        self.fame = 50  # Valore di fame da 0 a 100

    def abbaia(self, numero):
        print(f'{self.nome}: {"bau " * numero}')

    def mangia(self, nutrimento):
        if self.fame - nutrimento <= 0:
            print(f"Il cane {self.nome} non vuole mangiare")
        else:
            self.fame -= nutrimento  # self.fame = self.fame - nutrimento
            print(f"Il cane {self.nome} ha mangiato")

    # SOVRASCRIVE il modo in cui python converte in stringa gli oggetti di
    # questa classe
    def __str__(self):
        return f"{self.nome}: {self.data_nascita} - {self.razza}"

    def __add__(self, other):
        razza = "Incrocio"
        if self.razza == other.razza:
            razza = self.razza

        # TODO: da migliorare sempre con la data di "oggi"
        return Cane(self.nome + other.nome, "12/06/2026", razza)

cane1 = Cane("Fido", "10/12/2024", "Husky")
cane2 = Cane("Maya", "29/06/2025", "Husky")
cane3 = Cane("Pippo", "18/01/2022", "Golden Retriever")

cane1.abbaia(7)
cane2.abbaia(3)
cane3.abbaia(10)

cane1.mangia(20)
cane1.mangia(25)
cane1.mangia(10)

print(cane1)
print(cane1 + cane2 + cane3)

