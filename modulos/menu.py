from .gestion_datos import registrar_producto, listar_productos, buscar_producto, CATEGORIAS, productos
from .datos_basicos import solicitar_datos_producto
from .funciones_utiles import mostrar_categorias_disponibles, contar_productos_por_categoria

def iniciar_menu():
    while True:
        print("\n--- SISTEMA DE GESTIÓN DE PRODUCTOS ---")
        print("1. Registrar Producto")
        print("2. Ver Inventario")
        print("3. Buscar Producto")
        print("4. Reporte de Categorías")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            nombre, precio, stock = solicitar_datos_producto()
            
            categoria_final = None
            
            while True:
                mostrar_categorias_disponibles(CATEGORIAS)
                cat_input = input("Escriba la categoría: ").strip()
                
                # Buscamos si lo que escribió coincide con alguna categoría
                for cat in CATEGORIAS:
                    if cat.lower() == cat_input.lower():
                        categoria_final = cat
                        break
                
                if categoria_final:
                    # Si encontramos una coincidencia, salimos del bucle
                    break
                else:
                    print("ERROR: Categoría no válida. Intente nuevamente.")
            
            # Registramos con la categoría ya validada y formateada correctamente
            registrar_producto(nombre, categoria_final, precio, stock)

        elif opcion == '2':
            listar_productos()

        elif opcion == '3':
            nombre_b = input("Ingrese parte del nombre a buscar: ")
            buscar_producto(nombre_b)

        elif opcion == '4':
            print("\n--- Conteo por Categoría ---")
            mostrar_categorias_disponibles(CATEGORIAS)
            cat_buscar = input("Ingrese categoría a contar: ")
            
            total = contar_productos_por_categoria(productos, cat_buscar)
            print(f"Total de productos en '{cat_buscar}': {total}")

        elif opcion == '5':
            print("Cerrando sistema...")
            break
        
        else:
            print("Opción inválida.")