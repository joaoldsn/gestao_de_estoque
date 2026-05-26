from funcoes.conexao import conexao, cursor

def cadastrar_produto():

    nome = input('\nDigite o nome do produto:\nVocê:')
    categoria = input('Digite a categoria:\nVocê: ')
    quantidade = int(input('Digite a quantidade:\nVocê: '))
    preco = float(input('Digite o preço:\nVocê: '))

    print('\n===== CONFIRMAÇÃO =====')
    print(f'Nome: {nome}')
    print(f'Categoria: {categoria}')
    print(f'Quantidade: {quantidade}')
    print(f'Preço Unitário: R$ {preco:.2f}')   

    decisao = input('\nConfirmar cadastro? (sim/não):\nVocê: ')

    if decisao == 'sim':

        cursor.execute("""
        INSERT INTO produtos (nome, categoria, preco, quantidade)
        VALUES (?, ?, ?, ?)
        """, (nome, categoria, preco, quantidade))

        conexao.commit()

        produto_id = cursor.lastrowid

        print('\nProduto cadastrado com sucesso!')
        print(f'ID do produto: {produto_id}')

    else:

        print('\nCadastro cancelado.')