"""
Prendiamo in input due numeri interi positivi a e b e
utilizzando SOLAMENTE le somme/sottrazioni stampiamo
il risultato di
 * prima: a // b
 * poi: a % b

suggerimento: usiamo il ciclo while
NOTA: b > 0, a >= 0
"""
while True:
    numeri = input("Inserisci a e b separati da ';' (a;b): ").split(";")
    a, b = [int(numero) for numero in numeri]
    if a >= 0 and b > 0:
        break
    print("a deve essere >= 0, b deve essere > 0")
print(f"a: {a}, b: {b}")

risultato = 0  # Contatore che conta quante volte b sta dentro a
resto = a  # All'inizio il resto è tutto a
while resto >= b:
    resto -= b
    risultato += 1

print(f"{a} // {b} = {risultato}")
print(f"{a} % {b} = {resto}")


