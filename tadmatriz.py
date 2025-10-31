import random

#OK!
def new_mat(lins, cols):
	
	mat = []

	for linhas in range(lins):
		linha = []
		for colunas in range(cols):
			linha.append(random.randint(1, 9))

		mat.append(linha)

	return mat

#OK!
def print_mat(m):

	lin = len(m)
	col = len(m[0])

	for linhas in range(lin):
		for colunas in range(col):
			print('%3d' % m[linhas][colunas], ' ', end='')
		print()

#OK!
def setElem(m, valor, linh, col):

	m[linh][col] = valor

	return m

#OK!
def soma_mat(mA, mB):
	if len(mA) == len(mA[0]) and len(mB) == len(mB[0]):
		lst = []
		num = 0
		soma = []

		for linha in range(len(mA)):
			for coluna in range(len(mB)):
				num = mA[linha][coluna] + mB[linha][coluna]
				lst.append(num)	
			soma.append(lst)
			lst = []
			num = 0

		return soma

	else:
		return None

#OK!
def mult_mat(mA, mB): 
	
	if len(mA) == len(mA[0]) and len(mB) == len(mB[0]):


		lst = []
		num = 0
		mult = []

		for linha in range(len(mA)):
			for coluna in range(len(mB)):
				num = mA[linha][coluna] * mB[linha][coluna]
				lst.append(num)

			mult.append(lst)
			lst = []
			num = 0

		return mult

	else:
		return None

#OK!
def vezes_k(m, k):
	
	lst = []
	num = 0
	mult = []

	for linha in range(len(m)):
		for coluna in range(len(m[0])):
			num = m[linha][coluna] * k
			lst.append(num)
				
		mult.append(lst)
		lst = []
		num = 0

	return mult

#OK!
def transp_mat(m):
	
	lins = len(m) #5
	cols = len(m[0]) #2

	trans = []
	for i in range(cols): #2
		linha = [0] * lins #5
		trans.append(linha)

	for linha in range(cols):
		for coluna in range(lins):
			trans[linha][coluna] = m[coluna][linha]

	return trans

#OK!
def get_tamlins(m):

	return len(m)

#OK!
def get_tamcols(m):

	return len(m[0])


def salva_mat(m, filename):

	lin = len(m)
	col = len(m[0])


	arq = open(filename, 'w')
	

	for linhas in range(lin):
		for colunas in range(col):

			arq.write(f"{m[linhas][colunas]} ")
		arq.write('\n')
	arq.close()


def carrega_mat(filename):
	arq = open(filename, 'r')

	linhas = arq.readlines()
	mat = []
	for linha in linhas:
		lin = linha.strip().split(" ")
		mat.append(lin)

	arq.close()
	return mat


