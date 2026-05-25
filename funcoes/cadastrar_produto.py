def cadastrar_produto(nome, preco, quantidade):
    nome = input('Digite o nome do produto: ')
    quantidade=int(input('Digite a quantidade do produto: '))
    preco=float(input('Digite o preço do produto: '))
    produto = {
        'nome': nome,
        'quantidade': quantidade,
        'preço': preco,
    }

        estoque.append(produto)
        print('Produto cadastrado com sucesso!')
