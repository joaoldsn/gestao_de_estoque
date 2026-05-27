from funcoes.conexao import conexao, cursor

def cadastrar_produto():

    nome = input('\nDigite o nome do produto: ')
    categoria = input('Digite a categoria: ')
    quantidade = int(input('Digite a quantidade: '))
    preco = float(input('Digite o preço: R$'))

    print('\n===== CONFIRMAÇÃO =====')
    print(f'Nome: {nome}')
    print(f'Categoria: {categoria}')
    print(f'Quantidade: {quantidade}')
    print(f'Preço Unitário: R$ {preco:.2f}')   

    decisao = input('\nConfirmar cadastro? (sim/não):\n')

    if decisao == 'sim':

        cursor.execute("""
        INSERT INTO produtos (nome, categoria, preco, quantidade)
        VALUES (?, ?, ?, ?)
        """, (nome, categoria, preco, quantidade))

        conexao.commit()

        produto_id = cursor.lastrowid

        print('\nProduto cadastrado com sucesso!')
        print(f'ID do produto: {produto_id}')

    elif decisao == 'não':

        print('\nCadastro cancelado.')
    
    else:

        print('\nResposta inválida. Digite "sim" ou "não".')