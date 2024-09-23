# Clase para representar a un personaje
class Personaje:
    def __init__(self, nombre, nivel, experiencia, puntos_vida, ataque):
        self.nombre = nombre  # String para el nombre del personaje
        self.nivel = nivel  # Nivel del personaje (int)
        self.experiencia = experiencia  # Experiencia acumulada (int)
        self.puntos_vida = puntos_vida  # Puntos de vida (int)
        self.ataque = ataque  # Puntos de ataque (int)
    
    # Método para subir de nivel si la experiencia es suficiente
    def subir_nivel(self):
        experiencia_necesaria = self.nivel * 100  # Cada nivel requiere 100 puntos por nivel
        if self.experiencia >= experiencia_necesaria:
            self.nivel += 1  # Sube un nivel
            self.experiencia -= experiencia_necesaria  # Resta la experiencia necesaria
            self.puntos_vida += 10  # Aumenta puntos de vida con cada nivel
            self.ataque += 2  # Aumenta puntos de ataque con cada nivel
            print(f"¡{self.nombre} ha subido al nivel {self.nivel}!")
        else:
            print(f"{self.nombre} necesita más experiencia para subir de nivel.")

    # Método para simular un ataque a otro personaje
    def atacar(self, enemigo):
        print(f"{self.nombre} ataca a {enemigo.nombre} y causa {self.ataque} puntos de daño.")
        enemigo.puntos_vida -= self.ataque  # Reduce los puntos de vida del enemigo
        if enemigo.puntos_vida <= 0:
            enemigo.puntos_vida = 0
            print(f"{enemigo.nombre} ha sido derrotado.")
        else:
            print(f"A {enemigo.nombre} le quedan {enemigo.puntos_vida} puntos de vida.")

# Crear dos personajes
heroe = Personaje(nombre="Aragorn", nivel=1, experiencia=50, puntos_vida=100, ataque=15)
enemigo = Personaje(nombre="Orco", nivel=1, experiencia=20, puntos_vida=80, ataque=10)

# Mostrar información inicial
print(f"Personaje: {heroe.nombre}, Nivel: {heroe.nivel}, Experiencia: {heroe.experiencia}, Vida: {heroe.puntos_vida}, Ataque: {heroe.ataque}")
print(f"Enemigo: {enemigo.nombre}, Nivel: {enemigo.nivel}, Experiencia: {enemigo.experiencia}, Vida: {enemigo.puntos_vida}, Ataque: {enemigo.ataque}")

# Simulación de combate
heroe.atacar(enemigo)
enemigo.atacar(heroe)

# Ganar experiencia y subir de nivel
heroe.experiencia += 60  # Ganar experiencia
heroe.subir_nivel()  # Intentar subir de nivel

# Mostrar estado final
print(f"Estado final de {heroe.nombre}: Nivel {heroe.nivel}, Vida {heroe.puntos_vida}, Ataque {heroe.ataque}, Experiencia {heroe.experiencia}")
