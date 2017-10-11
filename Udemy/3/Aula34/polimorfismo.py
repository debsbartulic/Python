# Polimorfismo
# Pode demonstrar o polimorfimos nas chamadas de métodos, ou seja, significa, uma chamada de metodo pode ocorrer de várias formas
# o objeto que faz a chamada do método é quem decide a forma.

import math

class Forma():
	def __init__(self):
		print('Construtor da forma')

	def area(self):
		print('Área da forma')

	def perimetro(self):
		print('Perímetro da forma')

	def descricao(self):
		print('Descrição da forma')

class Quadrado(Forma):
	def __init__(self, lado):
		self.lado = lado

	def area(self):
		return self.lado ** 2

	def perimetro(self):
		return self.lado * 4

class Circulo(Forma):
	
	def __init__(self, raio):
		self.raio = raio

	def area(self):
		return math.pi * self.raio ** 2

	def perimetro(self):
		return 2 * math.pi  * self.raio

	def descricao(self):
		print('Descrição do Círculo')



quad = Quadrado(2)
print('Área: %d' % quad.area())
print('Perímetro: %d' % quad.perimetro())
quad.descricao()


circ = Circulo(3)
print('Área: %f' % circ.area())
print('Perímetro: %f' % circ.perimetro())
circ.descricao()
