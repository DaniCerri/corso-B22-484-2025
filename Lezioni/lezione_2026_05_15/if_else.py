"""
Vogliamo scrivere un semplice script che decida se vendere o no
un alcolico a un cliente
Regole:
    * Non si vendono alcolici a chi ha meno di 18 anni
    * Non si vendono alcolici dopo le 21:00
"""
eta = int(input("Inserisci la tua età: "))
orario = int(input("Inserisci l'orario (es: 21, 22, 18): "))

if eta >= 18 and orario < 21:
    print("Serviamo alcolici")
elif eta < 18:
    print("Non serviamo alcolici ai minorenni")
else:
    print("Non serviamo alcolici dopo le 21")