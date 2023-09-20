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

Una volta clonata la repository da terminale collocarsi nella directy di Prog_Snake e avviare il seguente comando

>Terminale
```
python main.py
```

E' possibile scegliere il campo da gioco e le mosse che effettuerà il serpente modificando il file `fiel_in.json` e `file_gioco.json`, due esempio di partite si trovano nella cartella `partite` [Vai alla cartella partite ](https://github.com/AngeloSpadea/Prog_Snake/tree/main/partite) per effettuare la modifica copiare il contenuto di `field_01.json` o `field_02.json` e sostituirlo al contenuto di field_in.json esegure la medesima operazione per i file `gamefile_*.json` e sostituire il contenuto nel file `file_gioco.json`. Procedura provvisoria che verrà sostituita nelle prossime fasi del progetto.

___
-------   `AVVERTENZA`   -------
Nel Modificare i test tenere conto che nella rappresentazione dei punti [i,j] `i` rappresente la `colonna` mentre `j` rappresenta la `riga`
___

# Avanzamento del progetto 


### Utility
___
1 __Struttura Docker__
[✗] Implementazione<br> 
  0%|------------------------------| 0/1 [00:00 ___________, Commits: _ ]<br>
___
2 __Scheletro del Readme__

[Vai a Readme.md ](https://github.com/AngeloSpadea/Prog_Snake/blob/main/README.md?plain=1)

[✓] Scrittura Introduzione<br>
[✗] Scrittura Funzionamento<br>
[✗] Scrittura Istruzioni di installazione<br>
[✗] Aggiornamento Stato progetto<br>
100%|██████------------------------| 1/4 [00:00 Sep 15 2023, Commits: 5,6 ]<br>
`Descrizione`
___
3 __gitignore__

[Vai a .gitignore ](https://github.com/AngeloSpadea/Prog_Snake/blob/main/.gitignore)

[✓] Scrittura<br>
100%|██████████████████████████████| 1/1 [00:00 Sep 15 2023, Commits: 7 ]<br>
`Descrizione`

### Funzioni principali di Funzioni_gioco
___
4 __Play(Angelo)__
> il nome della funzione è `def play(parametri):` che si trova nel file `funzioni_gioco.py` alla riga 182

[Vai alla funzine play() ](https://github.com/AngeloSpadea/Prog_Snake/blob/main/funzioni_gioco.py#L182)

[✓] Implementazione Funzione<br>
[✓] Implementazione Test<br>
100%|██████████████████████████████| 2/2 [00:00 Sep 18 2023, Commits: 18]<br>
`Descrizione`

Funzione che gestisce il gioco: converte le mosse, controlla se la 
posizione iniziale è una casella valida e per ogni mossa gestisce se il 
serpente deve muoversi, mangiare o se il serpente si blocca facendo 
terminare così il gioco.
___
5 __Converti_mosse(Martina)__
> il nome della funzione è `def converti_mosse(parametri):` che si trova nel file `funzioni_gioco.py` alla riga 9

e[Vai alla funzione converti_mosse() ](https://github.com/AngeloSpadea/Prog_Snake/blob/main/funzioni_gioco.py#L9)

[✓] Implementazione Funzione<br>
[✓] Implementazione Test<br>
100%|██████████████████████████████| 2/2 [00:00 Sep 15 2023, Commits: 5,6 ]<br>
`Descrizione`

Funzione che converte tutte le mosse scritte nella forma dei punti cardinali
nella forma vettoriale [a,b] dove a e b rappresentano lo spostamentamento 
rispettivamente nelle righe e nelle colonne

`Test 1`
> test_verifico_calcola_mossa nel file test_01.py riga 21

[Vai a test_corverti_mosse ](https://github.com/AngeloSpadea/Prog_Snake/blob/main/test_01.py#L21)

In questo primo test viene passata alla funzione la lista con le mosse, in questo caso (['N']) dove al suo interno c'è un'unica mossa Nord. La funzione una volta riconosciuta la mossa la converte in un vettore che successivamente viene verificato. Il test avra successo se la conversione come in questo cosa con il risultato [[-1, 0]] avverrà corettamente. Inserendo altri punti cardinali con i relativi vettori si potrà testare il corretto funzionamento della funzione

`Test 2`
> test_verifico_calcola_mossa nel file test_01.py riga 25

[Vai a test_corverti_mosse_oblique ](https://github.com/AngeloSpadea/Prog_Snake/blob/main/test_01.py#L25)

In questo secondo caso andremo ad affrontare il riconoscimento dei punti cardinali con doppio simbolo, come NW NE SO ecc ecc.. La funzione dovrà riconoscere che il punto cardinale sia sincolo e non doppio per poi convertirlo in maniera corretta. In questo caso si esaminerà (['NW']) con il giusto vettore che sarà [[-1, -1]]

___
6 __Controlla(Antonio)__
> il nome della funzione è `def controlla(parametri):` che si trova nel file `funzioni_gioco.py` alla riga 67

[Vai alla funzione controlla() ](https://github.com/AngeloSpadea/Prog_Snake/blob/main/funzioni_gioco.py#L67)

[✗] Implementazione Funzione<br>
[✗] Implementazione Test<br>
  0%|------------------------------| 0/2 [00:00 ___________, Commits: _ ]<br>
`Descrizione`

Funzione che controlla se la posizione nuova è:
1) un blocco ("block"): allora il gioco deve terminare
2) una cibo ("food"): allora il serpente deve mangiare e crescere di dimensione
3) casella vuota: allora il serpente si muove


### Funzioni Secondarie di Controlla
___
7 __Mangia (Antonio)__
> il nome della funzione è `def mangia(parametri):` che si trova nel file `funzioni_gioco.py` alla riga 98

[Vai alla funzione mangia() ](https://github.com/AngeloSpadea/Prog_Snake/blob/main/funzioni_gioco.py#L98)

[✓] Implementazione Funzione<br>
[✓] Implementazione Test<br>
100%|██████████████████████████████| 2/2 [00:00 Sep 15 2023, Commits: 10,11,12 ]<br>
`Descrizione`

Funzione che fa mangiare al serpente il cibo, il quale viene rimosso dalla 
lista del cibo.

`Test 1`
> test_mangia nel file test_01.py riga 29

[Vai a test_corverti_mosse_oblique ](https://github.com/AngeloSpadea/Prog_Snake/blob/main/test_01.py#L29)

In questo test si analizzerà il caso in cui il movimento del sepente cadrà sopra ad una casella cibo. Nella funzione mangia verranno pessati 4 parametri. Il primo paramentro rappresenta il corpo del serpente, con tutte le caselle occupate, il secondo paramentro rappresenterà invece la scia prodotta, il terzo paramentro sarà la nuova possizione della testa ed in fine ci sara il campo da gioco che viene definito alla riga 5 [ Vai campo_da_gioco ](https://github.com/AngeloSpadea/Prog_Snake/blob/main/test_01.py#L5). 
Il test per avere successo verificherà 3 parametri il primo collocato in result[0] verifica che il serpente abbia mangiato e si sia allungato di 2, il secondo parametro result[1] verifica che la scia sia aggiornata e il terzo parametro controlla se la casella cibo mangiata sia stata poi eliminata dalla variabile campo_da_gioco
___
8 __Termina (Angelo)__
> il nome della funzione è `def termina(parametri):` che si trova nel file `funzioni_gioco.py` alla riga 166

[Vai alla funzione termina() ](https://github.com/AngeloSpadea/Prog_Snake/blob/main/funzioni_gioco.py#L166)

[✓] Implementazione Funzione<br>
[✗] Implementazione Test<br>
 50%|███████████████---------------| 1/2 [00:00 Sep 15 2023, Commits: 8 ]<br>
 `Descrizione`

 Funzione che fa terminare il gioco

___
9 __Muovi (Martina)__
> il nome della funzione è `def muovi(parametri):` che si trova nel file `funzioni_gioco.py` alla riga 133

[Vai alla funzione muovi() ](https://github.com/AngeloSpadea/Prog_Snake/blob/main/funzioni_gioco.py#L133)

[✓] Implementazione Funzione<br>
[✓] Implementazione Test<br>
100%|██████████████████████████████| 2/2 [00:00 Sep 16 2023, Commits: 13,14 ]<br>
`Descrizione`

Funzione che fa muovere il serpente

`Test 1`
> test_muovi_start nel file test_01.py riga 35

[Vai a test_muovi_start ](https://github.com/AngeloSpadea/Prog_Snake/blob/main/test_01.py#L35)

`Test 2`
> test_muovi nel file test_01.py riga 40

[Vai a test_muovi ](https://github.com/AngeloSpadea/Prog_Snake/blob/main/test_01.py#L40)

`Test 3`
> test_muovi_da_cresciuto nel file test_01.py riga 45

[Vai a test_muovi_da_cresciuto ](https://github.com/AngeloSpadea/Prog_Snake/blob/main/test_01.py#L25)

### Funzioni Secondarie di Play
___
10 __Calcolo_mossa (Martina)__
> il nome della funzione è `def calcola_mossa(parametri):` che si trova nel file `funzioni_gioco.py` alla riga 40

[Vai alla funzione calcola_mossa() ](https://github.com/AngeloSpadea/Prog_Snake/blob/main/funzioni_gioco.py#L40)

[✓] Implementazione Funzione<br>
[✓] Implementazione Test<br>
100%|██████████████████████████████| 2/2 [00:00 Sep 12 2023, Commits: 3,4 ]<br>
`Descrizione`

Funzione che calcola la nuova posizione della testa tenendo conto della dimensione del campo da gioco.

`Test 1`
> test_verifico_calcola_mossa nel file test_01.py riga 13

[Vai a test_verifico_calcola_mossa ](https://github.com/AngeloSpadea/Prog_Snake/blob/main/test_01.py#L13)

Nel Test verifichiamo che il movimento sia quello corretto. I paramentri di ingresso di calcolo mossa sono il `corpo` composto dalla sola testa nella posizione (2,0), la `direzione` che deve prendere il serpente in questo caso est rappresentato dal vettore (0,1) e infine le `dimensioni del campo` prima le righe e poi le collone. Inserendo un qualsiasi `corpo del serpente` e un `vettore direzione` il `risultato del test` sarà positivo se la testa del serpente si muovera nella `direzione corretta`. Esempio `testa` (2,0) `direzione` (1,0) `risultato` la posizione della testa si troverà in (2,1).

`Test 2`
> test_verifico_calcola_mossa_con_uscita_dal_bordo nel file test_01.py riga 17

[Vai a test_verifico_calcola_mossa_con_uscita_dal_bordo nel file ](https://github.com/AngeloSpadea/Prog_Snake/blob/main/test_01.py#L17)

Nel Test verifichiamo cosa succede se la testa del serpente esce fuori dal bordo del campo. I paramentri di ingresso di calcolo mossa sono il `corpo` composto dalla sola testa nella posizione (3,5), la `direzione` che deve prendere il serpente in questo caso nord-est rappresentato dal vettore (1,1) e infine le `dimensioni del campo` prima le righe 4 e poi le collone 6. La nuova `posizione` calcolata dalla funzione dovrebbe essere (4,6) ma considerando che le collone sono 6 partendo da 0 la posizione (4,6) non è accettabile perchè il serpente `attraverserà il bordo` e si ritrovarà dall'altra parte nel campo, `posizione` (0,0).

### Funzioni principali di gestione_input

[Vai a gestione_input.py ](https://github.com/AngeloSpadea/Prog_Snake/blob/main/gestione_input.py)

[✓] Implementazione carico_dati<br>
[✓] Implementazione restituisco_dati<br>
100%|██████████████████████████████| 2/2 [00:00 Sep 18 2023, Commits: 16,17]<br>
`Descrizione`

___
11 __carico_dati (Angelo)__
> il nome della funzione è `def carico_dati(parametri):` che si trova nel file `gestione_input.py` alla riga 10

[Vai alla funzione carico_dati ](https://github.com/AngeloSpadea/Prog_Snake/blob/main/gestione_input.py#L10)

[✓] Implementazione Test<br>
100%|██████████████████████████████| 1/1 [00:00 Sep 18 2023, Commits: 19 ]<br>
`Descrizione`
Funzione che dato il file json restituisce le liste necessarie per la gestione del gioco

___
12 __restituisco_dati (Antonio)__
> il nome della funzione è `def restituisco_dati(parametri):` che si trova nel file `gestione_input.py` alla riga 40

[Vai alla funzione restituisco_dati ](https://github.com/AngeloSpadea/Prog_Snake/blob/main/gestione_input.py#L40)

[✓] Implementazione Funzione<br>
[✗] Implementazione Test<br>
 50%|███████████████---------------| 1/2 [00:00 ___________, Commits: _ ]<br>
  `Descrizione`
  Funzione che restituisce i dati finali


### Main (Angelo)

[Vai a nel main.py ](https://github.com/AngeloSpadea/Prog_Snake/blob/main/main.py)

[✗] Implementazione Funzione<br>
[✗] Implementazione Test<br>
  20%|██████------------------------| 0/2 [00:00 Sep  6 2023, Commits: 1 ]<br>
  `Descrizione`


## Note
Bisogna gestire ancora quando la testa atraversa il corpo<br>
Opzioni<br> 
    1 --> Scrittura di una nuova funzione<br>
    2 --> Inserimento all'interno di Controlla<br>