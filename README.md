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
___
1 __Struttura Docker__
[✗] Implementazione<br> 
  0%|------------------------------| 0/1 [00:00 ___________, Commits: _ ]<br>
___
2 __Scheletro del Readme__
[✓] Scrittura Introduzione<br>
[✗] Scrittura Funzionamento<br>
[✗] Scrittura Istruzioni di installazione<br>
[✗] Aggiornamento Stato progetto<br>
100%|██████------------------------| 1/4 [00:00 Sep 15 2023, Commits: 5,6 ]<br>
___
3 __gitignore__
[✓] Scrittura<br>
100%|██████████████████████████████| 1/1 [00:00 Sep 15 2023, Commits: 7 ]<br>

### Funzioni principali di Funzioni_gioco
___
4 __Play(Angelo)__
[✓] Implementazione Funzione<br>
[✓] Implementazione Test<br>
100%|██████████████████████████████| 2/2 [00:00 Sep 18 2023, Commits: 18]<br>
___
5 __Converti_mossa(Martina)__
[✓] Implementazione Funzione<br>
[✓] Implementazione Test<br>
100%|██████████████████████████████| 2/2 [00:00 Sep 15 2023, Commits: 5,6 ]<br>
___
6 __Controlla(Antonio)__
[✗] Implementazione Funzione<br>
[✗] Implementazione Test<br>
  0%|------------------------------| 0/2 [00:00 ___________, Commits: _ ]<br>

### Funzioni Secondarie di Controlla
___
7 __Mangia (Antonio)__
[✓] Implementazione Funzione<br>
[✓] Implementazione Test<br>
100%|██████████████████████████████| 2/2 [00:00 Sep 15 2023, Commits: 10,11,12 ]<br>
___
8 __Termina (Angelo)__
[✓] Implementazione Funzione<br>
[✗] Implementazione Test<br>
 50%|███████████████---------------| 1/2 [00:00 Sep 15 2023, Commits: 8 ]<br>
___
9 __Muovi (Martina)__
[✓] Implementazione Funzione<br>
[✓] Implementazione Test<br>
100%|██████████████████████████████| 2/2 [00:00 Sep 16 2023, Commits: 13,14 ]<br>

### Funzioni Secondarie di Play
___
10 __Calcolo_mossa (Martina)__
> il nome della funzione è def calcola_mossa(parametri): che si trova nel file funzioni_gioco.py alla riga 40

[Vai a calcola_mossa ](https://github.com/AngeloSpadea/Prog_Snake/blob/main/funzioni_gioco.py#L40)

[✓] Implementazione Funzione<br>
[✓] Implementazione Test<br>
100%|██████████████████████████████| 2/2 [00:00 Sep 12 2023, Commits: 3,4 ]<br>
`Descrizione`

Funzione che calcola la nuova posizione della testa tenendo conto della dimensione del campo da gioco.

`Test 1`
> test_verifico_calcola_mossa nel file test_01.py riga 13

Nel Test verifichiamo che il movimento sia quello corretto. I paramentri di ingresso di calcolo mossa sono il `corpo` composto dalla sola testa nella posizione (2,0), la `direzione` che deve prendere il serpente in questo caso est rappresentato dal vettore (0,1) e infine le `dimensioni del campo` prima le righe e poi le collone. Inserendo un qualsiasi `corpo del serpente` e un `vettore direzione` il `risultato del test` sarà positivo se la testa del serpente si muovera nella `direzione corretta`. Esempio `testa` (2,0) `direzione` (1,0) `risultato` la posizione della testa si troverà in (2,1).
`Test 2`
> test_verifico_calcola_mossa_con_uscita_dal_bordo nel file test_01.py riga 17

Nel Test verifichiamo cosa succede se la testa del serpente esce fuori dal bordo del campo. I paramentri di ingresso di calcolo mossa sono il `corpo` composto dalla sola testa nella posizione (3,5), la `direzione` che deve prendere il serpente in questo caso nord-est rappresentato dal vettore (1,1) e infine le `dimensioni del campo` prima le righe 4 e poi le collone 6. La nuova `posizione` calcolata dalla funzione dovrebbe essere (4,6) ma considerando che le collone sono 6 partendo da 0 la posizione (4,6) non è accettabile perchè il serpente `attraverserà il bordo` e si ritrovarà dall'altra parte nel campo, `posizione` (0,0).

### Funzioni principali di gestione_input
[✓] Implementazione carico_dati<br>
[✓] Implementazione restituisco_dati<br>
100%|██████████████████████████████| 2/2 [00:00 Sep 18 2023, Commits: 16,17]<br>
___
11 __carico_dati (Angelo)__
[✓] Implementazione Test<br>
100%|██████████████████████████████| 1/1 [00:00 Sep 18 2023, Commits: 19 ]<br>
___
12 __restituisco_dati (ignoto)__
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