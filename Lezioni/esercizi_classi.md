# Esercizi sulle Classi in Python (Difficoltà Crescente)

Questo documento contiene tre esercizi pratici per consolidare la comprensione della Programmazione Orientata agli Oggetti (OOP) in Python.

---

## 📚 Esercizio 1: Livello Base – La classe `Libro`

**Obiettivo:** Imparare a creare una classe, definire il metodo costruttore `__init__` e aggiungere un metodo semplice.

### Traccia
Crea una classe chiamata `Libro`.
1. Il costruttore deve accettare come parametri (oltre a `self`): `titolo`, `autore` e `pagine`.
2. Aggiungi un metodo chiamato `descrizione()` che restituisca o stampi una stringa formattata del tipo:
   > *"Il libro 'Il Signore degli Anelli' è stato scritto da J.R.R. Tolkien e ha 1200 pagine."*
3. Instanzia almeno due oggetti di questa classe con dati a tua scelta e chiama il metodo `descrizione()` per ciascuno di essi.

---

## 🏦 Esercizio 2: Livello Intermedio – Il `ContoBancario`

**Obiettivo:** Gestire lo stato di un oggetto tramite metodi, utilizzare l'incapsulamento (attributi privati/protetti) e implementare una logica di controllo.

### Traccia
Crea una classe chiamata `ContoBancario`.
1. Il costruttore deve inizializzare il nome del `titolare` e impostare un attributo privato `_saldo` (o `__saldo`) inizialmente pari a `0` (oppure a un valore passato come argomento).
2. Crea un metodo `deposita(importo)` che aggiunge la cifra al saldo (l'importo deve essere maggiore di zero).
3. Crea un metodo `preleva(importo)` che sottrae la cifra dal saldo. **Attenzione:** il prelievo è consentito solo se il saldo è sufficiente; in caso contrario, stampa un messaggio di errore ("Saldo insufficiente").
4. Crea un metodo `mostra_saldo()` che stampi a schermo il saldo attuale del conto.
5. Testa la classe effettuando un deposito, un prelievo andato a buon fine e un tentativo di prelievo superiore alla disponibilità attuale.

---

## 🛒 Esercizio 3: Livello Avanzato – Sistema `CarrelloECommerce`

**Obiettivo:** Interazione tra più classi (composizione), gestione di liste all'interno di un oggetto e calcoli dinamici.

### Traccia
Crea due classi distinte: `Prodotto` e `Carrello`.

1. **Classe `Prodotto`**:
   - Il costruttore accetta `nome` e `prezzo`.

2. **Classe `Carrello`**:
   - Il costruttore non accetta parametri esterni, ma inizializza una lista vuota chiamata `prodotti`.
   - Crea un metodo `aggiungi_prodotto(prodotto)` que accetta un oggetto di tipo `Prodotto` e lo aggiunge alla lista del carrello.
   - Crea un metodo `rimuovi_prodotto(nome_prodotto)` che cerca un prodotto nella lista tramite il nome e lo rimuove (se presente).
   - Crea un metodo `calcola_totale()` che restituisce la somma dei prezzi di tutti i prodotti presenti nel carrello.
   - Crea un metodo `applica_sconto(percentuale)` che riduce il costo totale del carrello della percentuale indicata (es: se si inserisce `10`, il totale finale viene scontato del 10%).

### Esempio di Test richiesto
Crea tre oggetti `Prodotto` (es: "Mouse" a 25€, "Tastiera" a 50€, "Monitor" a 150€). Aggiungili al carrello, calcola il totale iniziale, applica uno sconto del 10% e mostra il prezzo finale ottenuto.