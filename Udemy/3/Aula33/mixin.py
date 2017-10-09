'''
 Quando utilizar?
 - Se deseja reutilizar uma determinada feature em várias classes diferentes.
 - Para melhorar modularidade

 Mixins é uma forma controlada de adicionar funcionalidades as classes.

 Propriedades: 
 1) não deve ser extendida
 2) não deve ser instanciada

 E python o conceito de mixins é implementado utilizando herança múltipla.

'''

class Livro(object):
	def __init__(self, nome, conteudo):
		self.nome = nome
		self.conteudo = conteudo


class LivroHTMLMixin(object):
	def renderizar(self):
		return('<html><title>%s</title><body>%s</body></html>') % (self.nome, self.conteudo)

class LivroHTML(Livro, LivroHTMLMixin):
	pass


livro_html = LivroHTML('Algum livro', 'blá blá blá')

print(livro_html.renderizar())
