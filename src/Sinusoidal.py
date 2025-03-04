import numpy as np
import matplotlib.pyplot as plt

# Función sinusoidal: modelo de onda basado en amplitud, frecuencia y desfase
def sinusoidal(x, A=1, omega=1, phi=0):
    return A * np.sin(omega * x + phi)

# Derivada de la función sinusoidal
def sinusoidal_derivative(x, A=1, omega=1, phi=0):
    return A * omega * np.cos(omega * x + phi)

# Generación de datos para el eje x
x = np.linspace(-2*np.pi, 2*np.pi, 400)
y = sinusoidal(x)  # Evaluación de la función sinusoidal
dy = sinusoidal_derivative(x)  # Evaluación de su derivada

# Configuración y visualización de la gráfica
plt.figure(figsize=(8, 5))
plt.plot(x, y, label='Sinusoidal')
plt.plot(x, dy, label='Derivada de la Sinusoidal', linestyle='dashed')
plt.axhline(0, color='black', linewidth=0.5)  # Línea horizontal en y = 0
plt.axvline(0, color='black', linewidth=0.5)  # Línea vertical en x = 0
plt.title("Función Sinusoidal y su Derivada")
plt.legend()
plt.grid()
plt.show()
