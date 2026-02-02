# Tupla de categorías (Dato inmutable)
CATEGORIAS = ('Electrónica', 'Hogar', 'Ropa', 'Alimentos')

# Inicializamos la lista con productos variados para probar todas las funciones
productos = [
    {"nombre": "Notebook HP", "categoria": "Electrónica", "precio": 450000, "stock": 10},
    {"nombre": "Mouse Logitech", "categoria": "Electrónica", "precio": 15000, "stock": 25},
    {"nombre": "Polera Básica", "categoria": "Ropa", "precio": 5000, "stock": 50},
    {"nombre": "Jeans Levis", "categoria": "Ropa", "precio": 35000, "stock": 15},
    {"nombre": "Arroz 1kg", "categoria": "Alimentos", "precio": 1200, "stock": 100},
    {"nombre": "Aceite Maravilla", "categoria": "Alimentos", "precio": 2500, "stock": 40},
    {"nombre": "Lámpara Escritorio", "categoria": "Hogar", "precio": 12000, "stock": 8},
    {"nombre": "Juego de Sábanas", "categoria": "Hogar", "precio": 22000, "stock": 5}
]


nombres_productos = {prod['nombre'].lower() for prod in productos}

def registrar_producto(nombre, categoria, precio, stock):
    # Validación de duplicados
    if nombre.lower() in nombres_productos:
        print(f"Error: El producto '{nombre}' ya existe.")
        return False

    nuevo_producto = {
        "nombre": nombre,
        "categoria": categoria,
        "precio": precio,
        "stock": stock
    }
    
    productos.append(nuevo_producto)
    nombres_productos.add(nombre.lower())
    print(f"Producto '{nombre}' registrado exitosamente.")
    return True

def listar_productos():
    if not productos:
        print("No hay productos en el inventario.")
        return

    print("\n--- Inventario de Productos ---")
    print(f"{'Nombre':<20} | {'Categoría':<15} | {'Precio':<10} | {'Stock':<5}")
    print("-" * 60)
    for prod in productos:
        print(f"{prod['nombre']:<20} | {prod['categoria']:<15} | ${prod['precio']:<9} | {prod['stock']:<5}")

def buscar_producto(nombre_buscar):
    encontrado = False
    print(f"\n--- Resultados para '{nombre_buscar}' ---")
    
    for prod in productos:
        if nombre_buscar.lower() in prod['nombre'].lower():
            print(f"ENCONTRADO: {prod['nombre']} | Cat: {prod['categoria']} | ${prod['precio']} | Stock: {prod['stock']}")
            encontrado = True
    
    if not encontrado:
        print("No se encontraron productos con ese nombre.")