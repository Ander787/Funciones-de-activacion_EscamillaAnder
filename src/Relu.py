import numpy as np
import matplotlib.pyplot as plt

# Función ReLU: devuelve el máximo entre 0 y x

def relu(x):
    return np.maximum(0, x)

# Derivada de la función ReLU

def relu_derivative(x):
    return np.where(x > 0, 1, 0)

# Generación de datos para el eje x
x = np.linspace(-3, 3, 400)
y = relu(x)  # Evaluación de la función ReLU
dy = relu_derivative(x)  # Evaluación de su derivada

# Configuración y visualización de la gráfica
plt.figure(figsize=(8, 5))
plt.plot(x, y, label='ReLU')
plt.plot(x, dy, label='Derivada de ReLU', linestyle='dashed')
plt.axhline(0, color='black', linewidth=0.5)  # Línea horizontal en y = 0
plt.axvline(0, color='black', linewidth=0.5)  # Línea vertical en x = 0
plt.title("Función ReLU y su Derivada")
plt.legend()
plt.grid()
plt.show()
