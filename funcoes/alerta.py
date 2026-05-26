from funcoes.conexao import cursor

def alertar_estoque_baixo():

    limite = int(input('\nDigite o limite mínimo: '))

    cursor.execute("""
    SELECT * FROM produtos
    WHERE quantidade < ?
    """, (limite,))

    produtos = cursor.fetchall()

    if produtos == []:

        print('\nNenhum produto com estoque baixo.')
        return

    print('\nPRODUTOS COM ESTOQUE BAIXO:')

    for produto in produtos:

        print('\n-------------------')
        print(f'ID: {produto[0]}')
        print(f'Nome: {produto[1]}')
        print(f'Quantidade: {produto[4]}')