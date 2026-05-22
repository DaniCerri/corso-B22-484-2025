"""
Facciamo un dizionario con dentro 3 coppie di chiave-valore così
strutturate:

Letture di temperatura
Torino: 10, 20.2, 12.2, 10, 24, 20, 10.9
Roma: 14, 24.2, 16.2, 16, 28, 12
Palermo: 21, 20.2, 17.8, 25, 27

Calcoliamo e stampiamo per ogni città la temperatura media
Città: N °C

Poi calcoliamo la media totale e la stampiamo
Quest'ultima media NON è (media_T + media_R + media_P) / 3
"""

dizionario_temperature = {
    "Torino": [10, 20.2, 12.2, 10, 24, 20, 10.9],
    "Roma": [14, 24.2, 16.2, 16, 28, 12],
    "Palermo": [21, 20.2, 17.8, 25, 27]
}

for citta, temperature in dizionario_temperature.items():
    media = sum(temperature) / len(temperature)
    print(f"{citta}: {media:.2f} °C")

# Per calcolare la media complessiva dobbiamo considerare tutte le temperature insieme nello stesso
# contenitore
totale = 0
numero_t = 0
for temperature in dizionario_temperature.values():
    totale += sum(temperature)
    numero_t += len(temperature)

media_finale = totale / numero_t
print(f"Media finale: {media_finale:.2f}")

lista_medie = [sum(lista) / len(lista) for lista in dizionario_temperature.values()]
media_media = sum(lista_medie) / len(lista_medie)
print(f"Media delle medie: {media_media:.2f}")