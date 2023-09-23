# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 18:00:31 2023

@author: angel
"""

import json
from PIL import Image

def carico_dati(game_file):
    """
    Funzione che legge i dati da un file JSON specificato e restituisce una tupla 
    contenente diverse liste di dati che saranno utilizzati all'interno del programma 
    principale del gioco per la gestione dello stesso.

    Parameters
    ----------
    game_file : file json
        un file nel quale sono contenute le informazione del campo da gioco, 
        della posizione iniziale, la lista delle mosse e il file su cui salvare
        l'immagine finale.

    Returns
    -------
    una tupla con le liste dei dati estratti: start, mosse, food, blocks, righe, colonne, field_out.

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

def restituisco_dati(corpo, scia_serpente, food, blocks, righe, colonne, final_field):
    """
    Funzione che restituisce la lunghezza del serpente e che genera un'immagine 
    rappresentativa dello stato finale del gioco.
    Crea una rappresentazione visiva dell'ultima configurazione del gioco, dove 
    il serpente è tracciato in verde, il cibo in arancione, i blocchi in rosso 
    e la scia del serpente in grigio su uno sfondo nero.
    Questi dati possono essere utilizzati per valutare l'evoluzione del gioco.  

    Parameters
    ----------
    final_field : json
        il file finale de gioco nel quale sono contenute le informazione del 
        campo da gioco, della posizione iniziale, la lista delle mosse e il 
        file su cui salvare l'immagine finale.

    Returns
    -------
    lunghezza_serpente: int
        numero di quadratini occupati dal serpente alla fine del gioco.

    """
    lunghezza_serpente= len(corpo)    

    black_image = Image.new("RGB", (colonne, righe), (0, 0, 0))
    
    for x, y in scia_serpente:
        black_image.putpixel((y, x), (128, 128, 128))
    
    for x, y in corpo:
        black_image.putpixel((y, x), (0, 255, 0))          
    
    for x, y in food:
        black_image.putpixel((y, x), (255, 128, 0))
    
    for x, y in blocks:
        black_image.putpixel((y, x), (255, 0, 0))
    
    black_image.save(final_field)
    return lunghezza_serpente