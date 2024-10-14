# Búsqueda lineal
def busqueda_lineal(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

# Búsqueda binaria (el arreglo debe estar ordenado)
def busqueda_binaria(arr, x):
    inicio, fin = 0, len(arr) - 1
    while inicio <= fin:
        mid = (inicio + fin) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            inicio = mid + 1
        else:
            fin = mid - 1
    return -1

# Ejemplo de uso
arr = [2, 3, 4, 10, 40]
x = 10
print("Búsqueda lineal:", busqueda_lineal(arr, x))
print("Búsqueda binaria:", busqueda_binaria(arr, x))
