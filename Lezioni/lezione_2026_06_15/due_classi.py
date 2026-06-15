class Scaler:
    def __init__(self, minimo, massimo):
        self.minimo = minimo
        self.massimo = massimo
        self.numero_minimo = None
        self.numero_massimo = None

    def fit(self, dati):
        # Troviamo il massimo e il minimo dei dati,
        # e salviamo questi valori negli attributi
        self.numero_massimo = max(dati)
        self.numero_minimo = min(dati)

    def transform(self, dati):
        # Con "assert" obblighiamo l'espressione logica che lo segue ad essere vera,
        # altrimenti si solleva un errore che può essere chiarito con una stringa dopo
        # l'espressione logica
        assert (self.numero_massimo is not None
                and self.numero_minimo is not None), "Prima di transform bisogna chiamare fit"

        dati_scalati = [(p - self.numero_minimo) /
                        (self.numero_massimo - self.numero_minimo)
                        * (self.massimo - self.minimo) + self.minimo for p in dati]
        return dati_scalati

    def fit_transform(self, dati):
        self.fit(dati)
        return self.transform(dati)

class Stack:
    ...

lista = [1, 2, 0, 12, 2, 9, 29]
lista2 = [64, 32, -1, -10]
scaler = Scaler(-1, 1)
scaler.fit(lista)
scalati = scaler.transform(lista)
print([f"{scalato:.2f}" for scalato in scalati])
print(scaler.transform(lista2))
print(scaler.fit_transform(lista2))
