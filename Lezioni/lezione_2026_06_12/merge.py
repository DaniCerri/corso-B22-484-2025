def merge(lista1: list[int | float], lista2: list[int | float]) -> list[int | float]:
    """
    Funzione che unisce due liste ordinate in una terza, mantenendola ordinata
    :param lista1: lista di numeri
    :param lista2: lista di numeri
    :return: lista ordinata unita
    """
    indice_prima = 0
    indice_seconda = 0
    output = [0] * (len(lista1) + len(lista2))
    # print(f"Lista iniziale: {output}")
    while indice_prima < len(lista1) and indice_seconda < len(lista2):
        # a ogni passo confrontiamo gli elementi al proprio indice e inseriamo
        # nella lista di output il minore
        # print(f"{'-' * 20} Passo {indice_seconda + indice_prima + 1} {'-' * 20}")
        # print(f"Indice prima: {indice_prima}")
        # print(f"Indice seconda: {indice_seconda}")
        # print(f"Confronto {lista1[indice_prima]} e {lista2[indice_seconda]}")
        if lista1[indice_prima] < lista2[indice_seconda]:
            output[indice_prima + indice_seconda] = lista1[indice_prima]
            # se inseriamo il primo elemento, aggiorniamo il suo indice
            indice_prima += 1
            # print(f"Aggiungo {lista1[indice_prima - 1]} alla lista finale")
        else:
            output[indice_prima + indice_seconda] = lista2[indice_seconda]
            # se inseriamo il secondo elemento, aggiorniamo il suo indice
            indice_seconda += 1
            # print(f"Aggiungo {lista2[indice_seconda - 1]} alla lista finale")


        # print(f"Lista aggiornata: {output}")
        # input()
    # print("-" * 70)
    if not indice_prima < len(lista1):
        # print("E' finita prima la lista 1, aggiungo la 2")
        for i in range(indice_seconda, len(lista2)):
            output[i + indice_prima] = lista2[i]
            # print(f"Aggiungo {lista2[i]}: {output}")
            # input()
    else:
        # print("E' finita prima la lista 1, aggiungo la 2")
        for i in range(indice_prima, len(lista1)):
            output[i + indice_seconda] = lista1[i]
            # print(f"Aggiungo {lista1[i]}: {output}")
            # input()

    return output
if __name__ == "__main__":
    l1 = [5]
    l2 = [7]
    print(f"Lista1: {l1}")
    print(f"Lista2: {l2}")
    print()
    l = merge(l1, l2)
    print(l)
