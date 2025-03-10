import matplotlib.pyplot as plt
import numpy as np

# Crear un array de x y y
x = np.linspace(-10, 10, 400)

# Crear las funciones tangente y cotangente
tangente = np.tan(x)
#seno = np.sin(x)
#coseno = np.cos(x)
#cotangente = coseno/seno
cotangente = 1/tangente

# Definimos el tamaño de la gráfica
plt.figure(figsize = (10, 3))

# Dibujar las funciones tagente y cotangente en la misma gráfica
plt.plot(x, tangente, color = "blue", linewidth = 1)
plt.plot(x, cotangente, color = "green", linewidth = 1)

# Establecemos el título de la gráfica y de los ejes X e Y 
plt.title("Gráficas de la tangente y la cotangente")
plt.xlabel("x")
plt.ylabel("y")

# Agregamos la leyenda al gráfico, fuera del gráfico, arriba a la derecha
plt.legend(["tan(x)", "cot(x)"], bbox_to_anchor = (1.1, 1), loc = "upper right",  prop={"size": 7})

# Establecemos el color y grosor de la línea divisora del eje X
plt.axhline(0, color = "gray", lw = 1)
# Establecemos el color y grosor de la línea divisora del eje Y
plt.axvline(0, color = "gray", lw = 1)

# Mostramos las gráficas del seno y el coseno
plt.show()