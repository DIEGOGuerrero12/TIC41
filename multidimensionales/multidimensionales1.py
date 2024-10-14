# Crear un arreglo bidimensional de 3x3
arreglo = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Acceder a un elemento
print("Elemento en la posición [1][2]:", arreglo[1][2])

# Recorrer el arreglo bidimensional
for fila in arreglo:
    for elemento in fila:
        print(elemento, end=" ")
    print()  # Para crear una nueva línea después de cada fila
