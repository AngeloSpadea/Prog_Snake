# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 17:56:12 2023

@author: angel
"""

import gestione_input as gi
import funzioni_gioco as fg

#prendo i dati dai file di gioco
start, mosse, food, blocks, righe, colonne, field_out = gi.carico_dati('file_gioco.json')

#gioco secondo i dati di gioco ottenuti
final_field = fg.play(start, mosse, food, blocks, righe, colonne)

#restituisco i risultati
gi.restituisco_dati(field_out)