"""
vogliamo fare un calcolatore di interessi
Sappiamo che abbiamo un capitale iniziale di 100€
e abbiamo un interesse annuo del 4%

Quanto abbiamo di capitale dopo 3 anni?
ATTENZIONE: 4% all'anno in 3 anni NON è il 12%
"""
capitale = 100
tasso = 0.04

# Anno 1
# capitale = capitale * (1 + tasso)  ---> Fa esattamente ciò che c'è sotto
capitale *= (1 + tasso)
print(f"Capitale dopo 1 anno: {capitale}")

# Anno 2
capitale *= (1 + tasso)
print(f"Capitale dopo 2 anni: {capitale}")

# Anno 3
capitale *= (1 + tasso)

print((100 * (1 + tasso) ** 3))

print(f"Capitale dopo 3 anni: {capitale}")

# C + C * I = C (1 + I) ->
# 7 * (4 + 3) = 49
# 7 * 4 + 7 * 3 = 28 + 21 = 49
# 7 + 7 * 3 = 7 * 1 + 7 * 3
# = 7 * (1 + 3)
