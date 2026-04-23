import sys
import os

# Add the parent directory to the sys.path to allow imports from src
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.service import create_record, get_all_records

def main():
    print("Sistema listo")
    
    # Módulo 1: Creación de registros en memoria y listado
    print("\n--- Creando registros de prueba ---")
    
    create_record("001", "Alice", "30")
    create_record("002", "Bob", "25")
    
    # Intentando duplicar un ID (validación de sets)
    create_record("001", "Charlie", "40")
    
    # Intentando datos inválidos (validaciones)
    create_record("003", "", "22")
    create_record("004", "David", "-5")
    
    print("\n--- Listando registros actuales ---")
    registros = get_all_records()
    for idx, r in enumerate(registros):
        print(f"Registro {idx+1}: {r}")

if __name__ == "__main__":
    main()
