# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 16:44:07 2023

@author: angel
"""
import sys

def converti_mosse(mosse):
    """
    Funzione che converte tutte le mosse scritte nella forma dei punti cardinali
    nella forma vettoriale [a,b] dove a e b rappresentano lo spostamentamento 
    rispettivamente nelle righe e nelle colonne

    Parameters
    ----------
    mosse : list 
        lista delle mosse scritte nella forma dei punti cardinali (es. [N, W, ...])

    Returns
    -------
    mosse_convertite : list
        lista delle mosse scritte nella forma vettoriale (es. [[-1, 0],[0,-1], ...])

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
    mosse_convertite = [direzioni[m] for m in mosse]
    return mosse_convertite    

def calcola_mossa(corpo, mossa, righe, colonne):
    """
    Funzione che calcola la nuova posizione della testa tenendo conto della 
    dimensione del campo da gioco

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
        posizione della testa

    """
    nuova_posizione = [(corpo[0][0] + mossa[0]) % righe, (corpo[0][1] + mossa[1]) % colonne]
    return nuova_posizione
    
def controlla(corpo, scia_serpente, posizione_nuova, mosse, food, blocks, righe, colonne):
    """
    Funzione che controlla se la posizione nuova è:
        1) un blocco ("block"): allora il gioco deve terminare
        2) una cibo ("food"): allora il serpente deve mangiare e crescere di 
                              dimensione
        3) casella vuota: allora il serpente si muove

    Parameters
    ----------
    corpo : list
        lista di tutte le caselle occupate dal corpo del serpente.
    scia_serpente : list
        lista di tutte le caselle in cui il corpo del serpente è passato.
    posizione_nuova : list
        lista di due elementi che rappresenta la riga e la colonna della nuova
        posizione della testa
    campo_da_gioco : file json
        un file nel quale sono contenute le informazione del campo da gioco, 
        della posizione iniziale, la lista delle mosse e il file su cui salvare
        l'immagine finale.

    Returns
    -------
    corpo : list
        lista di tutte le caselle occupate dal corpo del serpente.
    scia_serpente : list
        lista di tutte le caselle in cui il corpo del serpente è passato.
    """
    pass

def mangia(corpo, scia_serpente, posizione_nuova , campo_da_gioco):
    """
    Funzione che fa mangiare al serpente il cibo, il quale viene rimosso dalla 
    lista del cibo.

    Parameters
    ----------
    corpo : list
        lista di tutte le caselle occupate dal corpo del serpente.
    scia_serpente : list
        lista di tutte le caselle in cui il corpo del serpente è passato.
    posizione_nuova : list
        lista di due elementi che rappresenta la riga e la colonna della nuova
        posizione della testa
    campo_da_gioco : file json
        un file nel quale sono contenute le informazione del campo da gioco, 
        della posizione iniziale, la lista delle mosse e il file su cui salvare
        l'immagine finale.


    Returns
    -------
    corpo : list
        lista di tutte le caselle occupate dal corpo del serpente aggiornata.
    scia_serpente : list
        lista di tutte le caselle in cui il corpo del serpente è passato aggiornata.

    """
    campo_da_gioco["food"].remove(posizione_nuova)
    coda = corpo[-1]
    scia_serpente.insert(0,coda)
    corpo.remove(coda)
    corpo = [posizione_nuova,posizione_nuova]+corpo
    return corpo, scia_serpente

def muovi(corpo, scia_serpente, posizione_nuova):
    """
    Funzione che fa muovere il serpente

    Parameters
    ----------
    corpo : list
        lista di tutte le caselle occupate dal corpo del serpente.
    scia_serpente : list
        lista di tutte le caselle in cui il corpo del serpente è passato.
    posizione_nuova : list
        lista di due elementi che rappresenta la riga e la colonna della nuova
        posizione della testa
    campo_da_gioco : file json
        un file nel quale sono contenute le informazione del campo da gioco, 
        della posizione iniziale, la lista delle mosse e il file su cui salvare
        l'immagine finale.


    Returns
    -------
    corpo : list
        lista di tutte le caselle occupate dal corpo del serpente aggiornata.
    scia_serpente : list
        lista di tutte le caselle in cui il corpo del serpente è passato aggiornata.

    """
    coda = corpo.pop(-1)
    scia_serpente.insert(0,coda) 
    corpo.append(posizione_nuova)
    print(f"il corpo è:{corpo} e la scia è: {scia_serpente}")
    return corpo, scia_serpente

def termina(lunghezza_serpente):
    """
    Funzione che fa terminare il gioco

    Parameters
    ----------
    lunghezza_serpente : int
        lunghezza del serpente.

    Returns
    -------
    La lunghezza del serpente.

    """    
    sys.exit(f"GAME OVER. \n La lunghezza del serpente è di {lunghezza_serpente} quadrato/i")

def play(start, mosse, food, blocks, righe, colonne):
    """
    Funzione che gestisce il gioco: converte le mosse, controlla se la 
    posizione iniziale è una casella valida e per ogni mossa gestisce se il 
    serpente deve muoversi, mangiare o se il serpente si blocca facendo 
    terminare così il gioco.

    Parameters
    ---------
    start : list
        lista di due elementi che rappresentano la riga e la colonna della 
        posizione iniziale del serpente.
    mosse : list 
        lista delle mosse scritte nella forma dei punti cardinali (es. [N, W, ...])
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

    """
    mosse_convertite = converti_mosse(mosse)
    scia_serpente=[]
    corpo=[start]
    corpo, scia_serpente = controlla(corpo, scia_serpente, start, mosse, food, blocks, righe, colonne)    
    for mossa in mosse_convertite:
        posizione_nuova = calcola_mossa(corpo, mossa, righe, colonne)
        corpo, scia_serpente = controlla(corpo, scia_serpente, posizione_nuova, mosse, food, blocks, righe, colonne)
    print(f"La scia del serpente è:{corpo},   {scia_serpente}")
    return corpo, scia_serpente