from PIL import Image
import json
import os

# Specifica la cartella in cui sono presenti le immagini
cartella_immagini = "C:/Users/Antonio/Desktop/Progetto_Ianello/Prog_Snake/data/field"

# Ottenere una lista di tutti i file nella cartella
elenco_file = os.listdir(cartella_immagini)

# Itera su ogni file nella cartella
for file in elenco_file:
    if file.endswith(".jpg") or file.endswith(".png"):  # Puoi aggiungere altri formati di file se necessario
        # Crea il percorso completo del file
        percorso_file = os.path.join(cartella_immagini, file)
        
        # Carica l'immagine
        image = Image.open(percorso_file)
        
        # Estrai le dimensioni dell'immagine
        cols, rows = image.size  # Inverti le colonne con le righe
        
        # Inizializza le liste per il cibo e i blocchi
        food = []
        blocks = []
        
        # Scansiona l'immagine pixel per pixel
        for y in range(rows):  # Inverti la scansione delle colonne e delle righe
            for x in range(cols):  # Inverti la scansione delle colonne e delle righe
                pixel_color = image.getpixel((x, y))  # Inverti le coordinate x e y
                
                if pixel_color == (255, 128, 0):  # Colore del cibo
                    food.append([y, x])  # Inverti completamente le coordinate
                elif pixel_color == (255, 0, 0):  # Colore del blocco
                    blocks.append([y, x])  # Inverti completamente le coordinate
        
        # Crea il dizionario JSON per questa immagine
        dati_immagine = {
            "rows": rows,  # Inverti le colonne con le righe
            "cols": cols,  # Inverti le colonne con le righe
            "food": food,
            "blocks": blocks
        }
        
        # Costruisci il nome del file JSON basato sul nome del file di origine
        nome_file_json = os.path.splitext(file)[0] + ".json"
        
        # Salva i dati in un file JSON separato
        with open(os.path.join(cartella_immagini, nome_file_json), "w") as json_file:
            json.dump(dati_immagine, json_file, indent=2)

