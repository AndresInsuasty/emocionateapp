"""Módulo para gestionar archivos relacionados con el etiquetado de mensajes."""

import csv
from os.path import exists
from datetime import datetime


def save_label(message: str, label: str, filename: str = "labels.csv"):
    """Guarda el mensaje y su etiqueta en un archivo CSV."""

    file_exists = exists(filename)
    with open(filename, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        if not file_exists:
            # Escribir encabezados si el archivo no existe
            writer.writerow(["message", "label", "date"])
        date = datetime.now().isoformat()
        writer.writerow([message, label, date])
