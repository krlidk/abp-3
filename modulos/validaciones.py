def validar_nombre(nombre):
    if nombre and nombre.strip():
        return nombre.strip()
    return None

def validar_precio(valor):
    try:
        # CAMBIO: Usamos int() en vez de float()
        precio = int(valor)
        if precio > 0:
            return precio
        return None
    except ValueError:
        return None

def validar_stock(valor):
    #Valida que el stock sea un entero no negativo.
    try:
        stock = int(valor)
        if stock >= 0:
            return stock
        return None
    except ValueError:
        return None

def validar_categoria(categoria, categorias_permitidas):
    if categoria in categorias_permitidas:
        return categoria
    return None