import numpy as np
import matplotlib.pyplot as plt

# Función sigmoide: transforma valores reales en el rango (0,1)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Derivada de la función sigmoide

def sigmoid_derivative(x):
    return sigmoid(x) * (1 - sigmoid(x))

# Generación de datos para el eje x
x = np.linspace(-10, 10, 400)
y = sigmoid(x)  # Evaluación de la función sigmoide
dy = sigmoid_derivative(x)  # Evaluación de su derivada

# Configuración y visualización de la gráfica
plt.figure(figsize=(8, 5))
plt.plot(x, y, label='Sigmoide')
plt.plot(x, dy, label='Derivada de la Sigmoide', linestyle='dashed')
plt.axhline(0, color='black', linewidth=0.5)  # Línea horizontal en y = 0
plt.axvline(0, color='black', linewidth=0.5)  # Línea vertical en x = 0
plt.title("Función Sigmoide y su Derivada")
plt.legend()
plt.grid()
plt.show()
