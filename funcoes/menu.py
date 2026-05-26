from funcoes.cadastrar_produto import cadastrar_produto
from funcoes.registrar_entrada import registrar_entrada
from funcoes.registrar_saida import registrar_saida
from funcoes.consultar_estoque import consultar_estoque
from funcoes.alerta import alertar_estoque_baixo
from funcoes.relatorio import relatorio

def menu():

    while True:
    print("""
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃          SISTEMA DE GESTÃO DE ESTOQUE            
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
        opcao = input('\nEscolha uma opção: ')

        if opcao == '1':

            cadastrar_produto()

        elif opcao == '2':

            registrar_entrada()

        elif opcao == '3':

            registrar_saida()

        elif opcao == '4':

            consultar_estoque()

        elif opcao == '5':

            alertar_estoque_baixo()

        elif opcao == '6':

            relatorio()

        elif opcao == '0':

            print('\n Sistema encerrando...')
            break

        else:

            print('\n Opção inválida.')
    