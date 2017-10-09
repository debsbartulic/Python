Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> class MinhaClasse(object):
	pass

>>> class Pessoa:
	def __init__(self, nome, idade):
		self.nome = nome
		self.idade = idade

>>> 
>>> class PessoaFisica(Pessoa):
	def __init__(self, cpf, nome, idade):
		Pessoa.__init__(self, nome, idade)
		self.cpf = cpf

		
>>> p1 = Pessoa('Debora', 35)
>>> pi.nome
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    pi.nome
NameError: name 'pi' is not defined
>>> p1.nome
'Debora'
>>> p1.idade
35
>>> p_Fisica = PessoaFisica('999.999.999-99', p1.nome, p1.idade)
>>> p_Fisica.cpf
'999.999.999-99'
>>> p_Fisica.nome
'Debora'
>>> p_Fisica.idade
35
>>> 
