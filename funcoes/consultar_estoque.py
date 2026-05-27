from funcoes.conexao import cursor

def consultar_estoque():

    # Solicita ao usuário o nome do produto que deseja consultar
    nome = input('\nDigite o nome do produto: ')

    # Busca no banco de dados as informações do produto informado
    cursor.execute("""
    SELECT * FROM produtos
    WHERE nome = ?
    """, (nome,))

    # Obtém o resultado da consulta
    produto = cursor.fetchone()

    # Verifica se o produto foi encontrado
    if produto is None:

        print('\nProduto não encontrado.')
        return

    # Exibe os dados do produto encontrado
    print('\n===== DADOS DO PRODUTO =====')
    print(f'ID: {produto[0]}')
    print(f'Nome: {produto[1]}')
    print(f'Categoria: {produto[2]}')
    print(f'Preço Unitário: R$ {produto[3]:.2f}')
    print(f'Quantidade: {produto[4]} un')