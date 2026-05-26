from funcoes.conexao import cursor

def relatorio():

    cursor.execute("""
    SELECT * FROM produtos
    """)

    produtos = cursor.fetchall()

    if produtos == []:

        print('\n Nenhum produto cadastrado.')
        return

    print('\n===== RELATÓRIO =====')

    for produto in produtos:

        print('\n-------------------')
        print(f'ID: {produto[0]}')
        print(f'Nome: {produto[1]}')
        print(f'Categoria: {produto[2]}')
        print(f'Preço: R$ {produto[3]:.2f}')
        print(f'Quantidade: {produto[4]}')