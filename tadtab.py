def new_tab():

	tab = []
	lst = []


	#Criar a tabela
	for linha in range(3):
		for colunas in range(3):
			lst.append("X")
		tab.append(lst)

	return tab

def print_tab(tab):

	for linha in range(3):
		for coluna in range(3):
			print(tab[linha][coluna] + ' ',end='')
		print("\n", end='')


def status(tab):
	

	#sts1 = "jg1 venceu"
	#sts2 = "jg2 venceu"
	#sts4 = "cheio"
	sts = ''	


	if " " not in tab:
		sts = "cheio"


	for linha in (range(3)):
		for coluna in range(3):
			if tab[linha][coluna] == "X":
				if tab[linha][coluna] + tab[linha][coluna + 1] + (tab[linha][coluna + 2]) == "XXX":
					sts = "jg1 w"
				elif tab[linha][coluna] + tab[linha + 1][coluna] + tab[linha + 2][coluna] == "XXX":
					sts = "jg1 w"
				elif tab[linha][coluna] + tab[linha + 1][coluna + 1] + tab[linha + 2][coluna + 2] == "XXX":
					sts = "jg1 w"
				elif tab[linha][coluna] + (tab[linha][coluna - 1]) + ((tab[linha][coluna - 2])) == "XXX":
					sts = "jg1 w"
				elif tab[linha][coluna] + tab[linha - 1][coluna] + tab[linha - 2][coluna] == "XXX":
					sts = "jg1 w"
				elif tab[linha][coluna] + tab[linha - 1][coluna - 1] + tab[linha - 2][coluna - 2] == "XXX":
					sts = "jg1 w"
			elif tab[linha][coluna] == "O":
				if tab[linha][coluna] + (tab[linha][coluna + 1]) + ((tab[linha][coluna + 2])) == "OOO":
					sts = "jg2 w"
				elif tab[linha][coluna] + tab[linha + 1][coluna] + tab[linha + 2][coluna] == "OOO":
					sts = "jg2 w"
				elif tab[linha][coluna] + tab[linha + 1][coluna + 1] + tab[linha + 2][coluna + 2] == "OOO":
					sts = "jg2 w"
				elif tab[linha][coluna] + (tab[linha][coluna - 1]) + ((tab[linha][coluna - 2])) == "OOO":
					sts = "jg2 w"
				elif tab[linha][coluna] + tab[linha - 1][coluna] + tab[linha - 2][coluna] == "OOO":
					sts = "jg2 w"
				elif tab[linha][coluna] + tab[linha - 1][coluna - 1] + tab[linha - 2][coluna - 2] == "OOO":
					sts = "jg2 w"


	return sts


def jogar():
	pass
