import matplotlib.pyplot as plt
import numpy as np
from cargar_datos import leer

from matplotlib import cm
from matplotlib.ticker import LinearLocator

# Convertir coordenada x en grados de longitud
def x_to_lon(x):
	return 3.8 + (10.25 + 3.8) * -x / 5000

# Convertir coordenada y en grados de latitud
def y_to_lat(y):
	return 43.8 - (43.8 - 35.7) * y / 4500

def obtener_mapa():
	


	# Cargamos el mapa y nos quedamos con la parte que nos interesa
	mapa = leer('altitud.asc')[4500:,0:5000] #Esto carga el mapa completo
	mapa=mapa[4000:6000,0:1000]
	print('------------  Fichero Cargado -------------')
	print(mapa.shape)
	return mapa
	
def mostrar_mapa(mapa):
	fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
	X = np.arange(mapa.shape[1])
	Y = np.arange(mapa.shape[0])
	X, Y = np.meshgrid(X, Y)

	surf = ax.plot_surface(X, Y, mapa, cmap=cm.coolwarm, linewidth=0, antialiased=False)

	# Customize the z axis.
	ax.set_zlim(-1.01, 2000)
	ax.zaxis.set_major_locator(LinearLocator(10))
	# A StrMethodFormatter is used automatically
	ax.zaxis.set_major_formatter('{x:.02f}')
	ax.set_xlabel('Longitud X (°)')
	ax.set_ylabel('Altitud Y (m)')

	# Add a color bar which maps values to colors.
	fig.colorbar(surf, shrink=0.5, aspect=5)

	plt.show()

#mapa=obtener_mapa()
#mostrar_mapa(mapa)