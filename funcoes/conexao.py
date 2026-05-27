import sqlite3

conexao = sqlite3.connect("estoque.db")
cursor = conexao.cursor()

def criar_tabela():

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS produtos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        categoria TEXT NOT NULL,
        preco REAL NOT NULL,
        quantidade INTEGER NOT NULL
)
""")

conexao.commit()

criar_tabela()