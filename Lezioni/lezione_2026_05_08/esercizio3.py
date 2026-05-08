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
