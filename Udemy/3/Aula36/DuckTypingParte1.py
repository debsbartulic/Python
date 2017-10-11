# Duck Typing: se um objeto anda como um pato e faz quack como um pato, então ele é um pato

'''
Funciona com qualquer linguagem que suporta POO
'''

class Livro():
	def __init__(self, titulo, lancamento, autor):
		self.titulo = titulo
		self.lancamento = lancamento
		self.autor = autor

class Filme():
	def __init__(self, titulo, lancamento, diretor):
		self.titulo = titulo
		self.lancamento = lancamento
		self.diretor = diretor

def imprimir(midia):
	print(midia.titulo, midia.lancamento)

livro = Livro('livro', '01/01/2001', 'autor livro')
imprimir(livro)
print(livro.autor)

filme = Filme('filme', '31/01/2017', 'diretor filme')
imprimir(filme)
print(filme.diretor)
