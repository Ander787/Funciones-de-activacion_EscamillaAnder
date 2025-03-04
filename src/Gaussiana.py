import numpy as np
import matplotlib.pyplot as plt

# Función gaussiana: A controla la amplitud

def gaussian(x, A=1):
    return A * np.exp(-x**2)

# Derivada de la función gaussiana

def gaussian_derivative(x, A=1):
    return -2 * x * gaussian(x, A)

# Generación de datos para el eje x
x = np.linspace(-3, 3, 400)
y = gaussian(x)  # Evaluación de la función gaussiana
dy = gaussian_derivative(x)  # Evaluación de su derivada

# Configuración y visualización de la gráfica
plt.figure(figsize=(8, 5))
plt.plot(x, y, label='Gaussiana')
plt.plot(x, dy, label='Derivada de la Gaussiana', linestyle='dashed')
plt.axhline(0, color='black', linewidth=0.5)  # Línea horizontal en y = 0
plt.axvline(0, color='black', linewidth=0.5)  # Línea vertical en x = 0
plt.title("Función Gaussiana y su Derivada")
plt.legend()
plt.grid()
plt.show()
