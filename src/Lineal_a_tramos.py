import numpy as np
import matplotlib.pyplot as plt

# Función lineal a tramos

def piecewise(x):
    return np.piecewise(x, [x < -1, (-1 <= x) & (x <= 1), x > 1], [-1, lambda x: x, 1])

# Derivada de la función lineal a tramos

def piecewise_derivative(x):
    return np.piecewise(x, [x < -1, (-1 <= x) & (x <= 1), x > 1], [0, 1, 0])

# Generación de datos para el eje x
x = np.linspace(-3, 3, 400)
y = piecewise(x)  # Evaluación de la función
dy = piecewise_derivative(x)  # Evaluación de su derivada

# Configuración y visualización de la gráfica
plt.figure(figsize=(8, 5))
plt.plot(x, y, label='Lineal a Tramos')
plt.plot(x, dy, label='Derivada de la Lineal a Tramos', linestyle='dashed')
plt.axhline(0, color='black', linewidth=0.5)  # Línea horizontal en y = 0
plt.axvline(0, color='black', linewidth=0.5)  # Línea vertical en x = 0
plt.title("Función Lineal a Tramos y su Derivada")
plt.legend()
plt.grid()
plt.show()
