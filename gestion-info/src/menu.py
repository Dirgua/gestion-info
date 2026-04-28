from colorama import init, Fore, Style
from src.service import new_register, list_records, search_record, update_record, delete_record

# Inicializar colorama (necesario en Windows)
init(autoreset=True)

# --- Helpers de presentación ---

def _titulo(texto: str):
    print(f"\n{Fore.CYAN}{Style.BRIGHT}{'═' * 40}")
    print(f"  {texto}")
    print(f"{'═' * 40}{Style.RESET_ALL}")

def _exito(texto: str):
    print(f"{Fore.GREEN}✔ {texto}{Style.RESET_ALL}")

def _error(texto: str):
    print(f"{Fore.RED}✘ {texto}{Style.RESET_ALL}")

def _info(texto: str):
    print(f"{Fore.YELLOW}→ {texto}{Style.RESET_ALL}")

def _pedir(prompt: str) -> str:
    return input(f"{Fore.WHITE}{prompt}{Style.RESET_ALL}").strip()

# --- Opciones del menú ---

def _opcion_crear():
    _titulo("NUEVO REGISTRO")
    record_id = _pedir("ID      : ")
    name      = _pedir("Nombre  : ")
    age       = _pedir("Edad    : ")
    new_register(record_id, name, age)

def _opcion_listar():
    _titulo("LISTADO DE REGISTROS")
    registros = list_records()
    if not registros:
        _info("No hay registros guardados aún.")
        return
    for r in registros:
        print(f"  {Fore.CYAN}[{r['id']}]{Style.RESET_ALL} {r['name']} — {r['age']} años")

def _opcion_buscar():
    _titulo("BUSCAR REGISTRO")
    query = _pedir("Nombre a buscar: ")
    resultados = search_record(query)
    if not resultados:
        _info(f"No se encontraron registros con '{query}'.")
        return
    for r in resultados:
        print(f"  {Fore.CYAN}[{r['id']}]{Style.RESET_ALL} {r['name']} — {r['age']} años")

def _opcion_actualizar():
    _titulo("EDITAR REGISTRO")
    record_id = _pedir("ID del registro a editar: ")
    print(f"{Fore.YELLOW}  (Deja en blanco para no cambiar ese campo){Style.RESET_ALL}")
    name = _pedir("Nuevo nombre : ") or None
    age  = _pedir("Nueva edad   : ") or None
    update_record(record_id, name=name, age=age)

def _opcion_eliminar():
    _titulo("ELIMINAR REGISTRO")
    record_id = _pedir("ID del registro a eliminar: ")
    confirmacion = _pedir(f"¿Seguro que quieres eliminar '{record_id}'? (s/n): ").lower()
    if confirmacion == "s":
        delete_record(record_id)
    else:
        _info("Eliminación cancelada.")

# --- Menú principal ---

def mostrar_menu():
    print(f"\n{Fore.CYAN}{Style.BRIGHT}╔══════════════════════════════════════╗")
    print(f"║   SISTEMA DE GESTIÓN DE INFORMACIÓN   ║")
    print(f"╚══════════════════════════════════════╝{Style.RESET_ALL}")
    print(f"  {Fore.WHITE}1.{Style.RESET_ALL} Crear registro")
    print(f"  {Fore.WHITE}2.{Style.RESET_ALL} Listar registros")
    print(f"  {Fore.WHITE}3.{Style.RESET_ALL} Buscar registro")
    print(f"  {Fore.WHITE}4.{Style.RESET_ALL} Editar registro")
    print(f"  {Fore.WHITE}5.{Style.RESET_ALL} Eliminar registro")
    print(f"  {Fore.RED}0.{Style.RESET_ALL} Salir")

def run():
    """Bucle principal del menú. Se repite hasta que el usuario elige salir."""
    opciones = {
        "1": _opcion_crear,
        "2": _opcion_listar,
        "3": _opcion_buscar,
        "4": _opcion_actualizar,
        "5": _opcion_eliminar,
    }

    while True:
        mostrar_menu()
        try:
            eleccion = _pedir("\n  Elige una opción: ")
        except (KeyboardInterrupt, EOFError):
            break

        if eleccion == "0":
            print(f"\n{Fore.CYAN}¡Hasta luego!{Style.RESET_ALL}\n")
            break
        elif eleccion in opciones:
            opciones[eleccion]()
        else:
            _error("Opción no válida. Ingresa un número del 0 al 5.")
