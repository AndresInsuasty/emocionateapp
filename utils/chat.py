from openai import OpenAI


def send_message(message: str) -> str:
    """Analiza el mensaje recibido con OpenAI y devuelve la clasificación de emoción.
    
    Clasifica la emoción en una de las siguientes categorías:
    - tristeza
    - alegria
    - ira
    - sorpresa
    - asco
    - miedo
    - neutral
    """
    client = OpenAI()
    
    system_prompt = """Eres un analizador de emociones. Analiza el texto recibido y devuelve SOLO 
    la emoción principal detectada en una de estas categorías: tristeza, alegria, ira, sorpresa, asco, miedo, neutral.
    
    Responde con SOLO una palabra: la emoción detectada. No incluyas explicaciones ni otros textos."""
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": message}
        ],
        temperature=0.3
    )
    
    emotion = response.choices[0].message.content.strip().lower()
    return emotion

def save_label(message: str, label: str, filename: str = "labels.csv"):
    """Guarda el mensaje y su etiqueta en un archivo CSV."""
    import csv
    from os.path import exists
    from datetime import datetime

    file_exists = exists(filename)
    
    with open(filename, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["message", "label", "date"])  # Escribir encabezados si el archivo no existe
        date = datetime.now().isoformat()
        writer.writerow([message, label, date])