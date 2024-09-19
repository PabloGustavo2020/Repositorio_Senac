import sqlite3

class EstoqueModel:
    def __init__(self):
        self.conn = sqlite3.connect('estoque.db')
        self.criar_tabela()

    def criar_tabela(self):
        query = '''
        CREATE TABLE IF NOT EXISTS produtos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            quantidade INTEGER NOT NULL,
            preco REAL NOT NULL
        )
        '''
        self.conn.execute(query)
        self.conn.commit()

    def adicionar_produto(self, nome, quantidade, preco):
        query = 'INSERT INTO produtos (nome, quantidade, preco) VALUES (?, ?, ?)'
        self.conn.execute(query, (nome, quantidade, preco))
        self.conn.commit()

    def atualizar_produto(self, produto_id, nome, quantidade, preco):
        query = 'UPDATE produtos SET nome = ?, quantidade = ?, preco = ? WHERE id = ?'
        self.conn.execute(query, (nome, quantidade, preco, produto_id))
        self.conn.commit()

    def deletar_produto(self, produto_id):
        query = 'DELETE FROM produtos WHERE id = ?'
        self.conn.execute(query, (produto_id))
        self.conn.commit()
    
    def listar_produtos(self):
        query = 'SELECT * FROM produtos'
        cursor = self.conn.execute(query)
        return cursor.fetchall()
    
    def fechar_conexao(self):
        self.conn.close()