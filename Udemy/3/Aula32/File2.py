class Veiculo():
	pass

class Carro(Veiculo):
	pass

class Trem(Veiculo):
	pass

Veiculo.__mro__

Carro.__mro__

Trem.__mro__

class CarroTrem(Carro, Trem):
	pass

CarroTrem.__mro__
