import numpy as np
import matplotlib.pyplot as plt

# Función identidad: devuelve el mismo valor de entrada

def identity(x):
    return x

# Derivada de la función identidad: siempre es 1

def identity_derivative(x):
    return np.ones_like(x)

# Generación de datos para el eje x
x = np.linspace(-10, 10, 400)
y = identity(x)  # Evaluación de la función identidad
dy = identity_derivative(x)  # Evaluación de su derivada

# Configuración y visualización de la gráfica
plt.figure(figsize=(8, 5))
plt.plot(x, y, label='Identidad')
plt.plot(x, dy, label='Derivada de la Identidad', linestyle='dashed')
plt.axhline(0, color='black', linewidth=0.5)  # Línea horizontal en y = 0
plt.axvline(0, color='black', linewidth=0.5)  # Línea vertical en x = 0
plt.title("Función Identidad y su Derivada")
plt.legend()
plt.grid()
plt.show()
