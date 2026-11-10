# 1. abre o arquivo
try:
    arquivo = open("roupas.txt", "r")
    linhas = arquivo.readlines()
    arquivo.close()
except FileNotFoundError:
    linhas = []

# 2. inicializa as variaveis
maior_preco = 0
roupa_mais_cara = ""

# 3. percorre as linhas
for linha in linhas:
    if "," not in linha:
        continue

    nome, preco = linha.strip().split(",", 1)
    nome = nome.strip()
    preco = preco.strip()

    try:
        if int(preco) > maior_preco:
            maior_preco = int(preco)
            roupa_mais_cara = nome
    except ValueError:
        continue

# 4. exibe o resultado
print(f"roupa mais cara: {roupa_mais_cara} com R$ {maior_preco}")