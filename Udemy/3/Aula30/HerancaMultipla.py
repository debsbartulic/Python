class Relogio:

	def __init__(self, hora=0, minuto=0, segundo=0, *args, **kwargs):
		super(Relogio, self).__init__(*args, **kwargs)
		self.hora = hora
		self.minuto = minuto
		self.segundo = segundo

	def ajusta_hora(self, hora, minuto, segundo=0):
		self.hora = hora
		self.minuto = minuto
		self.segundo = segundo

	def __str__(self):
		return "{0:02d}:{1:02d}:{2:02d}".format(self.hora, self.minuto, self.segundo)

	def tick(self):
		if self.segundo == 59:
			self.segundo = 0
			if self.minuto == 59:
				self.minuto = 0
				if self.hora == 23:
					self.hora = 0
				else:
					self.hora = 1
			else:
				self.minuto += 1
		else:
			self.segundo += 1

'''rel = Relogio(23, 59, 59)
print(rel)
rel.tick()
print(rel)'''

class Calendario:

	meses = (31, 28, 31, 30, 31, 30, 31, 31, 30 ,31 ,30 ,31)

	def __init__(self, dia, mes, ano, *args, **kwargs):
		super(Calendario,self).__init__(*args, **kwargs)
		self.dia = dia
		self.mes = mes
		self.ano = ano

	def ajustar_data(self, dia, mes, ano):
		self.dia = dia
		self.mes = mes
		self.ano = ano

	def __str__(self):
		return "{0:02d}/{1:02d}/{2:4d}".format(self.dia, self.mes, self.ano)

	def avancar(self):
		dia_max = Calendario.meses[self.mes - 1]
		if self.dia == dia_max:
			self.dia = 1
			if self.mes == 12:
				self.mes = 1
				self.ano += 1
			else:
				self.mes += 1
		else:
			self.dia += 1

'''cal = Calendario(28,2,2016)
print(cal)
cal.avancar()
print(cal)'''

class CalendarioRelogio(Relogio, Calendario):
    
    def __init__(self, hora, minuto, segundo, dia, mes, ano):
        super(CalendarioRelogio, self).__init__(hora=hora, minuto=minuto, segundo=segundo, dia=dia, mes=mes, ano=ano)

    def __str__(self):
        return  Relogio.__str__(self) + ' , ' + Calendario.__str__(self)

    def tick(self):
        hora_anterio = self.hora
        Relogio.tick(self)
        if(self.hora < hora_anterio):
            self.avancar()

cal_rel = CalendarioRelogio(23, 59, 59, 31, 12, 2015)
print(cal_rel)
cal_rel.tick()
print(cal_rel)


#exibe a ordem de execução dos métodos de acordo com a ordem das heranças
print(CalendarioRelogio.mro())
