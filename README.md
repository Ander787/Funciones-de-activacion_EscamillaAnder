# README - Funciones de Activación en Redes Neuronales

## 🤓 Información del Proyecto  
**Materia:** Sistemas de Visión Artificial  
**Tarea:** Tarea 2.1 - Gráficas de funciones de activación con su derivada  
**Estudiante:** Ander Heinrich Escamilla Wong
**Fecha:** 03/03/2025  

---

## ✏️ Descripción General  
Este repositorio contiene un conjunto de scripts en Python que grafican diversas funciones de activación junto con sus derivadas. Cada función está implementada en su propio módulo dentro de la carpeta `src/`.  

El archivo `main.py` es el punto de entrada para ejecutar todas las gráficas de manera conjunta.  

---

## 🧠 Funciones de Activación en Redes Neuronales  
Este proyecto implementa las siguientes funciones de activación:  

- **Sigmoide**  
- **ReLU (Rectified Linear Unit)**  
- **Leaky ReLU**  
- **TanH (Tangente Hiperbólica)**  
- **ELU (Exponential Linear Unit)**  
- **Softmax**  

Cada función tiene su respectiva derivada y se representa visualmente en los gráficos generados por el código.  

---

# Proyecto de Funciones Matemáticas

Este repositorio contiene la implementación de diversas funciones matemáticas utilizadas en modelos de aprendizaje automático y redes neuronales.

## ☝️ Requisitos Previos
Antes de ejecutar el código, asegúrate de tener instaladas las siguientes bibliotecas en tu entorno de Python:

```sh
pip install numpy matplotlib
```

## 📋 Estructura del Repositorio

```
proyecto_funciones/
│── src/                        # Código fuente
│   ├── Escalon.py              # Función Escalón
│   ├── Gaussiana.py            # Función Gaussiana
│   ├── Identidad.py            # Función Identidad
│   ├── Lineal_a_tramos.py      # Función Lineal a Tramos
│   ├── Relu.py                 # Función ReLU
│   ├── Sigmoidal.py            # Función Sigmoide
│   ├── Sinusoidal.py           # Función Sinusoidal
│   ├── Tangente_hiperbolica.py # Función Tangente Hiperbólica
│── main.py                     # Punto de entrada para ejecutar todas las funciones
│── README.md                   # Este documento
```

### 1. `main.py`
Este archivo es el punto de entrada del proyecto. Su función principal es importar y ejecutar todas las funciones implementadas en `src/`. Para ello, realiza las siguientes importaciones:

```python
from src.Gaussiana import plot_gaussian
from src.Escalon import plot_step_function
from src.Identidad import plot_identidad
from src.Lineal_a_tramos import plot_piecewise_func
from src.Relu import plot_relu
from src.Sigmoidal import plot_sigmoid
from src.Sinusoidal import plot_sinusoidal
from src.Tangente_hiperbolica import plot_tanh
```

### 2. Funciones Implementadas
Cada función implementada genera una gráfica de la función de activación correspondiente, junto con su derivada. 

#### a) Función Escalón (`escalon.py`)
Representa la función de Heaviside, una función discontinua usada en redes neuronales.

```python
def step_function(x):
    return np.where(x < 0, 0, 1)

def step_derivative(x):
    return np.zeros_like(x)
```

#### b) Función Gaussiana (`gaussiana.py`)

```python
def gaussian_function(x):
    return np.exp(-x**2)

def gaussian_derivative(x):
    return -2 * x * np.exp(-x**2)
```

#### c) Función Identidad (`identidad.py`)

```python
def identidad_function(x):
    return x

def identidad_derivative(x):
    return np.ones_like(x)
```

#### d) Función Lineal a Tramos (`lineal_a_tramos.py`)

```python
def piecewise_function(x):
    return np.piecewise(x, [x < 0, x >= 0], [lambda x: x, lambda x: 2 * x])

def piecewise_derivative(x):
    return np.piecewise(x, [x < 0, x >= 0], [1, 2])
```

#### e) Función ReLU (`relu.py`)

```python
def relu_function(x):
    return np.maximum(0, x)

def relu_derivative(x):
    return np.where(x > 0, 1, 0)
```

#### f) Función Sigmoide (`sigmoidal.py`)

```python
def sigmoid_function(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    s = sigmoid_function(x)
    return s * (1 - s)
```

#### g) Función Sinusoidal (`sinusoidal.py`)

```python
def sinusoidal_function(x):
    return np.sin(x)

def sinusoidal_derivative(x):
    return np.cos(x)
```

#### h) Función Tangente Hiperbólica (`tangente_hiperbolica.py`)

```python
def tanh_function(x):
    return np.tanh(x)

def tanh_derivative(x):
    return 1 - np.tanh(x)**2
```

## 📖 Uso
Para ejecutar todas las funciones de activación, usa el siguiente comando:

```sh
python main.py
```

Esto generará gráficos de todas las funciones definidas en `src/`.

## 📊 Resultados Esperados

El programa generará **8 gráficas** que muestran:
- Funciones de activación comunes.
- Sus derivadas correspondientes, calculadas numéricamente.

## 🔍 Conclusión

El proyecto visualiza funciones de activación y sus derivadas con NumPy y Matplotlib, ofreciendo una herramienta clara para analizar su rol en redes neuronales y transformaciones matemáticas.



## ⭐ ¡Dale una estrella al repo si te fue útil!
