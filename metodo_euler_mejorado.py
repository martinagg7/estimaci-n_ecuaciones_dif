import numpy as np
import pandas as pd

# Definir la ecuación diferencial y'=x*sqrt(y)
def f(x, y):
    return x * np.sqrt(y)

# Valores iniciales
x0 = 1.0  # Valor inicial de x
y0 = 4.0  # Valor inicial de y

# Paso de integración
h = 0.2

# Punto final donde queremos estimar y
x_target = 1.6

# Inicializar listas para almacenar los valores de x, y y los valores de k
x_values = [x0]
y_values = [y0]
k1_values = []
k2_values = []
k3_values = []
k4_values = []

# Aplicar el método de Runge-Kutta de cuarto orden (RK4) para avanzar en la solución
while x_values[-1] < x_target:
    x = x_values[-1]
    y = y_values[-1]
    
    k1 = h * f(x, y)
    k2 = h * f(x + 0.5 * h, y + 0.5 * k1)
    k3 = h * f(x + 0.5 * h, y + 0.5 * k2)
    k4 = h * f(x + h, y + k3)
    
    y_new = y + (k1 + 2 * k2 + 2 * k3 + k4) / 6.0
    
    x_new = x + h

    x_values.append(x_new)
    y_values.append(y_new)
    k1_values.append(k1)
    k2_values.append(k2)
    k3_values.append(k3)
    k4_values.append(k4)

# Crear una tabla de valores utilizando Pandas
data = {'x': x_values[:-1], 'y': y_values[:-1], 'k1': k1_values, 'k2': k2_values, 'k3': k3_values, 'k4': k4_values}
df = pd.DataFrame(data)

# Imprimir la tabla de valores
print(df)
