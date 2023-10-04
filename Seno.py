#Importar bibliotecas
import numpy as np
import matplotlib.pyplot as plt

#Dominio y rango de la función
x = np.arange(-np.pi, np.pi, 0.2)
y = np.sin(x)

#Graficar la funcion
plt.plot(x,y, "--o", label = "$y= sin(x)$")
plt.legend(loc=1)
plt.savefig("GrafiaSeno.png")
plt.grid()
plt.show()