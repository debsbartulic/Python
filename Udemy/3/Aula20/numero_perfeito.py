# Número perfeito
# Desenvolva a função numero_perfeito que receberá como entrada um número e retornará True se ele for perfeito e False caso contrário.
def numero_perfeito(num):
	total = 0
	for i in range(1, num):
		if (num % i == 0):
			total = total + i
	if (total == num):
		return True
	else:
		return False
