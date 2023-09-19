# Prog_Snake
## Progetto realizzato da Martina, Angelo e Antonio

Questa repository contiene un'implementazione in Python del famoso gioco snake

## Introduzione

Questo programma prevede l'implementazione del gioco da riga di comando, risaltando piu le meccaniche del gioco rispetto all'interfaccia grafica che rimarrà minimale. 

## Descrizione del gioco

## Funzionamento

### Funzioni principali di Funzioni_gioco

#### Play(Angelo)

#### Converti_mosse(Martina)

#### Controlla(Antonio)

### Funzioni Secondarie di Controlla

#### Mangia (Antonio)

#### Termina (Angelo)

#### Muovi (Martina)

### Funzioni Secondarie di Play

#### Calcolo_mossa (Martina)

### Funzioni principali di gestione_input

#### carico_dati (Angelo)

#### restituisco_dati (ignoto)

### Main (Angelo)



# Avvio Progetto

## Clonare il repository: 
```
https://github.com/AngeloSpadea/Prog_Snake.git

```
## Installare le dipendenze
```
pip install -r requirements.txt

```

## Avviare il gioco

# Avanzamento del progetto 

### Utility

#### Struttura Docker
[✗] Implementazione<br> 
  0%|------------------------------| 0/1 [00:00 ___________, Commits: _ ]<br>

#### Scheletro del Readme
[✓] Scrittura Introduzione<br>
[✗] Scrittura Funzionamento<br>
[✗] Scrittura Istruzioni di installazione<br>
[✗] Aggiornamento Stato progetto<br>
100%|██████------------------------| 1/4 [00:00 Sep 15 2023, Commits: 5,6 ]<br>

#### gitignore
[✓] Scrittura<br>
100%|██████████████████████████████| 1/1 [00:00 Sep 15 2023, Commits: 7 ]<br>

### Funzioni principali di Funzioni_gioco

#### Play(Angelo)
[✓] Implementazione Funzione<br>
[✓] Implementazione Test<br>
100%|██████████████████████████████| 2/2 [00:00 Sep 18 2023, Commits: 18]<br>

#### Converti_mossa(Martina)
[✓] Implementazione Funzione<br>
[✓] Implementazione Test<br>
100%|██████████████████████████████| 2/2 [00:00 Sep 15 2023, Commits: 5,6 ]<br>

#### Controlla(Antonio)
[✗] Implementazione Funzione<br>
[✗] Implementazione Test<br>
  0%|------------------------------| 0/2 [00:00 ___________, Commits: _ ]<br>

### Funzioni Secondarie di Controlla

#### Mangia (Antonio)
[✓] Implementazione Funzione<br>
[✓] Implementazione Test<br>
100%|██████████████████████████████| 2/2 [00:00 Sep 15 2023, Commits: 10,11,12 ]<br>

#### Termina (Angelo)
[✓] Implementazione Funzione<br>
[✗] Implementazione Test<br>
 50%|███████████████---------------| 1/2 [00:00 Sep 15 2023, Commits: 8 ]<br>

#### Muovi (Martina)
[✓] Implementazione Funzione<br>
[✓] Implementazione Test<br>
100%|██████████████████████████████| 2/2 [00:00 Sep 16 2023, Commits: 13,14 ]<br>

### Funzioni Secondarie di Play

#### Calcolo_mossa (Martina)
[✓] Implementazione Funzione<br>
[✓] Implementazione Test<br>
100%|██████████████████████████████| 2/2 [00:00 Sep 12 2023, Commits: 3,4 ]<br>
##### Descrizione
> def calcola_mossa(): nel file funzioni_gioco.py riga 40
Funzione che calcola la nuova posizione della testa tenendo conto della dimensione del campo da gioco.

##### Test 1
> test_verifico_calcola_mossa nel file test_01.py riga 13

Nel Test verifichiamo che il movimento sia quello corretto. I paramentri di ingresso di calcolo mossa sono il corpo composto dalla sola testa nella posizione (2,0), la direzione che deve prendere il serpente in questo caso est rappresentato dal vettore (0,1) e infine le dimensioni del campo prima le righe e poi le collone. Inserendo un qualsiasi corpo del serpente e un vettore direzione il risultato del test sarà positivo se la testa del serpente si muovera nella direzione corretta. Esempio testa (2,0) direzione (1,0) risultato la posizione della testa si troverà in (2,1).
##### Test 2
> test_verifico_calcola_mossa_con_uscita_dal_bordo nel file test_01.py riga 17

Nel Test verifichiamo cosa succede se la testa del serpente esce fuori dal bordo del campo. I paramentri di ingresso di calcolo mossa sono il corpo composto dalla sola testa nella posizione (3,5), la direzione che deve prendere il serpente in questo caso nord-est rappresentato dal vettore (1,1) e infine le dimensioni del campo prima le righe 4 e poi le collone 6. La nuova posizione calcolata dalla funzione dovrebbe essere (4,6) ma considerando che le collone sono 6 partendo da 0 la posizione (4,6) non è accettabile perchè il serpente attraverserà il bordo e si ritrovarà dall'altra parte nel campo, posizione (0,0).

### Funzioni principali di gestione_input
[✓] Implementazione carico_dati<br>
[✓] Implementazione restituisco_dati<br>
100%|██████████████████████████████| 2/2 [00:00 Sep 18 2023, Commits: 16,17]<br>

#### carico_dati (Angelo)
[✓] Implementazione Test<br>
100%|██████████████████████████████| 1/1 [00:00 Sep 18 2023, Commits: 19 ]<br>

#### restituisco_dati (ignoto)
[✗] Implementazione Funzione<br>
[✗] Implementazione Test<br>
  0%|------------------------------| 0/2 [00:00 ___________, Commits: _ ]<br>

### Main (Angelo)
[✗] Implementazione Funzione<br>
[✗] Implementazione Test<br>
  0%|------------------------------| 0/2 [00:00 Sep  6 2023, Commits: 1 ]<br>

## Note
Bisogna gestire ancora quando la testa atraversa il corpo<br>
Opzioni<br> 
    1 --> Scrittura di una nuova funzione<br>
    2 --> Inserimento all'interno di Controlla<br>