📘 PROJETO – GESTÃO DE ESTOQUE
Valor: 2,0 pontos
🎯 Objetivo
Desenvolver um sistema de gestão de estoque em linguagem Python, aplicando conceitos de programação estruturada, manipulação de dados e organização lógica de funções.

O sistema deverá permitir o controle de produtos, incluindo cadastro, atualização e consulta de informações de estoque.



🧠 Contextualização
Sistemas de controle de estoque são fundamentais para a gestão eficiente de empresas comerciais e industriais, permitindo o monitoramento de entradas e saídas de produtos, evitando perdas e auxiliando na tomada de decisão.

Neste projeto, o aluno deverá implementar um sistema simplificado, simulando uma aplicação real de controle de estoque.



⚙️ Requisitos do Sistema
O programa deverá implementar as seguintes funcionalidades obrigatórias:

🔹 Cadastro de produtos
Permitir inserir novos produtos com:

Nome
Categoria
Preço
Quantidade inicial
🔹 Atualização de estoque
O sistema deverá permitir:

Registrar entrada de produtos (aumentar estoque)
Registrar saída de produtos (reduzir estoque)
🔹 Consulta de estoque
Permitir consultar:

Dados do produto
Quantidade disponível
🔹 Alerta de estoque baixo
O sistema deverá identificar produtos com quantidade abaixo de um limite definido pelo usuário.



💻 Estrutura obrigatória do código
O programa deve conter, obrigatoriamente, as seguintes funções:

 
def cadastrar_produto(nome, categoria, preco, quantidade):
    """Registra novo produto no sistema"""
 
def registrar_entrada(produto_id, quantidade):
    """Adiciona itens ao estoque"""
 
def registrar_saida(produto_id, quantidade):
    """Remove itens do estoque"""
 
def consultar_estoque(produto_id):
    """Verifica saldo atual do produto"""
 
def alertar_estoque_baixo(limite):
    """Identifica produtos com estoque crítico"""
 
 
📌 Requisitos técnicos
Utilizar listas ou dicionários para armazenar os dados
O sistema deve ter menu interativo
O código deve ser organizado e legível
Deve conter tratamento básico de erros (ex: produto inexistente, estoque insuficiente)
📊 Critérios de Avaliação
Critério

Pontuação

Implementação das funções

0,6

Lógica e funcionamento do sistema

0,6

Organização e clareza do código

0,4

Interface (menu e interação)

0,2

Total

2,0 pontos



🚀 Diferencial (bônus até +0,5)
Interface mais elaborada
Uso de arquivos (salvar dados)
Relatórios de estoque
Organização por módulos
📅 Entrega
Arquivo .py
Nome do arquivo: gestao_estoque_nome_aluno.py
Entrega via Blackboard, através do link git hub


⚠️ Observações adicionais (Uso de Git)
Para este projeto, recomenda-se a utilização de controle de versão com Git, como prática profissional de desenvolvimento de software.

📌 Requisitos mínimos:
O projeto deve ser armazenado em um repositório (GitHub, GitLab ou similar)
Deve conter um arquivo README.md com:
Descrição do projeto
Objetivo do sistema
Funcionalidades implementadas
Instruções de execução do código
Nome do aluno
📌 Boas práticas de commits:
Realizar commits frequentes, refletindo a evolução do desenvolvimento
Utilizar mensagens claras e objetivas, por exemplo:DO PROJETO
feat: adiciona função de cadastro de produto
fix: corrige erro na saída de estoque
refactor: melhora organização do código
📌 Critério de avaliação adicional (opcional pelo professor):
Organização do repositório
Clareza do README
Histórico de commits coerente
⚠️ Importante:
Evitar subir apenas um único commit final
O histórico de commits será considerado como evidência de desenvolvimento próprio
Projetos sem README ou sem organização poderão ter desconto na nota
TODOS OS ALUNOS DEVERÃO APRESENTAR LINK DO GIT HUB 