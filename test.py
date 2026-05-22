from gestao_de_estoque.funcoes.menu import exibir_menu

while True:

    exibir_menu()

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("Cadastrar produto")

    elif opcao == "0":
        print("Sistema encerrado.")
        break