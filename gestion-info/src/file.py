import json
import os
from typing import List, Dict, Any

# Locate records.json in the data/ directory (relative to project root)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
DATA_FILE = os.path.join(DATA_DIR, "records.json")

def load_data() -> List[Dict[str, Any]]:
    """Loads records from the JSON file. Returns an empty list if file doesn't exist or is corrupted."""
    if not os.path.exists(DATA_FILE):
        return []
    
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            return []
    except (json.JSONDecodeError, IOError) as e:
        print(f"Advertencia: El archivo de datos está dañado o no se puede leer. Iniciando con lista vacía. ({e})")
        return []

def save_data(data: List[Dict[str, Any]]) -> bool:
    """Saves records to the JSON file. Creates the directory if it doesn't exist."""
    try:
        os.makedirs(DATA_DIR, exist_ok=True)
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        return True
    except IOError as e:
        print(f"Error crítico: No se pudo guardar la información en el archivo. ({e})")
        return False
