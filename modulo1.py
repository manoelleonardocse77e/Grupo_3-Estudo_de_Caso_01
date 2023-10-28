import csv

class Estoque:
    def __init__(self, nome_produto, quantidade_inicial, limite_minimo):
        self.nome_produto = nome_produto
        self.quantidade = quantidade_inicial
        self.limite_minimo = limite_minimo

    def receber_produto(self, quantidade):
        self.quantidade += quantidade
        self.atualizar_csv()
        print(f"Recebido {quantidade} de {self.nome_produto}. Estoque atual: {self.quantidade}")

    def vender_produto(self, quantidade):
        if self.quantidade >= quantidade:
            self.quantidade -= quantidade
            self.atualizar_csv()
            print(f"Vendido {quantidade} de {self.nome_produto}. Estoque atual: {self.quantidade}")
        else:
            print(f"Estoque insuficiente para vender {quantidade} de {self.nome_produto}.")

    def verificar_estoque(self):
        if self.quantidade <= self.limite_minimo:
            print(f"ALERTA: Estoque de {self.nome_produto} está abaixo do limite mínimo de {self.limite_minimo}!")

    def atualizar_csv(self):
        data = []

        with open('estoque.csv', 'r', newline='') as file:
            reader = csv.reader(file)
            for linha in reader:
                if linha and linha[0] == self.nome_produto and len(linha) >= 2:
                    linha[1] = str(self.quantidade)
                data.append(linha)

        with open('estoque.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            for linha in data:
                writer.writerow(linha)
