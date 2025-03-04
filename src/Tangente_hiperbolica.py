import numpy as np
import matplotlib.pyplot as plt

# Función tangente hiperbólica: mapea cualquier valor real a un rango entre -1 y 1

def tanh(x):
    return np.tanh(x)  # Utiliza la función tanh de NumPy para calcular los valores de la tangente hiperbólica

# Derivada de la función tangente hiperbólica: 1 - tanh(x)^2

def tanh_derivative(x):
    return 1 - np.tanh(x)**2

# Generación de datos para el eje x
x = np.linspace(-3, 3, 400)
y = tanh(x)# Evaluación de la función tangente hiperbólica 
dy = tanh_derivative(x)  # Evaluación de la derivada 

# Configuración y visualización de la gráfica
plt.figure(figsize=(8, 5))  
plt.plot(x, y, label='Tangente Hiperbólica')
plt.plot(x, dy, label='Derivada de la Tangente Hiperbólica', linestyle='dashed')
plt.axhline(0, color='black', linewidth=0.5)  # Línea horizontal en y = 0
plt.axvline(0, color='black', linewidth=0.5)  # Línea vertical en x = 0
plt.title("Función Tangente Hiperbólica y su Derivada")
plt.legend()
plt.grid()
plt.show()
