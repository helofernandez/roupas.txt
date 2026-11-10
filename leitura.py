# 1. Menu Interativo (Estrutura Condicional)
print("\n=== MENU DE ROUPAS ===")
print("1 - Ver Roupas Cadastradas")
print("2 - Sair")

opcao = input("Escolha uma opção: ")

if opcao == "1":
    print("\n--- Lista de Roupas ---")
    # 2. Ler dados armazenados no arquivo TXT
    try:
        arquivo = open("roupas.txt", "r")
        conteudo = arquivo.read()
        arquivo.close()

        # 3. Exibir informações no terminal
        if conteudo == "":
            print("Nenhuma roupa cadastrada ainda.")
        else:
            print(conteudo)
    except FileNotFoundError:
        print("Nenhuma roupa cadastrada ainda (arquivo não encontrado).")

elif opcao == "2":
    print("Saindo do programa...")

else:
    print("Opção inválida! Escolha 1 ou 2.")