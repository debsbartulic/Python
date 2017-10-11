class Pato:
	def quack(self):
		print('Quack, quack')

class Pessoa:
	def quack(self):
		print('Eu faço quack igual a um pato')

def fazer_quack(obj):
	# EAFP - EASIER TO ASK FOR FORGIVENESS THAN PERMISSION
	# É PYTHONICO
	try:
		obj.quack()
	except AttributeError as e:
		print(e)

pato = Pato()
fazer_quack(pato)

pessoa = Pessoa()
fazer_quack(pessoa)
