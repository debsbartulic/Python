'''
isso NÃO é pythonico
'''


class Pato:
	def quack(self):
		print('Quack, quack')

class Pessoa:
	def quack(self):
		print('Eu faço quack igual a um pato')

def fazer_quack(obj):
	# LBYL - NÃO PYTHONICO
	if hasattr(obj, 'quack'):
		if callable(obj.quack):
			obj.quack()

pato = Pato()
fazer_quack(pato)

pessoa = Pessoa()
fazer_quack(pessoa)
