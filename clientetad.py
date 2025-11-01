

from xmlrpc.client import ServerProxy
#import tadpessoa as tpessoa

proxy = ServerProxy("http://localhost:8000/")
print("Conectando na porta local...\n.\n.\n.\n.")



print("Rodando o programa...\n.\n.\n.")
def main():


	arq = open("pessoas.txt", "r", encoding="utf-8")
	linha = arq.readline()
	pessoa = {}
	pessoas	= []
	lst = []

	while linha != "":
		lst = linha.strip().split(", ")


		nome = str(lst[0])
		peso = float(lst[1])
		altura = float(lst[2])
		idade =  int(lst[3])

		pessoa = proxy.new_pessoa(nome, peso, altura, idade)
		pessoas.append(pessoa)
		linha = arq.readline()

	for pessoa in pessoas:
		print(f"NOME: {pessoa["Nome"]}")
		print(f"IDADE: {pessoa["Idade"]} anos")
		print(f"PESO: {pessoa["Peso"]} Kg")
		print(f"ALTURA: {pessoa["Altura"]}m")
		if proxy.maiorIdade(pessoa) == True:

			print(f"\nIMC: {proxy.imc(pessoa)}\n\n")




	arq.close()
main()