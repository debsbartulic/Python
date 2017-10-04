# A mais longa substring em ordem alfabética
# Exemplo:
# azcbobobegghakl
# az, bo, bo, beggh, eggh, ggh, gh
# São substrings da string que estão em ordem alfabética, logo ele quer a maior dela, que seria beggh.
def obter_mais_longa_substring(s):
	d = { 'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26 }
	listSaida = []
	st = ''
	aux = 0
	for i in range(0, len(s)):
            st = st + s[i]
            for j in range(i+1, len(s)):
                if (s[j] >= s[j-1]):
                    st = st + s[j]
                else:
			if (len(st) > 0):
			    listSaida.append(st)
			    st = ''
        print(listSaida)
