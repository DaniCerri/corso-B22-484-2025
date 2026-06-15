"""
Data una borraccia all'utente, fare un menu che consenta di riempire e
svuotare la borraccia, finchè l'utente non decide di uscire (codice 0)
"""
import borraccia as brc

def input_numero(minimo: int | float, massimo: int | float, messaggio: str) -> int | float:
    while True:
        numero = float(input(messaggio))
        if minimo <= numero <= massimo:
            return numero
        print(f"Il numero inserito non rispetta il range {minimo} - {massimo}")

borraccia1 = brc.Borraccia(
    1.0,
    "rosso",
    "alluminio",
    10
)

while True:
    # 1. stampiamo il menu
    print("0. Esci")
    print("1. Inserisci liquido nella borraccia")
    print("2. Togli liquido dalla borraccia")

    # 2. prendiamo l'input
    scelta = input_numero(0, 2, "Inserisci la tua scelta: ")

    if scelta == 0:
        print("Uscita")
        break
    elif scelta == 1:
        volume_da_inserire = input_numero(
        0,
               borraccia1.volume,
     "Inserisci il volume da aggiungere: "
        )
        v_libero = borraccia1.riempi_borraccia(volume_da_inserire)
        if v_libero == -1:
            print("La borraccia era già piena")
        else:
            print(f"Volume libero rimasto: {v_libero:.2f}")