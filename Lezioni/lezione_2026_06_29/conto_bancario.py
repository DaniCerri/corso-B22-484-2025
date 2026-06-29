class ContoBancario:
    def __init__(self, titolare: str):
        self.titolare = titolare
        self.__saldo = 0

    # Primo metodo "SETTER" -> ci permette di aggiornare il saldo secondo
    # le nostre "regole di business"
    def deposita(self, importo: float) -> float:
        assert importo > 0, "Non si può depositare una cifra <= 0"
        self.__saldo += importo
        # Per comodità di chi chiama il metodo, restituiamo il saldo
        # aggiornato
        return self.__saldo

    def preleva(self, importo: float) -> float:
        assert importo > 0, "Non si può prelevare una cifra <= 0"
        if self.__saldo <  importo:
            return -1

        self.__saldo -= importo
        # Per comodità di chi chiama il metodo, restituiamo il saldo
        # aggiornato
        return self.__saldo

    def mostra_saldo(self):
        print(f"Saldo attuale: {self.__saldo}")

    def get_saldo(self):
        return self.__saldo

    def __str__(self):
        return f"{self.titolare}: {self.__saldo:.2f} €"

conto = ContoBancario("Daniele Cerrina")
print(conto)

conto.deposita(100)
print(conto)

conto.preleva(10)
print(conto)

# vogliamo dimezzare il conto
valore = conto.get_saldo()
importo_da_togliere = valore / 2
conto.preleva(importo_da_togliere)
print(conto)

conto.deposita(-10)
