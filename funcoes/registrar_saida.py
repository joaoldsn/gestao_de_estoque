from funcoes.conexao import conexao, cursor

def registrar_saida():

    # Solicita ao usuário o nome do produto e a quantidade que será retirada
    nome = input('\nDigite o nome do produto: ')
    quantidade = int(input('Digite a quantidade de saída: '))

    # Busca no banco de dados a quantidade atual do produto informado
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

    # Armazena a quantidade atual em estoque
    estoque_atual = produto[0]

    # Impede que sejam retiradas mais unidades do que existem no estoque
    if quantidade > estoque_atual:
        print('\n Estoque insuficiente.')
        return

    # Calcula a nova quantidade após a saída do produto
    nova_quantidade = estoque_atual - quantidade

    # Atualiza a quantidade do produto no banco de dados
    cursor.execute("""
    UPDATE produtos
    SET quantidade = ?
    WHERE nome = ?
    """, (nova_quantidade, nome))

    # Salva as alterações feitas no banco
    conexao.commit()
    
    print('\n Saída registrada com sucesso!')