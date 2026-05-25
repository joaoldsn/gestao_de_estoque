def cadastrar_produto(nome, categoria, preco, quantidade):
    while True:

      nome = input('Digite o nome do produto: ')
      quantidade=int(input('Digite a quantidade do produto: '))
      preco=float(input('Digite o preço do produto: '))
      produto = {
          'nome': nome,
          'categoria': categoria,
          'quantidade': quantidade,
          'preço': preco,
      }

      decisao=input('Confirmar cadastro? (sim/não)')
      if decisao == 'sim':
          estoque.append(produto)
          print('Produto cadastrado com sucesso!')
          break

      elif decisao == 'não':

          print('Cadastro cancelado. Digite os dados para um novo produto.')

      else:
          print('Resposta inválida. Por favor, digite "sim" ou "não".')

