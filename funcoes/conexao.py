import sqlite3
import os

caminho_banco = os.path.join(
    os.path.dirname(__file__),
    "..",
    "estoque.db"
)

conexao = sqlite3.connect(caminho_banco)
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