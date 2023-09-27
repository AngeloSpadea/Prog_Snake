from PIL import Image
import json
import os

def convert_image_to_json(image_path):
    """
    Funzione che a partire da un'immagine costrusice il file JSON

    Parameters
    ----------
    image_path : str
        percorso del file dell'immagine con estensione .png

    Returns
    -------
    json_file_path : str
        persocorso del file JSON.

    """
    # Carica l'immagine
    image = Image.open(image_path)

    # Estrai le dimensioni dell'immagine
    cols, rows = image.size

    # Inizializza le liste per il cibo e i blocchi
    food = []
    blocks = []

    # Scansiona l'immagine pixel per pixel
    for y in range(rows):
        for x in range(cols):
            pixel_color = image.getpixel((x, y))

            if pixel_color == (255, 128, 0):
                food.append([y, x]) 
            elif pixel_color == (255, 0, 0):
                blocks.append([y, x])

    # Crea il dizionario JSON per questa immagine
    dati_immagine = {
        "rows": rows,
        "cols": cols,  
        "food": food,
        "blocks": blocks
    }

    # Costruisci il nome del file JSON basato sul nome del file di origine
    nome_file_json = os.path.splitext(os.path.basename(image_path))[0] + ".json"

    # Salva i dati in un file JSON separato nella stessa directory dell'immagine
    json_file_path = os.path.join(os.path.dirname(image_path), nome_file_json)
    with open(json_file_path, "w") as json_file:
        json.dump(dati_immagine, json_file, indent=2)

    return json_file_path
