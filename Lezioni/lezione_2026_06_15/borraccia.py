class Borraccia:
    # Metodo costruttore -> prende i parametri dall'esterno e li
    # inserisce negli attributi della classe
    def __init__(self, volume: float, colore: str, materiale: str, isolamento: float):
        # Definiamo un attributo volume per la classe e gli assegnamo il valore
        # preso dall'esterno nel parametro "volume" del costruttore
        self.volume = volume

        # Replichiamo con gli altri attributi
        self.colore = colore
        self.materiale = materiale
        self.isolamento = isolamento

        # Inizializziamo anche il volume occupato della borraccia
        self.volume_occupato = 0  # Appena creata la borraccia è vuota

    def svuota_borraccia(self, volume_da_svuotare: float) -> float:
        """
        Preso un volume di liquido da togliere, se si può, lo toglie dalla borraccia,
        altrimenti la svuota finchè si può. Se è vuota restituisce -1, altrimenti il volume
        rimanente
        :param volume_da_svuotare: Volume di liquido da togliere
        :return: volume rimanente
        """
        # Nota: Prima le condizioni di uscita "prematura"
        if self.volume_occupato == 0:
            return -1

        rimanente = self.volume_occupato - volume_da_svuotare
        self.volume_occupato = max(rimanente, 0)
        return self.volume_occupato

    def riempi_borraccia(self, volume_da_riempire: float) -> float:
        """
        Preso un volume di liquido da aggiungere, se si può, lo aggiungere dalla borraccia,
        altrimenti la riempie finchè si può. Se è piena restituisce -1, altrimenti il volume
        libero rimanente
        :param volume_da_riempire: Volume di liquido da aggiungere
        :return: volume libero rimanente
        """
        if self.volume_occupato == self.volume:
            return -1

        self.volume_occupato = min(self.volume_occupato + volume_da_riempire, self.volume)
        return self.volume - self.volume_occupato

    # COn questo metodo andiamo a specificare all'interprete come vogliamo
    # che venga fatta la conversione in stringa degli oggetti della nostra classe
    def __str__(self):
        return (f"Borraccia {self.colore}-{self.materiale} "
                f"Volume: {self.volume_occupato:.2f}/{self.volume:.2f}")

if __name__ == "__main__":
    borraccia1 = Borraccia(1.0, "Grigio", "Alluminio", 10)
    borraccia2 = Borraccia(.7, "Rosso", "Plastica", 2)

    print(borraccia1)
    print(borraccia2)

    borraccia1.riempi_borraccia(2.0)
    borraccia2.riempi_borraccia(0.5)

    print(borraccia1)
    print(borraccia2)

    borraccia1.svuota_borraccia(0.5)
    borraccia2.svuota_borraccia(0.9)

    print(borraccia1)
    print(borraccia2)



