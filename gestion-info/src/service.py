from typing import Dict, List, Any
from src.validate import validate_non_empty_string, validate_positive_integer
from src.file import load_data, save_data

# In-memory storage for Módulo 1 & 2
records: List[Dict[str, Any]] = load_data()

# Set for unique IDs
existing_ids = {str(r["id"]) for r in records if "id" in r}

def create_record(record_id: str, name: str, age: str) -> bool:
    """Creates a new record after validating inputs and ensuring ID uniqueness."""
    
    # Validations
    if not validate_non_empty_string(record_id):
        print("Error: El ID no puede estar vacío.")
        return False
        
    if not validate_non_empty_string(name):
        print(f"Error: El nombre no puede estar vacío (ID: {record_id}).")
        return False
        
    if not validate_positive_integer(age):
        print(f"Error: La edad debe ser un número entero positivo (ID: {record_id}).")
        return False
        
    # Uniqueness check using sets
    if record_id in existing_ids:
        print(f"Error: Ya existe un registro con el ID {record_id}.")
        return False
        
    # Create and store record
    record = {
        "id": record_id,
        "name": name,
        "age": int(age)
    }
    
    records.append(record)
    existing_ids.add(record_id)
    
    # Save to file
    save_data(records)
    
    print(f"Éxito: Registro {record_id} creado.")
    return True

def get_all_records() -> List[Dict[str, Any]]:
    """Returns all records currently in memory."""
    return records
