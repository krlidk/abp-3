# Sistema de Gestión de Productos - Proyecto Módulo 3

## Descripción General
Este proyecto consiste en el desarrollo de una aplicación de consola en Python para gestionar el inventario de una empresa de tecnología. El sistema permite registrar productos, listar el stock actual, buscar items específicos mediante coincidencias parciales y generar reportes utilizando algoritmos recursivos.


---

## Estructura del Proyecto
El código ha sido modularizado siguiendo las buenas prácticas (PEP 8) para facilitar su mantenimiento y escalabilidad.

```text
sistema_gestion_productos/
│
├── main.py                     # Punto de entrada principal de la aplicación
├── README.md                   # Documentación técnica del proyecto
└── modulos/                    # Paquete que contiene la lógica del negocio
    ├── __init__.py             # Inicializador del paquete
    ├── datos_basicos.py        # Funciones para la captura y limpieza de inputs
    ├── funciones_utiles.py     # Lógica auxiliar y algoritmos recursivos
    ├── gestion_datos.py        # Base de datos en memoria (CRUD) y datos de prueba
    ├── menu.py                 # Controlador del flujo del programa (Menú principal)
    └── validaciones.py         # Reglas de negocio (validación de tipos y formatos)
```

## 🛠️ Justificación Técnica
A continuación se detalla el uso de las estructuras de control y datos aplicadas en el código, cumpliendo con los requerimientos del módulo:

### 1. Estructuras de Control
* **Bucle `while True` (Menú):** Se implementa en `menu.py` para mantener la aplicación en ejecución continua, permitiendo al usuario realizar múltiples operaciones sin reiniciar el programa hasta que decida explícitamente "Salir".
* **Bucle `while` (Validaciones):** En `datos_basicos.py`, cada solicitud de dato (`input`) está envuelta en un bucle `while`. Esto "atrapa" al usuario si ingresa un dato incorrecto (ej: texto en el precio) y le vuelve a preguntar hasta que ingrese un valor válido.
* **Condicionales `if`, `elif`, `else`:** Utilizados para el enrutamiento de opciones en el menú y para reglas de negocio críticas (ej: impedir el registro si la categoría ingresada no existe en la tupla de permitidas).

### 2. Estructuras de Datos
* **Listas (`list`):** Estructura principal (`productos`) para almacenar el inventario. Se eligió por ser ordenada, mutable y permitir el almacenamiento de diccionarios.
* **Diccionarios (`dict`):** Representan la entidad "Producto". Permiten acceder a los atributos (`nombre`, `categoria`, `precio`, `stock`) mediante claves descriptivas en lugar de índices numéricos.
* **Conjuntos (`set`):** Se utiliza la variable `nombres_productos` para almacenar los nombres en minúsculas.
    * *Por qué:* Los sets tienen una búsqueda de tiempo constante O(1), lo que hace mucho más eficiente verificar si un producto ya existe antes de registrarlo, evitando duplicados.
* **Tuplas (`tuple`):** Utilizada para definir `CATEGORIAS` ('Electrónica', 'Hogar', 'Ropa', 'Alimentos').
    * *Por qué:* Al ser inmutables, garantizan que las categorías base del negocio no puedan ser modificadas o borradas accidentalmente durante la ejecución del programa.

### 3. Algoritmos Específicos
* **Recursividad:** Implementada en la función `contar_productos_por_categoria` (archivo `funciones_utiles.py`).
    * *Lógica:* La función procesa el primer elemento de la lista ("cabeza") y se llama a sí misma pasando el resto de la lista ("cola"). Esto demuestra el manejo de recursión sobre estructuras de datos sin usar bucles iterativos tradicionales (`for`/`while`).
* **Búsqueda Parcial:** La función de búsqueda utiliza el operador de pertenencia `in`. Esto mejora la experiencia de usuario (UX), permitiendo encontrar "Notebook HP" escribiendo simplemente "hp" o "note".

## 🚀 Cómo ejecutar el programa

### Prerrequisitos
* Tener instalado **Python 3.x**.
* Terminal o consola de comandos disponible.

### Instrucciones paso a paso
1. Abre tu terminal.
2. Navega hasta la carpeta raíz del proyecto:
    ```bash
    cd ruta/a/tu/sistema_gestion_productos
    ```
3. Ejecuta el archivo principal:
    ```bash
    python main.py
    ```

## 🧪 Datos de Prueba (Mock Data)
Para facilitar la corrección y pruebas rápidas, el sistema inicia con 8 productos precargados en memoria.

### Productos incluidos:
* **Electrónica:** Notebook HP, Mouse Logitech
* **Ropa:** Polera Básica, Jeans Levis
* **Alimentos:** Arroz 1kg, Aceite Maravilla
* **Hogar:** Lámpara Escritorio, Juego de Sábanas

> **Nota:** No es necesario ingresar datos manualmente para probar las funciones "Listar", "Buscar" o "Reporte Recursivo". Simplemente inicie el programa y seleccione la **Opción 2** para ver los datos cargados.