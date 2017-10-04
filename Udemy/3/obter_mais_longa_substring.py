# A mais longa substring em ordem alfabética
# Exemplo:
# azcbobobegghakl
# az, bo, bo, beggh, eggh, ggh, gh
# São substrings da string que estão em ordem alfabética, logo ele quer a maior dela, que seria beggh.
def obter_mais_longa_substring(s):
	d = { 'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26 }
	listSaida = []
	st = ''
	maior = ''
	for i in range(0, len(s)):
            st = st + s[i]
            for j in range(i+1, len(s)):
                if (d[s[j]] >= d[s[j-1]]):
                    st = st + s[j]
                else:
			if (len(st) > 1):
			    listSaida.append(st)
			    st = ''
			    break;
        for item in lista:
		if (len(item) > len(maior)):
			maior = item
	print(maior)
		
