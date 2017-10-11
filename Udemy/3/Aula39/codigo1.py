# Esse modo não é pythonico, é a maneira comum de utilização em outras linguagens: C#, Java

class P():
	def __init__(self, x):
		self.__x = x #atributo privado
		# self.x = x #atributo público

	def getX(self):
		return self.__x

	def setX(self, x):
		if x > 0:
			self.__x = x

p = P(2)
print(p.getX())
p.setX(5)
print(p.getX())

