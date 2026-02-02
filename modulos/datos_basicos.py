from .validaciones import validar_nombre, validar_precio, validar_stock

def solicitar_datos_producto():
    # Solicitar Nombre del Producto
    while True:
        nombre_input = input("Ingrese nombre del producto: ")
        nombre = validar_nombre(nombre_input)
        if nombre:
            break
        print("Nombre inválido. No puede estar vacío.")

    # Solicitar Precio
    while True:
        precio_input = input("Ingrese precio CLP (ej: 15000): ")
        precio = validar_precio(precio_input)
        if precio:
            break
        print("Precio inválido. Debe ser un número entero mayor a 0.")

    # Solicitar Stock
    while True:
        stock_input = input("Ingrese cantidad en stock: ")
        stock = validar_stock(stock_input)
        if stock is not None:
            break
        print("Stock inválido. Debe ser un número entero positivo.")

    return nombre, precio, stock