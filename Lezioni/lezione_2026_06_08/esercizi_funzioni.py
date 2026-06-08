"""
Facciamo una funzione aabb
che presa una lista di numeri interi per ognuno
 * se è multiplo di 3 stampa "aa"
 * se è multiplo di 5 stampa "bb"
 * se è multiplo di 15 stampa "aabb"
"""
def aabb(lista_numeri: list[int]) -> None:
    for numero in lista_numeri:
        # if numero % 3 == 0 and numero % 5 == 0:
        #     print("aabb")
        # elif numero % 5 == 0:
        #     print("bb")
        # elif numero % 3 == 0:
        #     print("aa")

        da_stampare = ""

        if numero % 3 == 0:
            da_stampare += "aa"

        if numero % 5 == 0:
            da_stampare += "bb"
        print(da_stampare)

# aabb([1, 3, 5, 15, 20, 25, 12, 17])
"""
Facciamo una funzione che data una lista ordinata (crescente) di numeri e 
un target stampa True se esistono due numeri nella lista che sommati
danno il target
"""
def find_target(lista_numeri: list[int | float], target: int | float) -> None:
    left = 0
    right = len(lista_numeri) - 1
    trovato = False
    while left < right:
        if lista_numeri[left] + lista_numeri[right] == target:
            # print(lista_numeri[left], lista_numeri[right], True)
            trovato = True
            break
        elif lista_numeri[left] + lista_numeri[right] < target:
            left += 1
        else:
            right -= 1

    print(f"target: {target}, left: {left}, right: {right}, trovato: {trovato}")
# print([2, 4, 5, 7, 8, 11, 12])
# find_target([2, 4, 5, 7, 8, 11, 12], 12)
# find_target([2, 4, 5, 7, 8, 11, 12], 6)
# find_target([2, 4, 5, 7, 8, 11, 12], 13)
# find_target([2, 4, 5, 7, 8, 11, 12], 8)
# find_target([2, 4, 5, 7, 8, 11, 12], 3)
# find_target([2, 4, 5, 7, 8, 11, 12], 45)


"""
Facciamo una funzione che dato un numero n calcola l'n-simo numero 
di fibonacci
0 1 1 2 3 5 8 
numero_0 = 0
numero_1 = 1
numero_n = numero_(n-1) + numero_(n-2)
"""
def fibonacci(n: int) -> int:
    if n <= 2:
        return n - 1
    n_2 = 0
    n_1 = 1
    for i in range(2, n):
        corrente = n_1 + n_2
        n_2 = n_1
        n_1 = corrente

    return corrente / n_2

for i in range(2, 20):
    print(f"Numero di fibonacci pos {i} = {fibonacci(i)}")

