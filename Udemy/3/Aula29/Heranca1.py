class Funcionario:
	def __init__(self, nome, salario, cpf, x):
		self.nome = nome
		self.salario = salario
		self.cpf = cpf
		self.__x = x
	def get_bonificacao(self):
		return self.salario * 0.20

class Gerente(Funcionario):

	def __init__(self, nome, salario, cpf, x, senha):
		super().__init__(nome, salario, cpf, x)
		self.senha = senha

	def get_bonificacao(self):
		return super().get_bonificacao() + 1000

g = Gerente('Debora', 3000, '322.222.222-33', 2, 3333)
print(g.nome)
print(g.salario)
print(g.cpf)
print(g.get_bonificacao())
print(g.senha)

# o "x" é exclusivo da classe pai!
