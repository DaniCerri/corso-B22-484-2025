piove = True
sono_in_ritardo = False

# Condizione: Se piove E sono in ritardo, allora prendo la macchina
print(piove and sono_in_ritardo)

# Condizione: Se non piove E non sono in ritardo, allora prendo la macchina
print(not piove and not sono_in_ritardo)
print(not (piove or sono_in_ritardo))
print(not (piove and sono_in_ritardo))

orario = 17
ore_di_lezione = 2

print(not orario > 16 and not ore_di_lezione >= 1)
print(not(orario > 16 or ore_di_lezione >= 1))
