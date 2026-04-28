from typing import Dict, List, Any
from src.validate import validate_non_empty_string, validate_positive_integer
from src.file import load_data, save_data

# In-memory storage
records: List[Dict[str, Any]] = load_data()
existing_ids = {str(r["id"]) for r in records if "id" in r}

def new_register(record_id: str, name: str, age: str) -> bool:
    """Creates a new record after validating inputs and ensuring ID uniqueness."""
    if not validate_non_empty_string(record_id):
        print("Error: El ID no puede estar vacío.")
        return False
    if not validate_non_empty_string(name):
        print(f"Error: El nombre no puede estar vacío (ID: {record_id}).")
        return False
    if not validate_positive_integer(age):
        print(f"Error: La edad debe ser un número entero positivo (ID: {record_id}).")
        return False
        
    if record_id in existing_ids:
        print(f"Error: Ya existe un registro con el ID {record_id}.")
        return False
        
    record = {"id": record_id, "name": name, "age": int(age)}
    records.append(record)
    existing_ids.add(record_id)
    save_data(records)
    print(f"Éxito: Registro {record_id} creado.")
    return True

def list_records() -> List[Dict[str, Any]]:
    """Returns all records, sorted by name using a lambda function."""
    return sorted(records, key=lambda x: x.get("name", "").lower())

def search_record(query: str) -> List[Dict[str, Any]]:
    """Searches for records matching the query in their name using a list comprehension."""
    query = query.lower()
    return [r for r in records if query in r.get("name", "").lower()]

def update_record(record_id: str, name: str = None, age: str = None) -> bool:
    """Updates an existing record. Validates new fields if provided."""
    if record_id not in existing_ids:
        print(f"Error: No se encontró un registro con el ID {record_id} para actualizar.")
        return False

    if name is not None and not validate_non_empty_string(name):
        print("Error: El nuevo nombre no puede estar vacío.")
        return False

    if age is not None and not validate_positive_integer(age):
        print("Error: La nueva edad debe ser un número entero positivo.")
        return False

    for record in records:
        if record["id"] == record_id:
            if name is not None:
                record["name"] = name
            if age is not None:
                record["age"] = int(age)
            save_data(records)
            print(f"Éxito: Registro {record_id} actualizado.")
            return True
            
    return False

def delete_record(record_id: str) -> bool:
    """Deletes a record by ID."""
    if record_id not in existing_ids:
        print(f"Error: No se encontró un registro con el ID {record_id} para eliminar.")
        return False
        
    global records
    records = [r for r in records if r["id"] != record_id]
    existing_ids.remove(record_id)
    save_data(records)
    print(f"Éxito: Registro {record_id} eliminado.")
    return True
