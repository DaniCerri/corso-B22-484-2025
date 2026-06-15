class Frazione:
    def __init__(self, numeratore: int, denominatore: int):
        self.numeratore = numeratore
        self.denominatore = denominatore

    def valuta(self):
        """
        Restituisce il valore float della funzione, se si può.
        Se il denominatore è 0 e il numeratore no -> Restituisce "+/- inf"
        Se sono entrambi 0 -> Restituisce "nan"
        :return: valutazione della funzione
        """
        if self.denominatore == 0 and self.numeratore == 0:
            return "nan"
        elif self.denominatore == 0:
            segno = "+"
            if self.numeratore < 0:
                segno = "-"

            return f"{segno} inf"

        return self.numeratore / self.denominatore

    # Andiamo a definire il comportamento che questa classe
    # ha con l'operatore somma
    def __add__(self, other):
        # Regole da rispettare:
        # 1. La somma di due infiniti uguali dà inf di segno concorde
        #   --> + inf + + inf = + inf
        #   --> - inf + - inf = - inf
        # 2. La somma di due infiniti discordi dà nan
        # 3. Numero + (+/-) inf dà (+/-) inf
        # 4. se c'è almeno un nan dà nan
        # 5. se non c'è una regola di sopra che si applica,
        #    basta fare la somma classica
        print("self", self.numeratore, self.denominatore)
        print("other", other.numeratore, other.denominatore)
        if self.valuta() == "nan" or other.valuta() == "nan":
            return "nan"

        valutazione_self = str(self.valuta())
        valutazione_other = str(other.valuta())

        minore = min(valutazione_self, valutazione_other)
        maggiore = max(valutazione_self, valutazione_other)

        if minore == "+ inf" and maggiore == "- inf":
            return "nan"
        elif minore == maggiore and "inf" in minore:
            return minore
        elif "inf" in minore:
            return minore

        numeratore = (self.numeratore * other.denominatore
                      + self.denominatore * other.numeratore)
        denominatore = self.denominatore * other.denominatore
        return Frazione(numeratore, denominatore)

if __name__ == "__main__":
    fraz1 = Frazione(5, 0)
    fraz2 = Frazione(7, 3)
    fraz3 = Frazione(4, 5)
    print(fraz1.valuta())
    print(fraz2.valuta())
    print(fraz3.valuta())
    print(fraz1 + fraz2)






