from funcoes.cadastrar_produto import cadastrar_produto
from funcoes.registrar_entrada import registrar_entrada
from funcoes.registrar_saida import registrar_saida
from funcoes.consultar_estoque import consultar_estoque
from funcoes.alerta import alertar_estoque_baixo
from funcoes.relatorio import relatorio

def menu():

    # Mantém o menu em execução até que o usuário escolha sair
    while True:
        print("""
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃          SISTEMA DE GESTÃO DE ESTOQUE            ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

                MENU PRINCIPAL

    1 - Cadastrar produto
    2 - Registrar entrada
    3 - Registrar saída
    4 - Consultar estoque
    5 - Alerta de estoque baixo
    6 - Relatório
    0 - Sair
    """)

        # Solicita ao usuário a opção desejada
        opcao = input('\nEscolha uma opção: ')

        # Chama a função responsável por cadastrar um novo produto
        if opcao == '1':
            cadastrar_produto()

        # Chama a função para registrar entrada de produtos no estoque
        elif opcao == '2':
            registrar_entrada()

        # Chama a função para registrar saída de produtos do estoque
        elif opcao == '3':
            registrar_saida()

        # Exibe as informações do estoque
        elif opcao == '4':
            consultar_estoque()

        # Mostra os produtos com estoque abaixo do limite definido
        elif opcao == '5':
            alertar_estoque_baixo()

        # Gera um relatório com todos os produtos cadastrados
        elif opcao == '6':
            relatorio()

        # Encerra o sistema
        elif opcao == '0':
            print('\n Sistema encerrando...')
            break

        # Executado caso o usuário digite uma opção inexistente
        else:
            print('\n Opção inválida.')
    