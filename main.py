# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 17:56:12 2023

@author: angel
"""

import gestione_input as gi
import funzioni_gioco as fg

#prendo i dati dai file di gioco
start, mosse, food, blocks, righe, colonne, field_out = gi.carico_dati('Prog_Snake/file_gioco.json')

#gioco secondo i dati di gioco ottenuti
corpo, scia_serpente, food, blocks, righe, colonne = fg.play(start, mosse, food, blocks, righe, colonne)

#restituisco i risultati
gi.restituisco_dati(corpo, scia_serpente, food, blocks, righe, colonne, field_out)