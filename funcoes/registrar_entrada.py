from funcoes.conexao import conexao, cursor

def registrar_entrada():

    nome = input('\nDigite o nome do produto: ')
    quantidade = int(input('Digite a quantidade de entrada: '))

    cursor.execute("""
    SELECT quantidade FROM produtos
    WHERE nome = ?
    """, (nome,))

    produto = cursor.fetchone()

    if produto == None:

        print('\n Produto não encontrado.')
        return

    nova_quantidade = produto[0] + quantidade

    cursor.execute("""
    UPDATE produtos
    SET quantidade = ?
    WHERE nome = ?
    """, (nova_quantidade, nome))

    conexao.commit()

    print('\n Entrada registrada com sucesso!')
from funcoes.conexao import conexao, cursor