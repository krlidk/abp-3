def contar_productos_por_categoria(lista_productos, categoria_buscar):
    if not lista_productos:
        return 0

    producto_actual = lista_productos[0]
    resto_lista = lista_productos[1:]

    # Verificar coincidencia
    coincide = 1 if producto_actual['categoria'] == categoria_buscar else 0

    return coincide + contar_productos_por_categoria(resto_lista, categoria_buscar)

def mostrar_categorias_disponibles(categorias_tupla):
    print("Categorías:", end=" ")
    for cat in categorias_tupla:
        print(f"[{cat}]", end=" ")
    print()