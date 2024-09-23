import re

# Función para verificar si el código del producto es válido
def es_codigo_valido(codigo):
    # El código debe tener entre 5 y 10 caracteres, contener letras y números, y no contener caracteres especiales
    if re.match("^[A-Za-z0-9]{5,10}$", codigo):
        return True
    else:
        return False

# Función para agregar un producto al inventario si el código es válido
def agregar_producto(inventario, codigo_producto, nombre_producto):
    if es_codigo_valido(codigo_producto):
        inventario[codigo_producto] = nombre_producto
        print(f"Producto '{nombre_producto}' agregado al inventario con el código '{codigo_producto}'.")
    else:
        print(f"Error: El código '{codigo_producto}' no es válido. Debe contener solo letras y números, y tener entre 5 y 10 caracteres.")

# Función para mostrar el inventario
def mostrar_inventario(inventario):
    print("\nInventario actual:")
    for codigo, nombre in inventario.items():
        print(f"Código: {codigo} - Producto: {nombre}")

# Inventario inicial (diccionario alfanumérico)
inventario = {}

# Agregar algunos productos al inventario
agregar_producto(inventario, "ABC123", "Laptop")
agregar_producto(inventario, "4GHT56", "Teléfono móvil")
agregar_producto(inventario, "XYZ78900", "Monitor")
agregar_producto(inventario, "P@SSWORD", "Teclado")  # Código inválido (contiene un carácter especial)
agregar_producto(inventario, "12345", "Mouse")

# Mostrar el inventario después de las adiciones
mostrar_inventario(inventario)
