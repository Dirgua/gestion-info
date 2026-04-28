import sys
import os

# Add the parent directory to the sys.path to allow imports from src
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.service import new_register, list_records, search_record, update_record, delete_record

def main():
    print("Sistema listo - Módulo 3 (CRUD Completo)")
    
    print("\n--- 1. Creando registros de prueba ---")
    new_register("001", "Alice", "30")
    new_register("002", "Bob", "25")
    new_register("003", "Charlie", "40")
    
    print("\n--- 2. Listando registros actuales (Ordenados por nombre) ---")
    registros = list_records()
    for idx, r in enumerate(registros):
        print(f"Registro {idx+1}: {r}")

    print("\n--- 3. Actualizando registro 002 ---")
    update_record("002", name="Robert", age="26")
    
    # Intento de actualización con errores
    update_record("999", name="Ghost") # ID no existe
    update_record("001", age="-5") # Edad inválida
    
    print("\n--- 4. Búsqueda de registros ---")
    print("Buscando 'ro':")
    resultados = search_record("ro")
    for r in resultados:
        print(f"Encontrado: {r}")

    print("\n--- 5. Eliminando registro 003 ---")
    delete_record("003")
    
    # Intento de eliminar ID inexistente
    delete_record("999")
    
    print("\n--- Listado final ---")
    for r in list_records():
        print(r)

if __name__ == "__main__":
    main()
