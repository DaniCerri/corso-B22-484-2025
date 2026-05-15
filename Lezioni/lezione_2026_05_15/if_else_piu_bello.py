"""
Vogliamo scrivere un semplice script che decida se vendere o no
un alcolico a un cliente
Regole:
    * Non si vendono alcolici a chi ha meno di 18 anni
    * Non si vendono alcolici dopo le 21:30
"""
eta = int(input("Inserisci la tua età: "))
orario_raw = input("Inserisci l'orario (hh:mm): ")
orario = orario_raw.split(":")  # [int(a) for a in orario_raw.split(":")]
orario[0] = int(orario[0])
orario[1] = int(orario[1])

orario_limite = 21 * 60 + 30  # 21:30
orario_minimo = 8 * 60 + 0  # 08:00
orario_inserito = orario[0] * 60 + orario[1]
if eta >= 18 and orario_minimo < orario_inserito < orario_limite:
    print("Serviamo alcolici")
elif eta < 18:
    print("Non serviamo alcolici ai minorenni")
else:
    print("Non serviamo alcolici dopo le 21")
