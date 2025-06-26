# GRAFICO DE LINEAS

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from scipy.stats import multivariate_normal

# Datos para graficar
x = [1, 2, 300000000000000, 4, 500000000000000]
y = [2, 3, 5, 700000000, 110000000000000000000]

# Crear la gráfica
plt.plot(x, y)

# Añadir título y etiquetas
plt.title("Ejemplo de gráfica simple")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")

#grafica NUEVA de pastel 
# Datos
etiquetas = ['Manzanas', 'Bananas', 'Cerezas', 'Uvas']
valores = [30, 25, 20, 25]
colores = ['red', 'yellow', 'pink', 'purple']

# Crear gráfica de pastel
plt.figure(figsize=(6, 6))
plt.pie(valores, labels=etiquetas, colors=colores, autopct='%1.1f%%', startangle=90)
plt.title('Frutas en inventario')
plt.axis('equal')  # Mantiene el círculo perfecto

#grafica NUEVA de pastel 
# Datos
etiquetas = ['Manzanas', 'Bananas', 'Cerezas', 'Uvas']
valores = [30, 25, 20, 25]
colores = ['red', 'yellow', 'pink', 'purple']

# Crear gráfica de pastel
plt.figure(figsize=(6, 6))
plt.pie(valores, labels=etiquetas, colors=colores, autopct='%1.1f%%', startangle=90)
plt.title('Frutas en inventario')
plt.axis('equal')  # Mantiene el círculo perfecto

# Mostrar gráfica
plt.show()

#impresión de una suma 
a=2234
b= 234
print("hola mundo como estás, yo estoy muy bien como tu estas ahora ?")

# DISTRO NORMAL EN 3D 
# Crear una cuadrícula de puntos (X, Y)
x = np.linspace(-3, 3, 100)
y = np.linspace(-3, 3, 100)
X, Y = np.meshgrid(x, y)
pos = np.dstack((X, Y))

# Definir parámetros de la distribución normal bivariada
mean = [0, 0]  # media en x e y
cov = [[1, 0], [0, 1]]  # matriz de covarianza (independientes)

# Crear la distribución
rv = multivariate_normal(mean, cov)
Z = rv.pdf(pos)  # calcular la densidad de probabilidad

# Graficar en 3D
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis', linewidth=0, antialiased=False)

# Etiquetas
ax.set_title('Distribución Normal Bivariada')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Densidad')

plt.tight_layout()

# Mostrar gráfica
plt.show()
