def promedio_arreglo(arr):
    return sum(arr) / len(arr) if arr else 0

# Ejemplo de uso 1
arreglo1 = [10, 20, 30]
promedio1 = promedio_arreglo(arreglo1)
print("El promedio de los valores en arreglo1 es:", promedio1)
