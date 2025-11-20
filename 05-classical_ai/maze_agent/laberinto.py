import random

class Laberinto:
	def __init__(self, num_filas = 20, num_columnas = 20):
		self.num_filas = num_filas
		self.num_columnas = num_columnas
		self.mapa = [' ' * num_columnas] * num_filas
		for i in range(3, int(min(num_filas, num_columnas)/3)):
			for j in range(int(min(num_filas, num_columnas) / 8)):
				self.poner_obstaculo_aleatorio(i)
		self.poner_objeto_aleatorio()


	def poner_obstaculo(self, fila, columna, longitud, direccion):
		se_puede = True
		if direccion == 'h':
			if columna + longitud > self.num_columnas or fila >= self.num_filas:
				se_puede = False
			else:
				for c in range(columna, columna + longitud):
					if self.mapa[fila][c] != ' ':
						se_puede = False
				if se_puede:
					for c in range(columna, columna + longitud):
						array = list(self.mapa[fila])
						array[c] = '*'
						self.mapa[fila] = "".join(array)
		else:
			if fila + longitud > self.num_filas or columna >= self.num_columnas:
				se_puede = False
			else:
				for f in range(fila, fila + longitud):
					if self.mapa[f][columna] != ' ':
						se_puede = False
				if se_puede:
					for f in range(fila, fila + longitud):
						array = list(self.mapa[f])
						array[columna] = '*'
						self.mapa[f] = "".join(array)
		return se_puede
		
	def poner_obstaculo_aleatorio(self, longitud):
		intentos = 0
		insertado = False
		while intentos < 100 and not insertado:
			fila = random.randrange(0, self.num_filas)
			columna = random.randrange(0, self.num_columnas)
			direccion = 'hv'[random.randrange(0,2)]
			if self.poner_obstaculo(fila, columna, longitud, direccion):
				insertado = True
			intentos += 1
		return insertado
	
	def poner_objeto(self, fila, columna, caracter='O'):
		se_puede = True
		if self.mapa[fila][columna] == '*':
			se_puede = False
		else:
			array = list(self.mapa[fila])
			array[columna] = caracter
			self.mapa[fila] = "".join(array)
		return se_puede
	
	def poner_objeto_aleatorio(self, caracter = 'O'):
		insertado = False
		intentos = 0
		while intentos < 500 and not insertado:
			fila = random.randrange(0, self.num_filas)
			columna = random.randrange(0, self.num_filas)
			if self.poner_objeto(fila, columna):
				insertado = True
			intentos += 1
		return insertado
		
	def __str__(self):
		res = '-' * (self.num_columnas + 2)
		res = res + '\n'
		for f in range(self.num_filas):
			res = res + '|' + self.mapa[f] + '|\n'
		res = res + '-' * (self.num_columnas + 2) + '\n'
		return res

