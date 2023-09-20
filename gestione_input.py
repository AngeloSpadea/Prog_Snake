# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 18:00:31 2023

@author: angel
"""

import json
from PIL import Image

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
    g = open('Prog_Snake/'+game['field_in'])
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
    lunghezza_serpente= len(corpo)
    print(lunghezza_serpente)

    black_image = Image.new("RGB", (colonne, righe), (0, 0, 0))
    
    for x, y in scia_serpente:
        black_image.putpixel((y, x), (128, 128, 12))
    
    for x, y in corpo:
        black_image.putpixel((y, x), (0, 255, 0))          
    
    for x, y in food:
        black_image.putpixel((y, x), (255, 128, 0))
    
    for x, y in blocks:
        black_image.putpixel((y, x), (255, 0, 0))
    
    black_image.save("Prog_Snake/output/"+final_field)