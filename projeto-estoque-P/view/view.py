import tkinter as tk
from tkinter import ttk

class EstoqueView:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerenciamento de Estoque")

        self.frame = ttk.Frame(root, padding="10")
        self.frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Campos de entrada
        self.nome_var = tk.StringVar()
        self.quantidade_var = tk.IntVar()
        self.preco_var = tk.DoubleVar()

        ttk.Label(self.frame, text="Nome:").grid(row=0, column=0, sticky=tk.W)
        ttk.Entry(self.frame, textvariable=self.nome_var).grid(row=0, column=1)

        ttk.Label(self.frame, text="Quantidade:").grid(row=1, column=0, sticky=tk.W)
        ttk.Entry(self.frame, textvariable=self.quantidade_var).grid(row=1, column=1)

        ttk.Label(self.frame, text="Preço:").grid(row=2, column=0, sticky=tk.W)
        ttk.Entry(self.frame, textvariable=self.preco_var).grid(row=2, column=1)

        # Botões
        self.adicionar_btn = ttk.Button(self.frame, text="Adicionar")
        self.adicionar_btn.grid(row=3, column=0, pady=5)

        self.atualizar_btn = ttk.Button(self.frame, text="Atualizar")
        self.atualizar_btn.grid(row=3, column=1, pady=5)

        self.deletar_btn = ttk.Button(self.frame, text="Deletar")
        self.deletar_btn.grid(row=3, column=2, pady=5)

        # Lista de produtos
        self.tree = ttk.Treeview(self.frame, columns=("ID", "Nome", "Quantidade", "Preço"), show='headings')
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nome", text="Nome")
        self.tree.heading("Quantidade", text="Quantidade")
        self.tree.heading("Preço", text="Preço")
        self.tree.grid(row=4, column=0, columnspan=3, pady=10)

    def get_inputs(self):
        return self.nome_var.get(), self.quantidade_var.get(), self.preco_var.get()

    def set_inputs(self, nome, quantidade, preco):
        self.nome_var.set(nome)
        self.quantidade_var.set(quantidade)
        self.preco_var.set(preco)

    def clear_inputs(self):
        self.nome_var.set("")
        self.quantidade_var.set(0)
        self.preco_var.set(0.0)

    def insert_product(self, produto):
        self.tree.insert('', 'end', values=produto)

    def update_product(self, produto_id, produto):
        selected_item = self.tree.selection()[0]
        self.tree.item(selected_item, values=(produto_id, *produto))

    def delete_selected_product(self):
        selected_item = self.tree.selection()[0]
        self.tree.delete(selected_item)

    def get_selected_product(self):
        selected_item = self.tree.selection()
        if selected_item:
            return self.tree.item(selected_item[0], 'values')  # Retorna os valores da linha selecionada
        return None