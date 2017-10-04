# Tupla Par
# Vamos resolver um exercício que envolve tuplas? Você deverá desenvolver uma função chamada tupla_par. 
# Essa função recebe uma tupla como entrada e retorna uma nova tupla como saída onde os elementos dessa nova tupla são os elementos 
# cujos índices são números pares. Lembrando que o Python indexa a partir do zero.
# Exemplo de tupla de entrada: ('oi', 'estou', 'estudando', 'poo')
# Tupla que deve ser retornada: ('oi', 'estudando') #

def tupla_par(tupla):
	listSaida = []
	for ponteiro in range(0,len(tupla)):
		if (ponteiro % 2 == 0):
			listSaida.append(tupla[ponteiro])
	return tuple(listSaida)
