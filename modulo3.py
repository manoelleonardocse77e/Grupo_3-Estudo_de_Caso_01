class Mercearia:
    def __init__(self):
        self.inventario = {}
        self.vendas = {}

    def adicionar_produto(self, nome, tipo, quantidade, preco, descricao=''):
        if nome in self.inventario:
            print(f"O produto {nome} já existe no inventário.")
        else:
            self.inventario[nome] = {'tipo': tipo, 'quantidade': quantidade, 'preco': preco, 'descricao': descricao}

    def vender_produto(self, nome, quantidade):
        if nome in self.inventario:
            if self.inventario[nome]['quantidade'] >= quantidade:
                self.inventario[nome]['quantidade'] -= quantidade
                if nome in self.vendas:
                    self.vendas[nome] += quantidade
                else:
                    self.vendas[nome] = quantidade
            else:
                print(f"Quantidade insuficiente de {nome} em estoque.")
        else:
            print(f"O produto {nome} não existe no inventário.")

    def alerta_reposicao(self, limite_minimo=10):
        for produto, detalhes in self.inventario.items():
            if detalhes['quantidade'] < limite_minimo:
                print(f"Alerta: {produto} precisa ser reabastecido.")

    def analise_desempenho(self, nome_produto):
        if nome_produto in self.vendas:
            return f"O produto {nome_produto} teve {self.vendas[nome_produto]} unidades vendidas."
        else:
            return f"O produto {nome_produto} não teve unidades vendidas."
