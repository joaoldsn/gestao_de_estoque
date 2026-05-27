from funcoes.conexao import cursor

def relatorio():

    # Busca todos os produtos cadastrados no banco de dados
    cursor.execute("""
    SELECT * FROM produtos
    """)

    # Armazena todos os registros encontrados em uma lista
    produtos = cursor.fetchall()

    # Verifica se existe algum produto cadastrado
    if produtos == []:

        print('\n Nenhum produto cadastrado.')
        return

    print('\n===== RELATÓRIO =====')

    # Percorre a lista de produtos para exibir as informações
    for produto in produtos:

        print('\n-------------------')
        print(f'ID: {produto[0]}')
        print(f'Nome: {produto[1]}')
        print(f'Categoria: {produto[2]}')
        print(f'Preço Unitário: R$ {produto[3]:.2f}')
        print(f'Quantidade: {produto[4]} un')

        # Calcula o valor total do estoque daquele produto
        print(f'Valor Total: R$ {produto[3] * produto[4]:.2f}')