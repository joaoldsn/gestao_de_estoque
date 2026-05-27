from funcoes.conexao import cursor

def alertar_estoque_baixo():

    # Pede ao usuário o valor mínimo de estoque
    limite = int(input('\nDigite o limite mínimo: '))

    # Consulta os produtos que possuem quantidade menor que o limite informado
    cursor.execute("""
    SELECT * FROM produtos
    WHERE quantidade < ?
    """, (limite,))

    # Guarda os resultados da consulta
    produtos = cursor.fetchall()

    # Verifica se foi encontrado algum produto com estoque baixo
    if produtos == []:

        print('\nNenhum produto com estoque baixo.')
        return

    print('\nPRODUTOS COM ESTOQUE BAIXO:')

    # Exibe os produtos encontrados
    for produto in produtos:

        print('\n-------------------')
        print(f'ID: {produto[0]}')
        print(f'Nome: {produto[1]}')
        print(f'Quantidade: {produto[4]} un')