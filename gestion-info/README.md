# 📁 Sistema de Gestión de Información

¡Hola! Bienvenido/a a este pequeño sistema de gestión. 
Este programa es una herramienta sencilla que permite administrar información (como si fuera una agenda o un directorio) directamente desde tu computadora.

---

## 🤔 ¿Qué necesitas antes de empezar?

Dado que este programa está escrito en un lenguaje llamado **Python**, tu computadora necesita tener instalado este lenguaje para poder "entenderlo".

**Si no tienes Python instalado:**
1. Ve a la página oficial: [Descargar Python](https://www.python.org/downloads/)
2. Descarga la versión más reciente para Windows.
3. Al abrir el instalador, **es vital que marques una casilla en la parte de abajo** que dice **"Add Python to PATH"** o "Agregar Python al PATH".
4. Haz clic en "Instalar" y espera a que termine.

---

## 🚀 ¿Cómo iniciar el programa paso a paso?

Una vez que tengas Python en tu computadora, sigue estos pasos:

### Paso 1: Abrir la terminal
Necesitas abrir la "consola" o "terminal" de tu computadora. 
- Puedes abrir el menú de inicio de Windows, buscar **"cmd"** o **"Símbolo del sistema"** y abrirlo.
- *(Si usas un programa especial para ver el código como VS Code, simplemente usa su terminal integrada).*

### Paso 2: Ubicarte en la carpeta del proyecto
En la terminal, debes asegurarte de estar ubicado justo en esta misma carpeta (la carpeta llamada `gestion-info`). 

### Paso 3: Instalar los complementos necesarios
Nuestro programa usa algunas herramientas extra para funcionar. Para descargarlas automáticamente, escribe el siguiente texto en tu terminal y presiona la tecla **Enter**:

```bash
pip install -r requirements.txt
```
*(Solo necesitas hacer esto la primera vez).*

### Paso 4: ¡Encender el sistema!
Por último, para ejecutar el programa, escribe esto y presiona **Enter**:

```bash
python src/main.py
```
*(Nota: Si al hacer esto se abre la tienda de Windows sola, revisa los pasos de instalación de Python y asegúrate de haber marcado la casilla de "Add Python to PATH").*

---

## ✨ ¿Qué hace el programa actualmente?

Por ahora, al correr el programa, la pantalla te mostrará una prueba automática donde el sistema:
1. **Crea personas de prueba:** Intenta guardar nombres y edades (por ejemplo, a Alice de 30 años).
2. **Evita errores:** El sistema es inteligente y bloqueará la creación si alguien tiene el mismo "ID" repetido o si le ponen una edad inválida (como números negativos).
3. **Muestra una lista:** Al terminar, imprimirá en la pantalla la lista de todos los registros que se guardaron con éxito.

¡En futuras actualizaciones este sistema tendrá menús interactivos donde tú mismo podrás escribir, guardar y borrar la información!

---

## 🗂️ Historial de Módulos

### MÓDULO 1 — Estructura de datos y validaciones base

**Objetivo:** Definir la estructura del registro y almacenar datos en memoria.

**Requisitos que se cumplen aquí:**
- Listas y diccionarios
- Sets (para IDs únicos o correos únicos)
- Validaciones de campos

**Entregables:**
- `validate.py` con funciones de validación
- `service.py` con estructura inicial (sin archivos aún)
- `main.py` crear datos y listar datos

**Criterios de aceptación:**
- Se pueden crear registros en memoria y listar.
- No permite IDs duplicados (uso de set).

*(Etiquetado en el repositorio como `m1-data`)*

---

### MÓDULO 2 — Persistencia en archivos (JSON recomendado)

**Objetivo:** Guardar y cargar los registros desde un archivo.

**Requisitos que se cumplen aquí:**
- Manejo seguro de archivos
- try-except para errores de lectura/escritura
- Persistencia real (los datos quedan guardados)

**Entregables:**
- `file.py` con funciones:
    - `load_data()`
    - `save_data(data)`
- Archivo dentro de `data/` (por ejemplo `records.json`)
- Modificar `main.py` crear datos y listar datos en el archivo `.json`

**Criterios de aceptación:**
- Si el archivo no existe, el programa crea/arranca con lista vacía.
- Si el archivo está dañado, muestra mensaje y no se cae.

*(Etiquetado en el repositorio como `m2-files`)*

