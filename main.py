# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 17:56:12 2023

@author: angel
"""

import gestione_input as gi
import funzioni_gioco as fg

    
def play(game_file: str) -> int:
    #prendo i dati dai file di gioco
    start, mosse, food, blocks, righe, colonne, field_out = gi.carico_dati(game_file)
    
    #gioco secondo i dati di gioco ottenuti
    corpo, scia_serpente, food, blocks, righe, colonne = fg.gioca(start, mosse, food, blocks, righe, colonne)
    
    #restituisco i risultati
    lunghezza_serpente = gi.restituisco_dati(corpo, scia_serpente, food, blocks, righe, colonne, field_out)
    print(lunghezza_serpente) 
    return lunghezza_serpente

if __name__ == '__main__':    
    game_file=input("Inserisci il nome del file di gioco:\n")
    lunghezza_serpente=play(game_file)