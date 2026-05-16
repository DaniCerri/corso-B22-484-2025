## Esercizio 1: Controllo accesso in palestra

Una palestra ammette l'ingresso solo a determinate condizioni.

**Regole:**
- L'utente deve avere almeno 16 anni.
- L'abbonamento non deve essere scaduto (`abbonamento_attivo = True`).
- Gli orari di apertura sono dalle `07:00` alle `22:30`.
- Sotto i 18 anni si entra solo prima delle `20:00`.

**Cosa fare:**
1. Chiedere all'utente: età, stato abbonamento (`s`/`n`), orario in formato `hh:mm`.
2. Decidere con `if / elif / else` se l'utente può entrare.
3. In caso di rifiuto, stampare il motivo specifico (es. *"abbonamento scaduto"*,
   *"troppo tardi per i minorenni"*).

**Esempio:**
```
Età: 17
Abbonamento attivo (s/n): s
Orario (hh:mm): 20:30
> Accesso negato: troppo tardi per i minorenni
```

---

## Esercizio 2: Validazione codice fiscale (lunghezza)

Vogliamo accettare in input un codice fiscale italiano. Per ora controlliamo
solo che abbia la lunghezza giusta (16 caratteri). Continuiamo a richiederlo
finché l'input non è valido (stile loop di validazione visto in `for_e_while.py`).

**Regole:**
- Il codice deve essere lungo esattamente 16 caratteri.
- Va trasformato in maiuscolo prima del controllo.
- Stampare quanti tentativi sbagliati ha fatto l'utente.

**Cosa fare:**
1. Usare un `while` che ripete l'input finché la lunghezza non è 16.
2. Tenere un contatore `tentativi` che aumenta ogni volta che l'input è sbagliato.
3. Alla fine stampare il codice valido e il numero di tentativi sbagliati.

---

## Esercizio 3: Conto in banca con interesse composto

Variante dell'esercizio sull'interesse visto a lezione il 15/05.

**Dati:**
- Capitale iniziale: `1500 €`
- Tasso annuo: `3.5%`
- Obiettivo: arrivare ad almeno `2500 €`.

**Cosa fare:**
1. Usare un `while` che continua finché il capitale è sotto l'obiettivo.
2. Ad ogni iterazione applicare l'interesse: `capitale *= (1 + tasso)`.
3. Salvare ogni valore in una lista `storico`.
4. Alla fine stampare quanti anni servono e lo storico formattato con 2 decimali
   e simbolo `€` (vedi `f"{x:.2f} €"`).

**Bonus:** stampare anche l'interesse complessivo in percentuale
(`{var:.2%}` come in lezione).

---

## Esercizio 4: Carrello e sconto a soglia

Un e-commerce applica sconti in base al totale del carrello.

**Dati:**
```python
carrello = [12.50, 4.99, 30.00, 7.20, 18.75, 2.50]
```

**Regole sconto:**
- Totale `< 20€`: nessuno sconto.
- Totale tra `20€` e `50€`: sconto del `5%`.
- Totale tra `50€` e `100€`: sconto del `10%`.
- Totale `>= 100€`: sconto del `15%`.

**Cosa fare:**
1. Calcolare il totale con un ciclo `for` (no `sum()`, è troppo facile).
2. Applicare lo sconto giusto con `if / elif / else`.
3. Stampare totale prima dello sconto, percentuale applicata, totale finale.

---

## Esercizio 5: Conta giorni lavorativi tra due date (anno semplificato)

Versione semplificata: assumiamo che ogni mese abbia 30 giorni e ogni settimana
6 giorni lavorativi (dal lunedì al sabato, si salta solo la domenica).

**Input:**
- Data inizio in formato `dd/MM/YYYY` (riusa la validazione di `for_e_while.py`:
  il `while` ripete finché `split("/")` non dà 3 pezzi).
- Data fine nello stesso formato.

**Cosa fare:**
1. Validare entrambe le date con `while` finché non hanno il formato corretto.
2. Convertire ciascuna in un numero totale di giorni:
   `giorni_totali = anno * 360 + mese * 30 + giorno`.
3. Con un `for` che cicla su `range(giorni_inizio, giorni_fine + 1)` contare
   solo i giorni che NON sono domenica.
   Considera domenica quando `giorno_corrente % 7 == 0` (semplificazione).
4. Stampare il numero di giorni lavorativi.

**Bonus:** se la data di fine è prima di quella di inizio, stampare un errore e
non fare il conto.
