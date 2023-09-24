from PIL import Image
import json
import os

def convert_image_to_json(image_path):
    # Carica l'immagine
    image = Image.open(image_path)

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
    nome_file_json = os.path.splitext(os.path.basename(image_path))[0] + ".json"

    # Salva i dati in un file JSON separato nella stessa directory dell'immagine
    json_file_path = os.path.join(os.path.dirname(image_path), nome_file_json)
    with open(json_file_path, "w") as json_file:
        json.dump(dati_immagine, json_file, indent=2)

    return json_file_path
