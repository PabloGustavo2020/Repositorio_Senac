from model.model import EstoqueModel
from view.view import EstoqueView

class EstoqueController:
    def __init__(self, root):
        self.model = EstoqueModel()
        self.view = EstoqueView(root)

        # Conecta os botões da view aos métodos do controller
        self.view.adicionar_btn.config(command=self.adicionar_produto)
        self.view.atualizar_btn.config(command=self.atualizar_produto)
        self.view.deletar_btn.config(command=self.deletar_produto)

        self.atualizar_lista_produtos()

    def adicionar_produto(self):
        nome, quantidade, preco = self.view.get_inputs()
        if nome and quantidade and preco:
            self.model.adicionar_produto(nome, quantidade, preco)
            self.view.clear_inputs()
            self.atualizar_lista_produtos()

    def atualizar_produto(self):
        try:
            selected = self.view.get_selected_product()
            if selected is not None:
                produto_id = int(selected[0])  # Pega o ID do produto selecionado
                nome, quantidade, preco = self.view.get_inputs()  # Pega os novos valores dos campos

                # Valida se os campos não estão vazios e se os valores são coerentes
                if nome and quantidade > 0 and preco > 0:
                    # Atualiza o produto no banco de dados
                    self.model.atualizar_produto(produto_id, nome, quantidade, preco)

                    # Limpa os campos e atualiza a lista na interface
                    self.view.clear_inputs()
                    self.atualizar_lista_produtos()
                else:
                    print("Todos os campos devem ser preenchidos com valores válidos.")
            else:
                print("Nenhum produto selecionado para atualizar.")
        except ValueError as e:
            print(f"Erro ao atualizar o produto: {e}")
        except IndexError:
            print("Erro ao tentar atualizar: Nenhum item foi selecionado corretamente.")

    def deletar_produto(self):
        try:
            produto_id, _, _, _ = self.view.get_selected_product()
            self.model.deletar_produto(produto_id)
            self.view.delete_selected_product()
        except IndexError:
            pass  # Nenhum item selecionado

    def atualizar_lista_produtos(self):
        for produto in self.view.tree.get_children():
            self.view.tree.delete(produto)
        for produto in self.model.listar_produtos():
            self.view.insert_product(produto)
