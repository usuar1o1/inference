import matplotlib.pyplot as plt
import numpy as np

# Crear un rango de valores x
x = np.linspace(0, 10, 100)

# Funciones a graficar
y1 = np.sin(x)
y2 = np.cos(x)

# Crear la figura y el eje
fig, ax = plt.subplots()

# Graficar las dos funciones con diferentes estilos
ax.plot(x, y1, label='sin(x)', color='blue', linestyle='-', linewidth=2)
ax.plot(x, y2, label='cos(x)', color='red', linestyle='--', linewidth=2)

# Añadir título y etiquetas
ax.set_title('Gráfica avanzada: sin(x) y cos(x)')
ax.set_xlabel('x')
ax.set_ylabel('y')

# Añadir cuadrícula
ax.grid(True, linestyle='--', alpha=0.7)

# Añadir leyenda
ax.legend()

# Anotar un punto importante en sin(x)
max_sin_x = np.pi / 2
max_sin_y = np.sin(max_sin_x)
ax.annotate('Máximo de sin(x)', xy=(max_sin_x, max_sin_y), xytext=(max_sin_x+1, max_sin_y),
            arrowprops=dict(facecolor='black', shrink=0.05))

# Anotar un punto importante en cos(x)
min_cos_x = np.pi
min_cos_y = np.cos(min_cos_x)
ax.annotate('Mínimo de cos(x)', xy=(min_cos_x, min_cos_y), xytext=(min_cos_x+1, min_cos_y-0.5),
            arrowprops=dict(facecolor='black', shrink=0.05))

# Mostrar la gráfica
plt.show()
