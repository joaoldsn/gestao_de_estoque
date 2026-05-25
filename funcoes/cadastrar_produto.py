def cadastrar_produto(nome, preco, quantidade):
    nome = input('Digite o nome do produto: ')
    categoria = input('Digite a categoria do produto: ')
    quantidade=int(input('Digite a quantidade do produto: '))
    preco=float(input('Digite o preço do produto: '))
    produto = {
        'nome': nome,
        'categoria': categoria,
        'quantidade': quantidade,
        'preço': preco,
    }

        estoque.append(produto)
        print('Produto cadastrado com sucesso!')

