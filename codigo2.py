# GRAFICO DE LINEAS

import matplotlib.pyplot as plt

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

# Mostrar gráfica
plt.show()

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
