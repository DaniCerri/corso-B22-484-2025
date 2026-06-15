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







