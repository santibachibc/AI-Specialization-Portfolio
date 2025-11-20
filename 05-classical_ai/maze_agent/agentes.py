from laberinto import Laberinto
import random

class AgenteLaberinto:
	def __init__(self, laberinto = None, fila = None, columna = None, nombre = 'A'):
		if laberinto == None:
			self.laberinto = Laberinto()
		else:
			self.laberinto = laberinto
		if  fila == None or columna == None:
			colocado = False
			while not colocado:
				self.fila = random.randrange(0, self.laberinto.num_filas)
				self.columna = random.randrange(0, self.laberinto.num_columnas)
				if self.laberinto.mapa[self.fila][self.columna] == ' ':
					colocado = True
		else:
			self.fila = fila
			self.columna = columna
		self.nombre = nombre
		#self.laberinto.poner_objeto(self.fila, self.columna, self.nombre)
		self.pasos = 0

	def mirar_norte(self):
		if self.fila == 0:
			return None
		else:
			return self.laberinto.mapa[self.fila-1][self.columna]

	def mirar_sur(self):
		if self.fila == self.laberinto.num_filas-1:
			return None
		else:
			return self.laberinto.mapa[self.fila+1][self.columna]

	def mirar_este(self):
		if self.columna == 0:
			return None
		else:
			return self.laberinto.mapa[self.fila][self.columna-1]

	def mirar_oeste(self):
		if self.columna == self.laberinto.num_columnas-1:
			return None
		else:
			return self.laberinto.mapa[self.fila][self.columna+1]

	def mover_norte(self):
		if self.fila == 0 or self.laberinto.mapa[self.fila-1][self.columna] == '*':
			pass
		else:
			self.laberinto.poner_objeto(self.fila, self.columna, '·')
			self.fila -= 1
			self.laberinto.poner_objeto(self.fila, self.columna, self.nombre)

	def mover_sur(self):
		if self.fila == self.laberinto.num_filas or self.laberinto.mapa[self.fila+1][self.columna] == '*':
			pass
		else:
			self.laberinto.poner_objeto(self.fila, self.columna, '·')
			self.fila += 1
			self.laberinto.poner_objeto(self.fila, self.columna, self.nombre)

	def mover_este(self):
		if self.columna == 0 or self.laberinto.mapa[self.fila][self.columna-1] == '*':
			pass
		else:
			self.laberinto.poner_objeto(self.fila, self.columna, '·')
			self.columna -= 1
			self.laberinto.poner_objeto(self.fila, self.columna, self.nombre)

	def mover_oeste(self):
		if self.columna == self.laberinto.num_columnas or self.laberinto.mapa[self.fila][self.columna+1] == '*':
			pass
		else:
			self.laberinto.poner_objeto(self.fila, self.columna, '·')
			self.columna += 1
			self.laberinto.poner_objeto(self.fila, self.columna, self.nombre)

	# Aquí se toma la decisión de qué hacer en cada movimiento
	def mover(self):
		encontrado = False
		if self.mirar_norte() == 'O' or self.mirar_sur() == 'O' or self.mirar_este() == 'O' or self.mirar_oeste() == 'O':
			encontrado = True
		else:
			if self.mirar_norte() == ' ':
				self.mover_norte()
			elif self.mirar_este() == ' ':
				self.mover_este()
			elif self.mirar_sur() == ' ':
				self.mover_sur()
			elif self.mirar_oeste() == ' ':
				self.mover_oeste()
			elif self.mirar_norte() != '*' and self.mirar_norte() != None:
				self.mover_norte()
			elif self.mirar_este() != '*' and self.mirar_este() != None:
				self.mover_este()
			elif self.mirar_sur() != '*' and self.mirar_sur() != None:
				self.mover_sur()
			elif self.mirar_oeste() != '*' and self.mirar_oeste() != None:
				self.mover_oeste()
			self.pasos += 1
		return encontrado
	
	def buscar(self):
		encontrado = False
		while not encontrado:
			encontrado = self.mover()
			#if (self.pasos % 10 == 0):
			input()
			print(self.laberinto)
		print('Número de pasos: ', self.pasos)
		print(self.laberinto)
