# Tipos de datos primitivos
entero = 10                 # Integer
decimal = 10.5              # Float
cadena = "Hola, mundo"      # String
booleano = True             # Boolean

# Tipos de datos como objetos
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

persona = Persona("Juan", 25)

# Imprimir los tipos de datos
print("Entero:", entero)
print("Decimal:", decimal)
print("Cadena:", cadena)
print("Booleano:", booleano)
print("Objeto Persona:", persona.nombre, persona.edad)
