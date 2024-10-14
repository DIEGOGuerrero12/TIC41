# Ordenamiento burbuja
def ordenamiento_burbuja(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Ordenamiento por selección
def ordenamiento_seleccion(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Ejemplo de uso
arr = [64, 25, 12, 22, 11]
print("Ordenamiento burbuja:", ordenamiento_burbuja(arr.copy()))
print("Ordenamiento por selección:", ordenamiento_seleccion(arr.copy()))
