import random

def new_mat(lins, cols):
	
	mat = []

	for linhas in range(lins):
		linha = []
		for colunas in range(cols):
			linha.append(random.radint(1, 10))

		mat.append(linha)

	return mat

def print_mat(m):

	lin = len(m[0])
	col = len(m)
	for linhas in range(lin):
		for colunas in range(col):
			print('%5d' % m[linhas][colunas], ' ', end='')
		print()


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

def vezes_k(m, k):
	
	lst = []
	num = 0
	mult = []

	for linha in len(m):
		for coluna in len(m[0]):
			num = mA[linha][coluna] * k
			lst.append(num)
				
		mult.append(lst)
		lst = []
		num = 0

	return mult

def transp_mat(m):
	
	lins = len(m)
	cols = len(m[0])

#criar uma nova matriz inversa vazia
	
	trans = []
	for linhas in range(cols):
		linha = []
		for colunas in range(linhas):
			linha.append(0)
		trans.append(linha)

#inserir os valores da matriz nos seus lugares
	for linha in m:
		for coluna in linha:
			trans[linha][coluna] = m[coluna][linha]

	return trans


def get_tamlins(m):

	return len[m]

def get_tamcols(m):
#retorna a quantidade de colunas da mat
	return len(m[0])

def salva_mat(m, filename):

	lin = len(m[0])
	col = len(m)


	arq = open(filename, 'w')

	for linhas in range(lin):
		for colunas in range(col):
			arq.write('%5d' % m[linhas][colunas], ' ', end='')
		arq.write('\n')
	arq.close()


def carrega_mat(filename):
	arq.open(filename, 'r')

	linhas = arq.readlines()
	mat = linhas.strip().split(" ")

	return mat

def setElem(m, valor, linh, col):

	m[linh][col] = valor

	return m



