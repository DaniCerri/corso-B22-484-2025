"""
Vogliamo fare un calcolatore di tasse
Chiediamo all'utente di inserire
 * Coeff di redditività: N%
 * % di IRPEF (dell'imponibile): N%
 * % di INPS (dell'imponibile): N%
 * € Fatturato (dell'anno): N€
 * N° fatture (dell'anno): N
"""
"""
Calcoliamo:
 * Netto €
 * Da pagare per INPS
 * Da pagare per IRPEF
 * € Fattura media
 * BONUS: % di netto sul lordo
"""
# numero_str = input("Inserisci un numero: ")
# numero = float(numero_str)
# print(numero_str, numero)

coeff_redditivita = input("Inserisci il coeff di redditività (N%): ")
coeff_redditivita = int(coeff_redditivita) / 100

coeff_inps = input("Inserisci il coeff di INPS (N%): ")
coeff_inps = int(coeff_inps) / 100

coeff_irpef = input("Inserisci il coeff di IRPEF (N%): ")
coeff_irpef = int(coeff_irpef) / 100

fatturato = input("Inserisci il fatturato (N€): ")
fatturato = float(fatturato)

n_fatture = input("Inserisci il numero di fatture (N): ")
n_fatture = int(n_fatture)

da_pagare_inps = fatturato * coeff_redditivita * coeff_inps
da_pagare_irpef = fatturato * coeff_redditivita * coeff_irpef

fatt_media = fatturato / n_fatture

# netto = fatturato - (da_pagare_inps + da_pagare_irpef)
# perc_netto = netto / fatturato

# perc_netto = 1 - coeff_redditivita * coeff_irpef + coeff_redditivita * coeff_inps
perc_netto = 1 - (coeff_redditivita * (coeff_irpef + coeff_inps))
