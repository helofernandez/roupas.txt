# Funcao para salvar a roupa no arquivo TXT (Persistencia de Dados)
def salvar_roupa(nome, preco):
    # O modo 'a' (append) adiciona o texto ao final do arquivo sem apagar o que ja existe
    with open("roupas.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{nome} , {preco}\n")
    print(f"👕 Roupa '{nome}' cadastrada com sucesso!\n")


# Funcao principal do cadastro
def menu():
    while True:
        print("=== CADASTRO DE ROUPAS ===")
        print("1 - Cadastrar Nova Roupa")
        print("2 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Digite o nome da roupa: ")

            # Validacao simples para garantir que o preco seja apenas numeros
            while True:
                preco = input("Digite o preço da roupa (ex: 150): ")
                if preco.isdigit():
                    break
                print("❌ Erro: O preço deve conter apenas números inteiros. Tente novamente.")

            salvar_roupa(nome, preco)

        elif opcao == "2":
            print("Saindo do programa. Até logo!")
            break

        else:
            print("❌ Opção inválida! Tente novamente.\n")


# Executa o programa
if __name__ == "__main__":
    menu()