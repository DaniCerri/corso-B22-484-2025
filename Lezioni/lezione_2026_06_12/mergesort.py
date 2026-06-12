import merge

def mergesort(lista_numeri: list[int | float]) -> list[int | float]:
    # 1. troviamo lunghezza e metà della lista
    meta = int(len(lista_numeri) // 2)
    if meta == 0:
        print(f"la lista è lunga 1: {lista_numeri}")
        return  lista_numeri

    # 2. spezziamo a metà la lista
    prima_meta = lista_numeri[:meta]
    seconda_meta = lista_numeri[meta:]
    print(f"Prima metà: {prima_meta} | Seconda metà: {seconda_meta}")

    # 3. richiamo mergesort su ogni metà
    lista_1 = mergesort(prima_meta)
    lista_2 = mergesort(seconda_meta)

    print(f"Prima metà ordinata: {lista_1}")
    print(f"Seconda metà ordinata: {lista_2}")

    return merge.merge(lista_1, lista_2)


l = mergesort([1, 2, 3, 4, 5, 6, 7, 8][::-1])
print(l)