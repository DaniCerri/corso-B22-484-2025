"""
Abbiamo un'orario in secondi e dobbiamo capire a che ora del giorno (hh:mm:ss) corrisponde
"""
# orario = int(input("Inserisci l'orario: "))
orario = 129382

ore = orario // 3600

orario -= ore * 3600  # orario = orario - ore * 3600

minuti = orario // 60

secondi = orario - minuti * 60

ore %= 24  # ore = ore % 24
# ...


print(f"Orario del giorno: {ore:02d}:{minuti:02d}:{secondi:02d}")
