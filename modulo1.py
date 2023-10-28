import csv

class Estoque:
    def __init__(self, gasolina, alcool, diesel, energia_solar, limite_minimo=100):
        self.gasolina = gasolina
        self.alcool = alcool
        self.diesel = diesel
        self.energia_solar = energia_solar
        self.limite_minimo = limite_minimo
        self.filename = 'estoque_pecas.csv'

    def receber_produto(self, tipo, quantidade):
        if tipo == 'gasolina':
            self.gasolina += quantidade
        elif tipo == 'alcool':
            self.alcool += quantidade
        elif tipo == 'diesel':
            self.diesel += quantidade
        elif tipo == 'energia_solar':
            self.energia_solar += quantidade
        else:
            print("Tipo de produto inválido.")

        self.atualizar_arquivo()

    def vender_produto(self, tipo, quantidade):
        if tipo == 'gasolina':
            if self.gasolina >= quantidade:
                self.gasolina -= quantidade
            else:
                print("Quantidade de gasolina insuficiente.")
        elif tipo == 'alcool':
            if self.alcool >= quantidade:
                self.alcool -= quantidade
            else:
                print("Quantidade de álcool insuficiente.")
        elif tipo == 'diesel':
            if self.diesel >= quantidade:
                self.diesel -= quantidade
            else:
                print("Quantidade de diesel insuficiente.")
        elif tipo == 'energia_solar':
            if self.energia_solar >= quantidade:
                self.energia_solar -= quantidade
            else:
                print("Quantidade de energia solar insuficiente.")
        else:
            print("Tipo de produto inválido.")

        self.atualizar_arquivo()

    def verificar_alerta(self):
        if self.gasolina < self.limite_minimo:
            print(f"Alerta: Nível de gasolina abaixo do limite mínimo.")
        if self.alcool < self.limite_minimo:
            print(f"Alerta: Nível de álcool abaixo do limite mínimo.")
        if self.diesel < self.limite_minimo:
            print(f"Alerta: Nível de diesel abaixo do limite mínimo.")
        if self.energia_solar < self.limite_minimo:
            print(f"Alerta: Nível de energia solar abaixo do limite mínimo.")

    def atualizar_arquivo(self):
        with open(self.filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Produto', 'Quantidade'])
            writer.writerow(['Gasolina', self.gasolina])
            writer.writerow(['Álcool', self.alcool])
            writer.writerow(['Diesel', self.diesel])
            writer.writerow(['Energia Solar', self.energia_solar])
