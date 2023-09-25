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
Verrà cosi avviato il programma con le impostazioni base per caricare la bartita. Copiare il percorso della partita che si vuole caricare e premere invio. All'interno di data troverete gli 8 gamefile di base piu 4 creati da noi per testare alcune funzionalita

Le specifiche per ora implementate sono le seguenti<br>

1  [✓]  La testa del serpente può muoversi nelle otto direzioni stabilite da consegna<br>
2  [✓]  Oltrepassando un bordo del campo, il serpente riappare dal bordo opposto<br>
3  [✓]  Quando il serpente “mangia” cibo il suo corpo cresce di un quadratino<br>
4  [✓]  Quando il serpente si scontra con un ostacolo, il gioco termina<br>
5  [✓]  Quando il serpente si scontra contro la sua stessa coda, il gioco termina. Ciò vale anche quando il serpente tenta di attraversare la sua coda in direzione diagonale<br>


___
-------   `AVVERTENZA`   -------
Se si vogliono testare le funzionalita implementate modificare i test tenere conto però che nella rappresentazione dei punti [i,j] `i` rappresente la `colonna` mentre `j` rappresenta la `riga`
___

# Avanzamento del progetto 

## Indice
[Utility](#103)
  [Docker](#105)
  [Readme](#109)
  [gitignore](#120)
[Funzioni principali di Funzioni_gioco](#funzioni-principali-di-funzioni_gioco-1)
  [gioca](#130)
  [converti mosse](#145)
  [controlla](#182)
  [scontro coda](#197)
[Funzioni Secondarie di Controlla](#funzioni-secondarie-di-controlla-1)
  [mangia](#236)
  [muovi](#266)
[Funzioni Secondarie di gioca](#funzioni-secondarie-di-gioca)
  [controlla mossa](#315)
[Funzioni principali di gestione_input](#funzioni-principali-di-gestione_input-1)
  [carico dati](#356)
  [restituisco dati](#367)
[Main](#main-angelo-1)

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
4 __gioca(Angelo)__
> il nome della funzione è `def play(parametri):` che si trova nel file `funzioni_gioco.py` alla riga 214

[Vai alla funzine play() ](https://github.com/AngeloSpadea/Prog_Snake/blob/main/funzioni_gioco.py#L214)

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
> il nome della funzione è `def converti_mosse(parametri):` che si trova nel file `funzioni_gioco.py` alla riga 8

e[Vai alla funzione converti_mosse() ](https://github.com/AngeloSpadea/Prog_Snake/blob/main/funzioni_gioco.py#L8)

[✓] Implementazione Funzione<br>
[✓] Implementazione Test<br>
100%|██████████████████████████████| 2/2 [00:00 Sep 15 2023, Commits: 5,6 ]<br>
`Descrizione`

Funzione che converte tutte le mosse scritte nella forma dei punti cardinali
nella forma vettoriale [a,b] dove a e b rappresentano lo spostamentamento 
rispettivamente nelle righe e nelle colonne

`Test 1`
> test_verifico_calcola_mossa nel file test_01.py riga 32

[Vai a test_corverti_mosse ](https://github.com/AngeloSpadea/Prog_Snake/blob/main/test_01.py#L32)

Verifica che la funzione converti_mosse converta correttamente la direzione verticale Nord (N).<br>
Parametri: <br>
    mosse: Nord (N) in punto cardinale.<br>
Risultato atteso:<br>
    mosse_convertite: mossa Nord in forma vettoriale.<br>

`Test 2`
> test_verifico_calcola_mossa nel file test_01.py riga 45

[Vai a test_corverti_mosse_oblique ](https://github.com/AngeloSpadea/Prog_Snake/blob/main/test_01.py#L45)

Verifica che la funzione converti_mosse converta correttamente la direzione obliqua Nord-Ovest (NW).<br>
Parametri: <br>
    mosse: Nord-Ovest (NW) in punto cardinale.<br>
Risultato atteso:<br>
    mosse_convertite: mossa Nord-Ovest in forma vettoriale.<br>

___
6 __Controlla(Antonio)__
> il nome della funzione è `def controlla(parametri):` che si trova nel file `funzioni_gioco.py` alla riga 68

[Vai alla funzione controlla() ](https://github.com/AngeloSpadea/Prog_Snake/blob/main/funzioni_gioco.py#L68)

[✓] Implementazione Funzione<br>
100%|██████████████████████████████| 1/1 <br>
`Descrizione`

Funzione che controlla se la posizione nuova è:<br>
1) un blocco ("block"): allora il gioco deve terminare<br>
2) una cibo ("food"): allora il serpente deve mangiare e crescere di dimensione<br>
3) casella vuota: allora il serpente si muove<br>

___
7 __Scontro coda(Antonio)__
> il nome della funzione è `def scontro_coda(parametri):` che si trova nel file `funzioni_gioco.py` alla riga 180

[Vai alla funzione controlla() ](https://github.com/AngeloSpadea/Prog_Snake/blob/main/funzioni_gioco.py#L180)

[✓] Implementazione Funzione<br>
[✓] Implementazione Test<br>
100%|██████████████████████████████| 2/2 <br>
`Descrizione`

Funzione che controlla se il serpente si scontra con la sua coda, tentando di attraversarla.
Per verificare se il serpente tenta di attraversare la sua coda in direzione diagonale,
sono stati calcolati:<br>
segmento1: quadratino adiacente lungo le ordinate a posizione_nuova <br>
    (traslato orizzontalmente rispetto a posizione_nuova secondo l'ascissa di mossa)<br>
segmento2: quadratino adiacente lungo le ascisse a posizione_nuova <br>
    (traslato verticalmente rispetto a posizione_nuova secondo l'ordinata di mossa)<br>
Se segmento1 e segmento2 appartengono al corpo del serpente, il gioco deve terminare.<br>

`Test 1`
> test_scontro_coda nel file test_01.py riga 122

[Vai a test_scontro_coda ](https://github.com/AngeloSpadea/Prog_Snake/blob/main/test_01.py#L122)

Verifica che la funzione scontro_coda rilevi correttamente lo scontro con la coda in direzione verticale/orizzontale.
Parametri: corpo, posizione_nuova, mossa.<br>
Risultato atteso: condizione che segnala che lo scontro è avvenuto.<br>

`Test 2`
> test_scontro_coda_direzione_diagonale nel file test_01.py riga 133

[Vai a test_scontro_coda_direzione_diagonale ](https://github.com/AngeloSpadea/Prog_Snake/blob/main/test_01.py#L133)

Verifica che la funzione scontro_coda rilevi correttamente lo scontro con la coda in direzione diagonale.<br>
Parametri: corpo, posizione_nuova, mossa.<br>
Risultato atteso: condizione che segnala che lo scontro è avvenuto.<br>

### Funzioni Secondarie di Controlla
___
8 __Mangia (Antonio)__
> il nome della funzione è `def mangia(parametri):` che si trova nel file `funzioni_gioco.py` alla riga 116

[Vai alla funzione mangia() ](https://github.com/AngeloSpadea/Prog_Snake/blob/main/funzioni_gioco.py#L116)

[✓] Implementazione Funzione<br>
[✓] Implementazione Test<br>
100%|██████████████████████████████| 2/2 [00:00 Sep 15 2023, Commits: 10,11,12 ]<br>
`Descrizione`

Funzione che fa mangiare al serpente il cibo, il quale viene rimosso dalla 
lista del cibo.

`Test 1`
> test_mangia nel file test_01.py riga 58

[Vai a test_corverti_mosse_oblique ](https://github.com/AngeloSpadea/Prog_Snake/blob/main/test_01.py#L58)

Verifica che la funzione mangia gestisca correttamente il caso in cui posizione_nuova sia occupata da un cipo.
La funzione aggiunge la nuova posizione (dove il cibo è stato mangiato) due volte all'inizio del corpo del serpente,
facendo crescere il corpo del serpente.<br>
Parametri: <br>
    corpo: un solo elemento.<br>
    scia_serpente: vuota.<br>
    posizone_nuova.<br>
    food.<br>
Risultati attesi: corpo, scia_serpente.<br>
___

9 __Muovi (Martina)__
> il nome della funzione è `def muovi(parametri):` che si trova nel file `funzioni_gioco.py` alla riga 151

[Vai alla funzione muovi() ](https://github.com/AngeloSpadea/Prog_Snake/blob/main/funzioni_gioco.py#L151)

[✓] Implementazione Funzione<br>
[✓] Implementazione Test<br>
100%|██████████████████████████████| 2/2 [00:00 Sep 16 2023, Commits: 13,14 ]<br>
`Descrizione`

Funzione che fa muovere il serpente

`Test 1`
> test_muovi_start nel file test_01.py riga 77

[Vai a test_muovi_start ](https://github.com/AngeloSpadea/Prog_Snake/blob/main/test_01.py#L77)

Verifica che la funzione muovi gestisca correttamente il movimento di partenza quando la nuova posizione è vuota.<br>
Parametri:<br>
    corpo: un solo elemento.<br>
    scia_serpente: vuota.<br>
    posizione_nuova.<br>
Risultati attesi: corpo, scia_serpente.<br>

`Test 2`
> test_muovi nel file test_01.py riga 92

[Vai a test_muovi ](https://github.com/AngeloSpadea/Prog_Snake/blob/main/test_01.py#L92)

Verifica che la funzione muovi gestisca correttamente il movimento generale.<br>
Parametri:<br>
    corpo: un solo elemento.<br>
    scia_serpente: non vuota.<br>
    posizione_nuova.<br>
Risultati attesi: corpo, scia_serpente.<br>

`Test 3`
> test_muovi_da_cresciuto nel file test_01.py riga 107

[Vai a test_muovi_da_cresciuto ](https://github.com/AngeloSpadea/Prog_Snake/blob/main/test_01.py#L107)

Verifica che la funzione muovi gestisca correttamente il movimento quando il serpente è cresciuto.<br>
Parametri:<br>
    corpo: più elementi.<br>
    scia_serpente: non vuota.<br>
    posizione_nuova.<br>
Risultati attesi: corpo, scia_serpente.<br>

### Funzioni Secondarie di gioca
___
10 __Calcolo_mossa (Martina)__
> il nome della funzione è `def calcola_mossa(parametri):` che si trova nel file `funzioni_gioco.py` alla riga 39

[Vai alla funzione calcola_mossa() ](https://github.com/AngeloSpadea/Prog_Snake/blob/main/funzioni_gioco.py#L39)

[✓] Implementazione Funzione<br>
[✓] Implementazione Test<br>
100%|██████████████████████████████| 2/2 [00:00 Sep 12 2023, Commits: 3,4 ]<br>
`Descrizione`

Funzione che calcola la nuova posizione della testa tenendo conto della dimensione del campo da gioco.

`Test 1`
> test_verifico_calcola_mossa nel file test_01.py riga 8

[Vai a test_verifico_calcola_mossa ](https://github.com/AngeloSpadea/Prog_Snake/blob/main/test_01.py#L8)

Verifica che la funzione calcola_mossa funzioni correttamente restituendo la nuova posizione.<br>
Parametri: corpo, mossa, righe, colonne.<br>
Risultato atteso: nuova posizione. <br>

`Test 2`
> test_verifico_calcola_mossa_con_uscita_dal_bordo nel file test_01.py riga 17

[Vai a test_verifico_calcola_mossa_con_uscita_dal_bordo nel file ](https://github.com/AngeloSpadea/Prog_Snake/blob/main/test_01.py#L20)

Verifica che la funzione calcola_mossa gestisca correttamente l'uscita dal bordo,
facendo ricomparire la testa del serpente dal bordo opposto.<br>
Parametri: corpo, mossa, righe, colonne.<br>
Risultato atteso: nuova_posizione.<br>

### Funzioni principali di gestione_input

[Vai a gestione_input.py ](https://github.com/AngeloSpadea/Prog_Snake/blob/main/gestione_input.py)

[✓] Implementazione carico_dati<br>
[✓] Implementazione restituisco_dati<br>
100%|██████████████████████████████| 2/2 [00:00 Sep 18 2023, Commits: 16,17]<br>
`Descrizione`

___
11 __carico_dati (Angelo)__
> il nome della funzione è `def carico_dati(parametri):` che si trova nel file `gestione_input.py` alla riga 43

[Vai alla funzione carico_dati ](https://github.com/AngeloSpadea/Prog_Snake/blob/main/gestione_input.py#L43)

[✓] Implementazione Test<br>
100%|██████████████████████████████| 1/1 [00:00 Sep 18 2023, Commits: 19 ]<br>
`Descrizione`
Funzione che dato il file json restituisce le liste necessarie per la gestione del gioco

___
12 __restituisco_dati (Antonio)__
> il nome della funzione è `def restituisco_dati(parametri):` che si trova nel file `gestione_input.py` alla riga 75

[Vai alla funzione restituisco_dati ](https://github.com/AngeloSpadea/Prog_Snake/blob/main/gestione_input.py#L75)

[✓] Implementazione Funzione<br>
[✓] Implementazione Test<br>
100%|██████████████████████████████| 1/1<br>
  `Descrizione`
  Funzione che restituisce i dati finali


### Main (Angelo)

[Vai a nel main.py ](https://github.com/AngeloSpadea/Prog_Snake/blob/main/main.py)

[✓] Implementazione Funzione<br>
100%|██████████████████████████████| 1/1 [00:00 Sep  6 2023, Commits: 1 ]<br>
  `Descrizione`
