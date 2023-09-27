# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 17:56:12 2023

@author: angel
"""

import gestione_input as gi
import funzioni_gioco as fg

    
def play(game_file: str) -> int:
    """
    Funzione principale del programma che:
        - carica i dati di gioco dal file specificato;
        - consente di giocare utilizzando i dati di gioco ottenuti;
        - restituisce la lunghezza del serpente quando il gioco è terminato.

    Parameters
    ----------
    game_file: str 
        nome del file di gioco. I file di gioco si trovano nella directory data
        esempio di stringa ("data/gamefile_01.json")
        
    Returns
    -------
    lunghezza_serpente: int
        Lunghezza del serpente alla fine del gioco.

    """
    start, mosse, food, blocks, righe, colonne, field_out = gi.carico_dati(game_file)
    
    corpo, scia_serpente, food, blocks, righe, colonne = fg.gioca(start, mosse, food, blocks, righe, colonne)
    
    lunghezza_serpente = gi.restituisco_dati(corpo, scia_serpente, food, blocks, righe, colonne, field_out)
    print(f"La lunghezza del serpente alla fine del gioco è: {lunghezza_serpente}") 
    return lunghezza_serpente

if __name__ == '__main__':    
    game_file=input("Inserisci il nome del file di gioco:\n")
    lunghezza_serpente=play(game_file)