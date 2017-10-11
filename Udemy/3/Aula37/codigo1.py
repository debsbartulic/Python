class Pato:
	def quack(self):
		print('Quack, quack')

class Pessoa:
	def quack(self):
		print('Eu faço quack igual a um pato')

def fazer_quack(obj):
	if isinstance(obj, Pato):
		obj.quack()
	else:
		print('Isso tem que ser um pato')

pato = Pato()
fazer_quack(pato)

pessoa = Pessoa()
fazer_quack(pessoa)
