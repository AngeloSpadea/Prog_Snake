# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 18:00:31 2023

@author: angel
"""

import json

def carico_dati(game_file):
    """
    Funzione che dato il file json restituisce le liste necessarie per la 
    gestione del gioco

    Parameters
    ----------
    game_file : file json
        un file nel quale sono contenute le informazione del campo da gioco, 
        della posizione iniziale, la lista delle mosse e il file su cui salvare
        l'immagine finale.

    Returns
    -------
    una tupla con le liste dei dati necessari.

    """
    f = open(game_file)
    game = json.load(f)
    field_out = game['field_out']
    g = open(game['field_in'])
    field = json.load(g)
    start = game['start']
    mosse = game['moves']    
    righe = field['rows']
    colonne = field['cols']
    food = field['food']
    blocks = field['blocks']        
    return start, mosse, food, blocks, righe, colonne, field_out

def restituisco_dati(final_field):
    """
    Funzione che restituisce i dati finali

    Parameters
    ----------
    final_field : json
        il file finale de gioco nel quale sono contenute le informazione del 
        campo da gioco, della posizione iniziale, la lista delle mosse e il 
        file su cui salvare l'immagine finale.

    Returns
    -------
    None.

    """
    pass