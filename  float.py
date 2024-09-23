# Función para calcular el balance final con interés compuesto
def calcular_balance_inicial(balance_inicial, tasa_interes_anual, anos):
    return balance_inicial * (1 + tasa_interes_anual / 100) ** anos  # Fórmula de interés compuesto

# Función para simular depósitos y retiros
def transacciones_bancarias(balance_inicial, deposito, retiro):
    balance_actual = balance_inicial + deposito - retiro  # Suma depósitos y resta retiros
    if balance_actual < 0:
        print("Alerta: El balance es negativo. Ha retirado más de lo que tiene en la cuenta.")
    return balance_actual

# Datos iniciales (floats)
balance_inicial = 1000.75  # Balance inicial de la cuenta en punto flotante
tasa_interes_anual = 3.5  # Tasa de interés anual en porcentaje (float)
anos = 5  # Número de años para aplicar el interés compuesto (entero)
deposito = 500.25  # Monto del depósito (float)
retiro = 200.50  # Monto del retiro (float)

# Calcular el balance inicial después de aplicar interés compuesto
balance_despues_interes = calcular_balance_inicial(balance_inicial, tasa_interes_anual, anos)
print(f"Balance después de {anos} años con una tasa de interés del {tasa_interes_anual}%: ${balance_despues_interes:.2f}")

# Calcular el balance después de las transacciones (depósito y retiro)
balance_final = transacciones_bancarias(balance_despues_interes, deposito, retiro)
print(f"Balance final después de un depósito de ${deposito} y un retiro de ${retiro}: ${balance_final:.2f}")
