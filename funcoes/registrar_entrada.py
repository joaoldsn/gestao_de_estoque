from funcoes.conexao import conexao, cursor

def registrar_entrada():

    # Solicita ao usuário o nome do produto e a quantidade que será adicionada
    nome = input('\nDigite o nome do produto: ')
    quantidade = int(input('Digite a quantidade de entrada: '))

    # Busca a quantidade atual do produto no banco de dados
    cursor.execute("""
    SELECT quantidade FROM produtos
    WHERE nome = ?
    """, (nome,))

    # Obtém o resultado da consulta
    produto = cursor.fetchone()

    # Verifica se o produto existe no banco
    if produto == None:

        print('\n Produto não encontrado.')
        return

    # Soma a quantidade informada à quantidade atual em estoque
    nova_quantidade = produto[0] + quantidade

    # Atualiza a quantidade do produto no banco de dados
    cursor.execute("""
    UPDATE produtos
    SET quantidade = ?
    WHERE nome = ?
    """, (nova_quantidade, nome))

    # Salva as alterações realizadas
    conexao.commit()

    print('\n Entrada registrada com sucesso!')