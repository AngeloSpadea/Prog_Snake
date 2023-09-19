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
        'N': [0, -1],
        'S': [0, 1],
        'E': [1, 0],
        'W': [-1, 0],
        'NE': [1, -1],
        'NW': [-1, -1],
        'SE': [1, 1],
        'SW': [-1, 1]
    }
    mosse_senza_spazi = mosse.split() 
    mosse_convertite = [direzioni[m] for m in mosse_senza_spazi]
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
    nuova_posizione = [(corpo[0][0] + mossa[0]) % colonne, (corpo[0][1] + mossa[1]) % righe]
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
    condizione = False
    if posizione_nuova in blocks:
        condizione = True
    elif posizione_nuova in food:
        corpo, scia_serpente = mangia(corpo, scia_serpente, posizione_nuova, food)
        print("Il serpente ha mangiato il cibo!")
    else:
        corpo, scia_serpente = muovi(corpo, scia_serpente, posizione_nuova)
        print("mi sono mosso")
    return corpo, scia_serpente, condizione

def mangia(corpo, scia_serpente, posizione_nuova, food):
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
    food.remove(posizione_nuova)
    coda = corpo[-1]
    scia_serpente.insert(0,coda)
    corpo.remove(coda)
    corpo = [posizione_nuova,posizione_nuova]+corpo
    print(f"il corpo è:{corpo} e la scia è: {scia_serpente}")
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
    sys.exit(f"Gioco terminato.\n La lunghezza del serpente è di {lunghezza_serpente} quadrato/i")

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
    #corpo, scia_serpente = controlla(corpo, scia_serpente, start, mosse, food, blocks, righe, colonne)    
    for mossa in mosse_convertite:
        posizione_nuova = calcola_mossa(corpo, mossa, righe, colonne)
        corpo, scia_serpente, condizione = controlla(corpo, scia_serpente, posizione_nuova, mosse, food, blocks, righe, colonne)
        if condizione:
            break
    #print(f"La scia del serpente è:{corpo},   {scia_serpente}")
    return corpo, scia_serpente, food, blocks, righe, colonne