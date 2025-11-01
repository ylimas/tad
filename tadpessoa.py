from xmlrpc.server import SimpleXMLRPCServer


def new_pessoa(nome, peso, altura, idade): 	

	#criar o dicionário
	tadpessoa = {"Nome": "", "Peso": 0, "Altura": 0, "Idade": 0}


	#preencher os dados
	tadpessoa["Nome"] = str(nome)
	tadpessoa["Peso"] = float(peso)
	tadpessoa["Altura"] = float(altura)
	tadpessoa["Idade"] = int(idade)

	return tadpessoa

def maiorIdade(tadpessoa): #retorna True se for de maior
	if tadpessoa["Idade"] >= 18:
		return True
	else:
		return False

def imc(tadpessoa):

	imc = tadpessoa["Peso"] / (tadpessoa["Altura"] ** 2)

	return imc
	

def getNome(tadpessoa):
	return tadpessoa["Nome"]

def getPeso(tadpessoa):
	return tadpessoa["Peso"]

def getAltura(tadpessoa):
	return tadpessoa["Altura"]

def getIdade(tadpessoa):
	return tadpessoa["Idade"]


server = SimpleXMLRPCServer(("localhost", 8000))
print("Servidor RPC rodando na porta 8000...")

server.register_function(new_pessoa, "new_pessoa")
server.register_function(maiorIdade, "maiorIdade")
server.register_function(imc, "imc")
server.register_function(getNome, "getNome")
server.register_function(getPeso, "getPeso")
server.register_function(getIdade, "getIdade")
server.register_function(getAltura, "getAltura")

server.serve_forever()