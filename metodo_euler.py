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

# Inicializar listas para almacenar los valores de x y y
x_values = [x0]
y_values = [y0]

# Aplicar el método de Euler para avanzar en la solución
while x_values[-1] < x_target:
    x_new = x_values[-1] + h
    y_new = y_values[-1] + h * f(x_values[-1], y_values[-1])
    x_values.append(x_new)
    y_values.append(y_new)

# Calcular la estimación de y en x_target
y_target = y_values[-1]

# Crear una tabla de valores utilizando Pandas
data = {'x': x_values, 'y': y_values}
df = pd.DataFrame(data)

# Imprimir la tabla de valores
print(df)

print(f"La estimación de y({x_target}) es {y_target}")
