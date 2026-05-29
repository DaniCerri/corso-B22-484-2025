"""
Dobbiamo fare un viaggio che abbiamo rappresentato come lista di dizionari
che ci dicono partenza, arrivo, distanza

Abbiamo a disposizione un serbatoio da 50L e sappiamo il costo al L di benzina
e il consumo in L per 100 km

Vogliamo sapere
 * distanza totale
 * consumo totale
 * costo totale carburante
 * quante volte abbiamo fatto il pieno, sapendo che non scendiamo mai sotto
   il 40% del serbatoio per sicurezza
"""
def calcola_distanza(tappe):
    totale = 0
    for tappa in tappe:
        totale += tappa['distanza']
    return totale

def calcola_consumo(distanza, consumo_unitario, denominatore):
    return distanza * consumo_unitario / denominatore

def calcola_costo_carburante(consumo_tot, costo_carburante):
    return consumo_tot * costo_carburante

def conta_soste(serbatoio, consumo_tot):
    volte_min = consumo_tot // serbatoio
    if consumo_tot % serbatoio > 0:
        volte_min += 1

    return (serbatoio + consumo_tot - 1) // serbatoio
    return volte_min

lista_tappe = [
    {"partenza": "Torino", "arrivo": "Milano", "distanza": 150.2},
    {"partenza": "Milano", "arrivo": "Bologna", "distanza": 213.8},
    {"partenza": "Bologna", "arrivo": "Firenze", "distanza": 118.32},
    {"partenza": "Firenze", "arrivo": "Napoli", "distanza": 472.72},
    {"partenza": "Napoli", "arrivo": "Reggio Calabria", "distanza": 491.08},
]
serbatoio = 50
limite_inferiore_serbatoio = 0.4  # Al 40% facciamo il pieno
consumo = 12.32  # L / 100km
costo_benzina = 1.931  # Costo per 1L di benzina
