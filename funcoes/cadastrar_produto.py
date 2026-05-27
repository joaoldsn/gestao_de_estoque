from funcoes.conexao import conexao, cursor

def cadastrar_produto():

    # Solicita ao usuário os dados do produto
    nome = input('\nDigite o nome do produto: ')
    categoria = input('Digite a categoria: ')
    quantidade = int(input('Digite a quantidade: '))
    preco = float(input('Digite o preço: R$'))

    # Exibe um resumo dos dados informados para confirmação
    print('\n===== CONFIRMAÇÃO =====')
    print(f'Nome: {nome}')
    print(f'Categoria: {categoria}')
    print(f'Quantidade: {quantidade} un')
    print(f'Preço Unitário: R$ {preco:.2f}')

    # Solicita a confirmação do cadastro
    decisao = input('\nConfirmar cadastro? (sim/não):\n')

    # Realiza o cadastro caso o usuário confirme
    if decisao == 'sim':

        cursor.execute("""
        INSERT INTO produtos (nome, categoria, preco, quantidade)
        VALUES (?, ?, ?, ?)
        """, (nome, categoria, preco, quantidade))

        # Salva as alterações no banco de dados
        conexao.commit()

        # Obtém o ID gerado automaticamente para o produto
        produto_id = cursor.lastrowid

        print('\nProduto cadastrado com sucesso!')
        print(f'ID do produto: {produto_id}')

    # Cancela a operação caso o usuário não confirme
    elif decisao.lower() in ['não', 'nao']:

        print('\nCadastro cancelado.')

    # Executado caso a resposta seja diferente de "sim" ou "não"
    else:

        print('\nResposta inválida. Digite "sim" ou "não".')