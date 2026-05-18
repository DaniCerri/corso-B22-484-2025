"""
Come abbiamo detto in python non è presente il costrutto "do-while"
Per raggiungere un comportamento simile, usiamo il costrutto while con un
paio di stratagemmi per modificarne il comportamento globale.

In questo esempio prendiamo un numero "scelta" che dovrà essere utilizzato
come scelta dell'utente di una opzione da eseguire da un elenco
"""
MAX_SCELTA = 3  # Numero di opzione massima disponibile
MIN_SCELTA = 1  # Numero di opzione minima disponibile

while True:  # Questo ciclo gira per sempre -> ...
    # Stampiamo il menu
    print("1. Inserisci due numeri e calcola la media")
    print("2. Inserisci 3 stringhe e stampale in CAPS LOCK")
    print("3. Inserisci un numero e calcolane il fattoriale")

    # Prendiamo la scelta in input
    scelta = int(input(f"Inserisci la tua scelta ({MIN_SCELTA}-{MAX_SCELTA}): "))

    if MIN_SCELTA <= scelta <= MAX_SCELTA:  # Se la scelta inserita è consentita
        # Usciamo dal while
        break

    # Se arriviamo a questa parte del while, vuol dire che la condizione di sopra
    # ha dato come esito "False"
    # Per questo non è necessario l'else
    print(f"Il numero inserito ({scelta}) non va bene, "
          f"deve essere tra {MIN_SCELTA} e {MAX_SCELTA} compresi")

print(f"Scelta finale inserita: {scelta}")
if scelta == 1:
    # Inserimento dei numeri e calcolo della media
    numeri = input("Inserisci i due numeri di cui calcolare la media (N1 N2): ").split(" ")

    # numero1, numero2 = [float(numero) for numero in numeri]
    # media = (numero1 + numero2) / 2

    # media =  sum(float(numero) for numero in numeri) / 2

    numeri = [float(numero) for numero in numeri]
    media = (numeri[0] + numeri[1]) / 2
    print(f"Media: {media:.2f}")

elif scelta == 2:
    # Prendiamo 3 stringhe e le stampiamo maiuscole
    stringhe = input("Inserisci le tue stringhe separate da ';': ").split(";")
    # stringhe = [stringa.upper() for stringa in stringhe]
    for stringa in stringhe:
        print(f" * {stringa.upper()}")

elif scelta == 3:
    # Prendiamo in input un numero (intero) e calcoliamo il fattoriale
    # Il numero deve essere >= 0
    while True:
        numero = int(input("Inserisci il numero: "))
        if numero >= 0:
            break
        print("Per calcolare un fattoriale, serve un numero maggiore o uguale a 0")

    # 0! = 1
    totale = 1  # Inizializziamo il totale a 1 così da poterlo aggiornare man mano
    # con le moltiplicazioni e coprire già il caso in cui il numero è 0 o 1
    while numero > 1:
        totale *= numero
        numero -= 1

    # totale = 1  # Inizializziamo il totale a 1 così da poterlo aggiornare man mano
    # # con le moltiplicazioni e coprire già il caso in cui il numero è 0 o 1
    # for n in range(numero):
    #     totale *= (n + 1)


