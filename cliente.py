from xmlrpc.client import ServerProxy

# Conectando ao servidor
proxy = ServerProxy("http://192.168.18.5:8000/")

def menu(dic):
    print("\n========= Cliente XML-RPC =========")
    print("1 - Criar nova matriz")
    print("2 - Mostrar matriz")
    print("3 - Alterar elemento da matriz")
    print("4 - Somar matrizes")
    print("5 - Multiplicar matrizes")
    print("6 - Multiplicar matriz por escalar")
    print("7 - Matriz transposta")
    print("8 - Quantidade de linhas")
    print("9 - Quantidade de colunas")
    print("10 - Salvar matriz")
    print("11 - Carregar matriz")
    print("0 - Sair")

    print("\n========= MATRIZES GERADAS =========\n")
    if dic:
        for chave in dic:
            print(f"{chave}")

def escolher_matriz(dic, prompt="Escolha a matriz: "):
    while True:
        nome = input(prompt).strip()
        if nome in dic:
            return nome
        print("Matriz não encontrada. Digite um nome válido.")

def main():
    dic = {}
    while True:
        menu(dic)
        opcao = input("\nOpção: ").strip()

        if opcao == "0":
            print("Encerrando cliente.")
            break

        elif opcao == "1":  # Criar nova matriz
            nome = input("Digite um nome para a matriz: ").strip()
            lins = int(input("Número de linhas: "))
            cols = int(input("Número de colunas: "))
            matriz = proxy.new_mat(lins, cols)
            dic[nome] = matriz
            print(f"Matriz '{nome}' criada com sucesso.")

        elif opcao == "2":  # Mostrar matriz
            if not dic:
                print("Nenhuma matriz disponível.")
                continue
            nome = escolher_matriz(dic)
            print(f"\nMatriz '{nome}':")
            proxy.print_mat(dic[nome])

        elif opcao == "3":  # Alterar elemento
            if not dic:
                print("Nenhuma matriz disponível.")
                continue
            nome = escolher_matriz(dic)
            lin = int(input("Linha (0-index): "))
            col = int(input("Coluna (0-index): "))
            val = int(input("Novo valor: "))
            dic[nome] = proxy.setElem(dic[nome], val, lin, col)
            print(f"Elemento alterado na matriz '{nome}'.")

        elif opcao == "4":  # Somar matrizes
            if len(dic) < 2:
                print("É necessário ter pelo menos duas matrizes.")
                continue
            print("Escolha a primeira matriz:")
            nome1 = escolher_matriz(dic)
            print("Escolha a segunda matriz:")
            nome2 = escolher_matriz(dic)
            res = proxy.soma_mat(dic[nome1], dic[nome2])
            if res is None:
                print("Erro: Matrizes incompatíveis para soma.")
            else:
                nome_res = input("Digite o nome da matriz resultado: ").strip()
                dic[nome_res] = res
                print(f"Matriz '{nome_res}' criada com o resultado da soma.")

        elif opcao == "5":  # Multiplicar matrizes
            if len(dic) < 2:
                print("É necessário ter pelo menos duas matrizes.")
                continue
            print("Escolha a primeira matriz:")
            nome1 = escolher_matriz(dic)
            print("Escolha a segunda matriz:")
            nome2 = escolher_matriz(dic)
            res = proxy.mult_mat(dic[nome1], dic[nome2])
            if res is None:
                print("Erro: Matrizes incompatíveis para multiplicação.")
            else:
                nome_res = input("Digite o nome da matriz resultado: ").strip()
                dic[nome_res] = res
                print(f"Matriz '{nome_res}' criada com o resultado da multiplicação.")

        elif opcao == "6":  # Multiplicar por escalar
            if not dic:
                print("Nenhuma matriz disponível.")
                continue
            nome = escolher_matriz(dic)
            k = int(input("Digite o valor do escalar k: "))
            dic[nome] = proxy.vezes_k(dic[nome], k)
            print(f"Matriz '{nome}' multiplicada por {k}.")

        elif opcao == "7":  # Transposta
            if not dic:
                print("Nenhuma matriz disponível.")
                continue
            nome = escolher_matriz(dic)
            dic[nome] = proxy.transp_mat(dic[nome])
            print(f"Matriz '{nome}' transposta.")

        elif opcao == "8":  # Linhas
            if not dic:
                print("Nenhuma matriz disponível.")
                continue
            nome = escolher_matriz(dic)
            lin = proxy.get_tamlins(dic[nome])
            print(f"Matriz '{nome}' tem {lin} linhas.")

        elif opcao == "9":  # Colunas
            if not dic:
                print("Nenhuma matriz disponível.")
                continue
            nome = escolher_matriz(dic)
            col = proxy.get_tamcols(dic[nome])
            print(f"Matriz '{nome}' tem {col} colunas.")

        elif opcao == "10":  # Salvar
            if not dic:
                print("Nenhuma matriz disponível.")
                continue
            nome = escolher_matriz(dic)
            filename = input("Digite o nome do arquivo para salvar: ").strip()
            proxy.salva_mat(dic[nome], filename)
            print(f"Matriz '{nome}' salva em '{filename}'.")

        elif opcao == "11":  # Carregar
            filename = input("Digite o nome do arquivo para carregar: ").strip()
            nome = input("Digite o nome da matriz: ").strip()
            dic[nome] = proxy.carrega_mat(filename)
            print(f"Matriz '{nome}' carregada de '{filename}'.")

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()