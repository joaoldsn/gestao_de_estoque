from funcoes.conexao import conexao, cursor
def registrar_saida():

    nome = input('\nDigite o nome do produto: ')
    quantidade = int(input('Digite a quantidade de saída: '))

    cursor.execute("""
    SELECT quantidade FROM produtos
    WHERE nome = ?
    """, (nome,))

    produto = cursor.fetchone()

    if produto == None:

        print('\n Produto não encontrado.')
        return

    estoque_atual = produto[0]

    if quantidade > estoque_atual:

        print('\n Estoque insuficiente.')
        return

    nova_quantidade = estoque_atual - quantidade

    cursor.execute("""
    UPDATE produtos
    SET quantidade = ?
    WHERE nome = ?
    """, (nova_quantidade, nome))

    conexao.commit()

    print('\n Saída registrada com sucesso!')