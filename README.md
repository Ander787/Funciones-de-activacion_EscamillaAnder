# README - Funciones de Activación en Redes Neuronales

## Información del Proyecto  
**Materia:** Sistemas de Visión Artificial  
**Tarea:** Tarea 2.1 - Gráficas de funciones de activación con su derivada  
**Estudiante:** Ander Heinrich Escamilla Wong
**Fecha:** 03/03/2025  

---

## Descripción General  
Este repositorio contiene un conjunto de scripts en Python que grafican diversas funciones de activación junto con sus derivadas. Cada función está implementada en su propio módulo dentro de la carpeta `src/`.  

El archivo `main.py` es el punto de entrada para ejecutar todas las gráficas de manera conjunta.  

---

## Funciones de Activación en Redes Neuronales  
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

## Requisitos Previos
Antes de ejecutar el código, asegúrate de tener instaladas las siguientes bibliotecas en tu entorno de Python:

```sh
pip install numpy matplotlib
```

## Estructura del Repositorio

```
proyecto_funciones/
│── src/                        # Código fuente
│   ├── escalon.py              # Función Escalón
│   ├── gaussiana.py            # Función Gaussiana
│   ├── identidad.py            # Función Identidad
│   ├── lineal_a_tramos.py      # Función Lineal a Tramos
│   ├── relu.py                 # Función ReLU
│   ├── sigmoidal.py            # Función Sigmoide
│   ├── sinusoidal.py           # Función Sinusoidal
│   ├── tangente_hiperbolica.py # Función Tangente Hiperbólica
│── main.py                     # Punto de entrada para ejecutar todas las funciones
│── README.md                   # Este documento
```

## Uso
Para ejecutar todas las funciones, usa el siguiente comando:

```sh
python main.py
```

## Contribuciones
Si deseas contribuir, por favor realiza un fork del repositorio, crea una rama con tus cambios y envía un pull request.

## Licencia
Este proyecto está bajo la licencia MIT.
