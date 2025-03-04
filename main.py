import numpy as np 
import matplotlib.pyplot as plt  

# Importación de funciones de activación y transformaciones
from src.Sigmoide import sigmoid
from src.Escalon import step
from src.Gaussiana import gaussian
from src.Identidad import identity
from src.Lineal_a_tramos import piecewise
from src.Relu import relu
from src.Sinusoidal import sinusoidal
from src.Tangente_hiperbolica import tanh

def plot_functions():
    x = np.linspace(-10, 10, 400)  # Genera los puntos para el eje x
    
    # Evaluamos cada función para los valores de x
    y = {
        'Sigmoidal': sigmoid(x),
        'Escalón': step(x),
        'Gaussiana': gaussian(x),
        'Identidad': identity(x),
        'Lineal a tramos': piecewise(x),
        'ReLU': relu(x),
        'Sinusoidal': sinusoidal(x),
        'Tangente Hiperbólica': tanh(x)
    }
    
    fig, axs = plt.subplots(4, 2, figsize=(12, 12))  # Configuramos la figura con subgráficas
    axs = axs.flatten()  # Convertimos la matriz de ejes a una lista para facilitar el acceso
    
    # Graficamos cada función y asignamos el título correspondiente
    for i, (func_name, values) in enumerate(y.items()):
        axs[i].plot(x, values)
        axs[i].set_title(func_name)
    
    plt.tight_layout()  # Ajusta el diseño para evitar superposiciones
    plt.show()  # Muestra todos los gráficos

# Ejecuta la función principal si el script es llamado directamente
if __name__ == "__main__":
    plot_functions()
