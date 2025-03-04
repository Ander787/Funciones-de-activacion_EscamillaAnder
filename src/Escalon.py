import numpy as np
import matplotlib.pyplot as plt

# Función escalón: devuelve 1 si x >= 0, de lo contrario 0
def step(x):
    return np.where(x >= 0, 1, 0)

# Derivada de la función escalón: siempre es 0

def step_derivative(x):
    return np.zeros_like(x)

# Generación de datos para el eje x
x = np.linspace(-10, 10, 400)
y = step(x)  # Evaluación de la función escalón
dy = step_derivative(x)  # Evaluación de su derivada

# Configuración y visualización de la gráfica
plt.figure(figsize=(8, 5))
plt.plot(x, y, label='Escalón')
plt.plot(x, dy, label='Derivada del Escalón', linestyle='dashed')
plt.axhline(0, color='black', linewidth=0.5)  # Línea horizontal en y = 0
plt.axvline(0, color='black', linewidth=0.5)  # Línea vertical en x = 0
plt.title("Función Escalón y su Derivada")
plt.legend()
plt.grid()
plt.show()
