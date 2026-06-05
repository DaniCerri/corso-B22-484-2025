# Esercizio: Analisi Finanziaria e Performance di Portafoglio

## Contesto
In qualità di analista quantitativo, ti viene assegnato il compito di valutare le performance storiche di un portafoglio composto da tre diversi asset. Hai a disposizione una matrice iniziale in cui ogni riga rappresenta un'azione e ogni colonna rappresenta il prezzo di chiusura settimanale registrato sul mercato.

## Obiettivi dell'Esercizio
A partire dai dati iniziali, sviluppa un algoritmo in Python per ottenere le seguenti metriche per ciascun asset:

1. **Matrice delle variazioni assolute**: Calcola la differenza di prezzo tra ogni periodo e il periodo direttamente precedente.
2. **Matrice delle variazioni percentuali**: Esprimi le variazioni appena trovate come tasso percentuale rispetto al prezzo del periodo precedente.
3. **Variazione cumulativa finale**: Calcola il bilancio netto tra l'inizio e la fine dell'osservazione (applicando l'aggregazione per somma delle righe sulla matrice delle variazioni assolute).
4. **Escursione massima (Volatility Spread)**: Individua la massima distanza calcolando la differenza tra la variazione percentuale più alta e quella più bassa registrate per il singolo asset.
5. **Interesse medio al periodo (CAGR)**: Converti le variazioni percentuali in coefficienti moltiplicativi (es. un incremento del 2% diventa `1.02`) e utilizza la media geometrica per ricavare il tasso di crescita medio reale per ogni periodo.
6. **Indice di Rischio (Volatilità)**: Calcola la deviazione standard sulla matrice delle variazioni percentuali per determinare l'instabilità e l'oscillazione dell'asset rispetto alla sua media.

## Dati di Partenza

Utilizza le seguenti strutture dati per l'implementazione del codice:

```python
# Matrice dei prezzi storici
# Righe: Azione Alpha, Azione Beta, Azione Gamma
# Colonne: Settimana 1, Settimana 2, Settimana 3, Settimana 4, Settimana 5

prezzi_storici = [
    [100.0, 102.0, 101.5, 103.0, 104.5],  
    [45.0, 52.0, 41.0, 48.5, 39.0],       
    [200.0, 210.0, 220.5, 231.5, 243.0]   
]

nomi_asset = ["Azione Alpha", "Azione Beta", "Azione Gamma"]
```