from funcoes.conexao import cursor

def consultar_estoque():

    nome = input('\nDigite o nome do produto: ')

    cursor.execute("""
    SELECT * FROM produtos
    WHERE nome = ?
    """, (nome,))

    produto = cursor.fetchone()

    if produto == None:

        print('\nProduto não encontrado.')
        return

    print('\n===== DADOS DO PRODUTO =====')
    print(f'ID: {produto[0]}')
    print(f'Nome: {produto[1]}')
    print(f'Categoria: {produto[2]}')
    print(f'Preço: R$ {produto[3]:.2f}')
    print(f'Quantidade: {produto[4]}')