#Importar bibliotecas
import numpy as np
import matplotlib.pyplot as plt

#Dominio y rango de la función
x = np.arange(-np.pi, np.pi, 0.2)
y = np.cos(x)

#Graficar la funcion
plt.plot(x,y, "--o", label = "$y= cos(x)$")
plt.legend(loc=1)
plt.grid()
plt.savefig("GrafiaCos.png")
plt.show()