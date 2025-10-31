from xmlrpc.server import SimpleXMLRPCServer


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
			print('%3d' % int(m[linhas][colunas]), ' ', end='')
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

#OK!
def salva_mat(m, filename):

	lin = len(m)
	col = len(m[0])


	arq = open(filename, 'w')
	

	for linhas in range(lin):
		for colunas in range(col):

			arq.write(f"{m[linhas][colunas]} ")
		arq.write('\n')
	arq.close()

#OK!
def carrega_mat(filename):
	arq = open(filename, 'r')

	linha = arq.readline()
	mat = []

	while linha != '':
		linha = linha.split()
		mat.append(linha)
		linha = arq.readline()


	arq.close()
	return mat





#==============Configuração do Servidor===============

server = SimpleXMLRPCServer(("0.0.0.0", 8000))
print("Servidor RPC rodando na porta 8000...")


#Registrar Funções

server.register_function(new_mat, "new_mat")
server.register_function(print_mat, "print_mat")
server.register_function(setElem, "setElem")
server.register_function(soma_mat, "soma_mat")
server.register_function(mult_mat, "mult_mat")
server.register_function(vezes_k, "vezes_k")
server.register_function(transp_mat, "transp_mat")
server.register_function(get_tamlins, "get_tamlins")
server.register_function(get_tamcols, "get_tamcols")
server.register_function(salva_mat, "salva_mat")
server.register_function(carrega_mat, "carrega_mat")

server.serve_forever()