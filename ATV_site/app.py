from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def conectar_banco():
    conn = sqlite3.connect('banco.db') 
    return conn
    
def criar_tabela_usuarios():
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS contatos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        senha TEXT NOT NULL
    )
    ''')
    conn.commit()
    
    cursor.execute('INSERT INTO usuarios (nome, senha) VALUES(?, ?)', ('admin', 1234))
    conn.commit()
    conn.close

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        nome = request.form['nome']
        senha = request.form['senha']
        
        conn = conectar_banco()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM usuarios WHERE nome = ? AND senha = ?', (nome, senha))
        usuarios = cursor.fetchone()
        conn.close()