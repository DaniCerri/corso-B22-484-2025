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
