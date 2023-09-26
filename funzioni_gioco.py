# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 16:44:07 2023

@author: angel
"""

def converti_mosse(mosse):
    """
    Funzione che converte tutte le mosse scritte nella forma dei punti cardinali
    nella forma vettoriale [a,b] dove a e b rappresentano lo spostamentamento 
    rispettivamente nelle righe e nelle colonne.

    Parameters
    ----------
    mosse : list 
        lista delle mosse scritte nella forma dei punti cardinali (es. [N, W, ...]).

    Returns
    -------
    mosse_convertite : list
        lista delle mosse scritte nella forma vettoriale (es. [[-1, 0],[0,-1], ...]).

    """
    direzioni = {
        'N': [-1, 0],
        'S': [1, 0],
        'E': [0, 1],
        'W': [0, -1],
        'NE': [-1, 1],
        'NW': [-1, -1],
        'SE': [1, 1],
        'SW': [1, -1]
    }
    mosse_senza_spazi = mosse.split() 
    mosse_convertite = [direzioni[m] for m in mosse_senza_spazi]
    return mosse_convertite    

def calcola_mossa(corpo, mossa, righe, colonne):
    """
    Funzione che calcola la nuova posizione della testa tenendo conto della 
    dimensione del campo da gioco.
    La funzione gestisce anche il caso in cui il serpente, oltrepassando un bordo del campo, 
    riappare dal bordo opposto.

    Parameters
    ----------
    corpo : list
        lista di tutte le caselle occupate dal corpo del serpente.
    mossa : list
        lista di due elementi dove il primo rappresenta lo spostamento sulle righe
        mentre il sencondo lo spostamento sulle colonne.
    righe : int 
        numero di righe del campo di gioco.
    colonne : int
        numero di colonne del campo di gioco.

    Returns
    -------
    nuova_posizione: list
        lista di due elementi che rappresenta la riga e la colonna della nuova
        posizione della testa.

    """
    nuova_posizione = [(corpo[0][0] + mossa[0]) % righe, (corpo[0][1] + mossa[1]) % colonne]
    return nuova_posizione
    
def controlla(corpo, scia_serpente, posizione_nuova, food, blocks, mossa):
    """
    Funzione che controlla se il serpente si scontra contro la sua stessa coda attraversando il suo corpo.
    Se ciò è verificato, il gioco deve terminare. Altrimenti controlla se posizione_nuova è:
        1) un blocco ("block"): allora il gioco deve terminare.
        2) un cibo ("food"): allora il serpente deve mangiare e crescere di
                             dimensione.
        3) una casella vuota: allora il serpente si muove.

    Parameters
    ----------
    corpo : list
        lista di tutte le caselle occupate dal corpo del serpente.
    scia_serpente : list
        lista di tutte le caselle in cui il corpo del serpente è passato.
    posizione_nuova : list
        lista di due elementi che rappresenta la riga e la colonna della nuova
        posizione della testa.
    food : list
        lista di caselle che contengono il cibo nel campo da gioco.
    blocks : list
        lista di caselle che sono blocchi nel campo da gioco.
    mossa : list
        lista di due elementi dove il primo rappresenta lo spostamento sulle righe
        mentre il sencondo lo spostamento sulle colonne.

    Returns
    -------
    corpo : list
        lista di tutte le caselle occupate dal corpo del serpente.
    scia_serpente : list
        lista di tutte le caselle in cui il corpo del serpente è passato.
    condizione : bool
        valore booleano che indica se il gioco deve terminare o no 
        (True se il serpente colpisce un blocco, altrimenti False).
    """
    condizione = False
    segmento1, segmento2 = scontro_coda(posizione_nuova, mossa)
    if posizione_nuova in blocks or posizione_nuova in corpo[:len(corpo)-1] or (segmento1 in corpo and segmento2 in corpo):
        condizione = True
    elif posizione_nuova in food:
        corpo, scia_serpente = mangia(corpo, scia_serpente, posizione_nuova, food)
        print("Il serpente ha mangiato il cibo!")
    else: #se la posizione nuova non è nè un cibo nè un blocco allora vuol dire che è vuoto quindi mi ci sposto
        corpo, scia_serpente = muovi(corpo, scia_serpente, posizione_nuova)
        print("mi sono mosso")
    return corpo, scia_serpente, condizione

def mangia(corpo, scia_serpente, posizione_nuova, food):
    """
    Funzione che fa mangiare al serpente il cibo e, muovendolo nella nuova casella, lo fa crescere di dimensioni.
    Il cibo, una volta mangiato viene rimosso dalla lista del cibo.
    La funzione tiene traccia delle posizioni precedenti attraverso le quali il serpente è passato, 
    aggiornando la sua scia.

    Parameters
    ----------
    corpo : list
        lista di tutte le caselle occupate dal corpo del serpente.
    scia_serpente : list
        lista di tutte le caselle in cui il corpo del serpente è passato.
    posizione_nuova : list
        lista di due elementi che rappresenta la riga e la colonna della nuova
        posizione della testa.
    food : list
        lista di caselle che contengono il cibo nel campo da gioco.

    Returns
    -------
    corpo : list
        lista di tutte le caselle occupate dal corpo del serpente aggiornata.
    scia_serpente : list
        lista di tutte le caselle in cui il corpo del serpente è passato aggiornata.

    """
    food.remove(posizione_nuova)
    coda = corpo[-1]
    scia_serpente.insert(0,coda)
    corpo.remove(coda)
    corpo = [posizione_nuova]+corpo+[coda]
    print(f"il corpo è:{corpo} e la scia è: {scia_serpente}")
    return corpo, scia_serpente

def muovi(corpo, scia_serpente, posizione_nuova):
    """
    Funzione che fa muovere il serpente e tiene traccia delle posizioni precedenti attraverso 
    le quali il serpente è passato, aggiornando la sua scia.

    Parameters
    ----------
    corpo : list
        lista di tutte le caselle occupate dal corpo del serpente.
    scia_serpente : list
        lista di tutte le caselle in cui il corpo del serpente è passato.
    posizione_nuova : list
        lista di due elementi che rappresenta la riga e la colonna della nuova
        posizione della testa.

    Returns
    -------
    corpo : list
        lista di tutte le caselle occupate dal corpo del serpente aggiornata.
    scia_serpente : list
        lista di tutte le caselle in cui il corpo del serpente è passato aggiornata.

    """
    coda = corpo.pop(-1)
    scia_serpente.insert(0,coda) 
    corpo = [posizione_nuova]+corpo
    print(f"il corpo è:{corpo} e la scia è: {scia_serpente}")
    return corpo, scia_serpente

def scontro_coda(posizione_nuova, mossa):
    """
    Funzione che controlla se il serpente si scontra con la sua coda, tentando di attraversarla.
    Per verificare se il serpente tenta di attraversare la sua coda in direzione diagonale,
    sono stati calcolati:
        segmento1: quadratino adiacente lungo le ordinate a posizione_nuova 
            (traslato orizzontalmente rispetto a posizione_nuova secondo l'ascissa di mossa)
        segmento2: quadratino adiacente lungo le ascisse a posizione_nuova 
            (traslato verticalmente rispetto a posizione_nuova secondo l'ordinata di mossa)
    Se segmento1 e segmento2 appartengono al corpo del serpente, il gioco deve terminare.
    
    Parameters
    ----------
    posizione_nuova : list
        lista di due elementi che rappresentano la riga e la colonna della nuova
        posizione della testa.
    mossa : list
        lista di due elementi dove il primo rappresenta lo spostamento sulle righe
        mentre il sencondo lo spostamento sulle colonne.

    Returns
    -------
    segmento1: list
        lista di due elementi che rappresentano la riga e la colonna del quadratino adiacente lungo le 
        ordinate a posizione_nuova 
    segmento2: list
        lista di due elementi che rappresentano la riga e la colonna del quadratino adiacente lungo le 
        ascisse a posizione_nuova

    """
    segmento1 = [posizione_nuova[0] - mossa[1], posizione_nuova[1]]
    segmento2 = [posizione_nuova[0], posizione_nuova[1] - mossa[0]]
    return segmento1, segmento2

def gioca(start, mosse, food, blocks, righe, colonne):
    """
    Funzione che gestisce il gioco: 
    1) converte le mosse da punti cardinali nella forma vettoriale.
    2) controlla se la posizione iniziale è una casella valida e per ogni mossa.
    3) calcola la nuova posizione che occuperà la testa del serpente. 
    gestendo anche il caso in cui esso oltrepassi un bordo del campo da gioco.
    4) controlla la nuova posizione che occuperà la testa del serpente e gestisce le seguenti situazioni:
        - se la casella è vuota, il serpente si muove.
        - se la casella è occupata da un cibo, il serpente mangia.
        - se la casella è un blocco o se il serpente attraversa sè stesso, il gico termina. 

    Parameters
    ---------
    start : list
        lista di due elementi che rappresentano la riga e la colonna della 
        posizione iniziale del serpente.
    mosse : list 
        lista delle mosse scritte nella forma dei punti cardinali (es. [N, W, ...]).
    food : list
        lista di caselle che contengono il cibo nel campo da gioco.
    blocks : list
        lista di caselle che sono blocchi nel campo da gioco.
    righe : int 
        numero di righe del campo di gioco.
    colonne : int
        numero di colonne del campo di gioco.

    Returns
    -------
    corpo : list
        lista di tutte le caselle occupate dal corpo del serpente aggiornata.
    scia_serpente : list
        lista di tutte le caselle in cui il corpo del serpente è passato aggiornata.
    food : list
        lista di caselle che contengono il cibo nel campo da gioco.
    blocks : list
        lista di caselle che sono blocchi nel campo da gioco.
    righe : int 
        numero di righe del campo di gioco.
    colonne : int
        numero di colonne del campo di gioco.

    """
    mosse_convertite = converti_mosse(mosse)
    scia_serpente=[]
    corpo=[start]
    #corpo, scia_serpente = controlla(corpo, scia_serpente, start, mosse, food, blocks, righe, colonne)    
    for mossa in mosse_convertite:
        posizione_nuova = calcola_mossa(corpo, mossa, righe, colonne)
        corpo, scia_serpente, condizione = controlla(corpo, scia_serpente, posizione_nuova, food, blocks, mossa)
        if condizione:
            break
    return corpo, scia_serpente, food, blocks, righe, colonne