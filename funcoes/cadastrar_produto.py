from funcoes.conexao import conexao, cursor
def cadastrar_produto(nome, categoria, preco, quantidade):
    while True:

      nome = input('Digite o nome do produto:\nVocê: ')
      categoria = input('Digite a categoria do produto:\nVocê:  ')
      quantidade=int(input('Digite a quantidade do produto:\nVocê:  '))
      preco=float(input('Digite o preço do produto:\nVocê:  '))
      produto = {
          'nome': nome,
          'categoria': categoria,
          'quantidade': quantidade,
          'preço': preco,
      }

      decisao=input('Confirmar cadastro? (sim/não)\nVocê: ')
      if decisao == 'sim':
          estoque.append(produto)
          print('Produto cadastrado com sucesso!')
          break

      elif decisao == 'não':

          print('Cadastro cancelado. Digite os dados para um novo produto.')

      else:
          print('Resposta inválida. Por favor, digite "sim" ou "não".')

    cursor.execute("""
        INSERT INTO produtos (nome, categoria, preco, quantidade)
        VALUES (?, ?, ?, ?)
        """, (nome, categoria, preco, quantidade))

        conexao.commit()

        produto_id = cursor.lastrowid

        print('\nProduto cadastrado com sucesso!')
        print(f'ID do produto: {produto_id}')

    else:

        print('\nCadastro cancelado.')

