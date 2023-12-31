import csv
import pandas as panda
import matplotlib.pyplot as grafico
from datetime import datetime

def Modulo1():
    class Estoque:
        def __init__(self, nome_produto, quantidade_inicial, limite_minimo):
            # (O(1))
            self.nome_produto = nome_produto
            self.quantidade = quantidade_inicial
            self.limite_minimo = limite_minimo
            self.vendas = []

        def receber_produto(self, quantidade):
            # (0(1))
            self.quantidade += int(quantidade)
            self.atualizar_csv()
            print(f"Recebido {quantidade} de {self.nome_produto}. Estoque atual: {self.quantidade}")

        def vender_produto(self, quantidade):
            # (0(1))
            if self.quantidade >= int(quantidade):
                self.quantidade -= int(quantidade)
                venda_info = {'data': datetime.now().strftime('%Y-%m-%d'), 'quantidade': int(quantidade)}
                self.vendas.append(vendas_info)
                self.atualizar_csv()
                print(f"Vendido {quantidade} de {self.nome_produto}. Estoque atual: {self.quantidade}")
            else:
                print(f"Estoque insuficiente para vender {quantidade} de {self.nome_produto}.")

        def verificar_estoque(self):
          # (O(1))
            if self.quantidade <= self.limite_minimo:
                print(f"ALERTA: Estoque de {self.nome_produto} está abaixo do limite mínimo de {self.limite_minimo}!")

        def atualizar_csv(self):
          # (O(M))
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

    def registrar_vendas_csv(self):
      # (o(k))
        try:
            with open('vendas.csv', 'r', newline=''):
                pass
        except FileNotFoundError:
            with open('vendas.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Produto', 'Data', 'Quantidade']) 

        with open('vendas.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            for venda in self.vendas:
                writer.writerow([self.nome_produto, venda['data'], venda['quantidade']])

    # definir nome, quantidade e limite de aviso
    gasolina = Estoque("Gasolina", 0, 40)
    alcool = Estoque("Álcool", 0, 40)
    diesel = Estoque("Diesel", 0, 40)
    energia_solar = Estoque("Energia Solar", 0, 40)

    while True:
        print("=-=" * 10)
        escolha = int(input('''[ 1 ] Vender Produto
[ 2 ] Receber Produto
[ 3 ] Verificar Estoque
[ 4 ] Sair
-> '''))

        if escolha == 1:
            print("=-=" * 10)
            escolhido = int(input('''Produto a ser vendido: 
[ 1 ] Gasolina
[ 2 ] Álcool 
[ 3 ] Diesel
[ 4 ] Energia Solar
[ 5 ] Sair
-> '''))
            if escolhido == 1:
                valor = int(input("Valor: "))
                gasolina.vender_produto(valor)
                gasolina.verificar_estoque()
            elif escolhido == 2:
                valor = int(input("Valor: "))
                alcool.vender_produto(valor)
                alcool.verificar_estoque()
            elif escolhido == 3:
                valor = int(input("Valor: "))
                diesel.vender_produto(valor)
                diesel.verificar_estoque()
            elif escolhido == 4:
                valor = int(input("Valor: "))
                energia_solar.vender_produto(valor)
                energia_solar.verificar_estoque()
            elif escolhido == 5:
                continue

        if escolha == 2:
            print("=-=" * 10)
            escolhido = int(input('''Produto a ser recebido: 
[ 1 ] Gasolina
[ 2 ] Álcool 
[ 3 ] Diesel
[ 4 ] Energia Solar
[ 5 ] Sair
-> '''))
            if escolhido == 1:
                valor = int(input("Quantidade: "))
                gasolina.receber_produto(valor)
            elif escolhido == 2:
                valor = int(input("Quantidade: "))
                alcool.receber_produto(valor)
            elif escolhido == 3:
                valor = int(input("Quantidade: "))
                diesel.receber_produto(valor)
            elif escolhido == 4:
                valor = int(input("Quantidade "))
                energia_solar.receber_produto(valor)
              
        if escolha == 3:
          contg = 0
          conta = 0
          contd = 0
          conte = 0
          ordem = [gasolina.quantidade, alcool.quantidade, diesel.quantidade, energia_solar.quantidade]
          ordem.sort(reverse=True)
          print("=-=" * 10)
          print("Estoque de Produtos")
          print("=-=" * 10)
          for c in range(len(ordem)):
              if ordem[c] == 0:
                continue
              elif contg == 0:
                if ordem[c] == gasolina.quantidade:
                  print(f"{c + 1}. Gasolina: {gasolina.quantidade}")
                  contg += 1
              elif conta == 0:
                if ordem[c] == alcool.quantidade:
                  print(f"{c + 1}. Alcool: {alcool.quantidade}")
                  conta += 1
              elif contd == 0:
                if ordem[c] == diesel.quantidade:
                  print(f"{c + 1}. Diesel: {diesel.quantidade}")
                  contd += 1
              elif conte == 0:
                if ordem[c] == energia_solar.quantidade:
                  print(f"{c + 1}. Energia Solar: {energia_solar.quantidade}")
                  conte += 1
          gasolina.verificar_estoque()
          alcool.verificar_estoque()
          diesel.verificar_estoque()
          energia_solar.verificar_estoque()
        if escolha == 4:
            break

def Modulo2():
      
      def normalize_date(date):
          return datetime.strptime(date, '%Y-%m-%d').date()
      
      def ordenar_oleo():
          with open("ordem_oleo.csv", mode='r', newline='') as file:
              reader = csv.DictReader(file)
              linhas = [linha for linha in reader]
              linhas_ordenadas = sorted(linhas, key=lambda x: normalize_date(x['Data']), reverse=True)
      
          with open("ordem_oleo.csv", mode='w', newline='') as file:
              writer = csv.DictWriter(file, fieldnames=linhas_ordenadas[0].keys())
              writer.writeheader()
              for linha in linhas_ordenadas:
                  writer.writerow(linha)
      
      def criar_os_oleo(cliente, carro, placa, mecanico, oleo, conta_oleo, tempoT):
          cliente = input("Digite o nome do cliente: \n")
          carro = input("Digite as informações do carro:\n")
          placa = input("Placa do carro:\n")
          mecanico = input("Mecânico responsável:\n")
          oleo = input("Óleo usado:\n")
          conta_oleo = int(input("Litros de óleo usado:\n"))
          tempoT = input("Tempo gasto no serviço:\n(Minutos)\n")
          data = input("Data do serviço:\n(EX: 2023-11-21)\n")
          servico = "Troca de oleo"
          
          os_oleo = {
              "Cliente": cliente,
              "Carro": carro,
              "Placa": placa,
              "Mecânico": mecanico,
              "Óleo": oleo,
              "Litros de Óleo": conta_oleo,
              "Minutos": tempoT,
              "Data": data
          }
      
          registrar_oleo(os_oleo)
          ordenar_oleo()
      
      def registrar_oleo(os_oleo):
          with open("ordem_oleo.csv", mode="a", newline="") as file:
              writer = csv.DictWriter(file, fieldnames=os_oleo.keys())
      
              writer.writerow(os_oleo)
      
      def ordenar_balanceamento():
          with open("ordem_balanceamento.csv", mode='r', newline='') as file:
              reader = csv.DictReader(file)
              linhas = [linha for linha in reader]
              linhas_ordenadas = sorted(linhas, key=lambda x: normalize_date(x['Data']), reverse=True)
      
          with open("ordem_balanceamento.csv", mode='w', newline='') as file:
              writer = csv.DictWriter(file, fieldnames=linhas_ordenadas[0].keys())
              writer.writeheader()
              for linha in linhas_ordenadas:
                  writer.writerow(linha)
      
      def criar_os_balanceamento(cliente, carro, placa, mecanico, tempoB):
          cliente = input("Digite o nome do cliente: \n")
          carro = input("Digite as informações do carro:\n")
          placa = input("Placa do carro:\n")
          mecanico = input("Mecânico responsável:\n")
          tempoB = input("Tempo gasto no serviço:\n(minutos)\n")
          data = input("Data do serviço:\n(EX: 2023-11-21)\n")
          servico = "Balanceamento"
          
          os_balanceamento = {
              "Cliente": cliente,
              "Carro": carro,
              "Placa": placa,
              "Mecânico": mecanico,
              "Minutos": tempoB,
              "Data": data
          }
      
          registrar_balanceamento(os_balanceamento)
          ordenar_balanceamento()
      
      def registrar_balanceamento(os_balanceamento):
          with open("ordem_balanceamento.csv", mode="a", newline="") as file:
              writer = csv.DictWriter(file, fieldnames=os_balanceamento.keys())
      
              writer.writerow(os_balanceamento)
      
      def agenda(cliente, carro, placa, servico, data, mecanico):
          cliente = input("Digite o nome do cliente: \n")
          carro = input("Digite as informações do carro:\n")
          placa = input("Placa do carro:\n")
          data = input("Dia para o agendamento:\n(1-Segunda 2-Terça 3-Quarta 4-Quinta 5-Sexta)\n")
          mecanico = input("Mecânico responsável:\n")
          servico = int(input("Informe o serviço prestado:\n(1-Troca de óleo e 2-Balanceamento)\n"))
          
          if servico == 1:
              servico = "Troca de oleo"
          elif servico == 2:
              servico = "Balanceamento"
      
          semana = {
              "1": "Segunda",
              "2": "Terça",
              "3": "Quarta",
              "4": "Quinta",
              "5": "Sexta"
          }
      
          data = semana[data]
      
          agendamento = {
              "Cliente": cliente,
              "Carro": carro,
              "Placa": placa,
              "Data": data,
              "Mecânico": mecanico,
              "Serviço": servico
          }
      
          registro(agendamento)
      
      def registro(agendamento):
          with open("agenda.csv", mode="a", newline="") as file:
              writer = csv.DictWriter(file, fieldnames=agendamento.keys())
      
              writer.writerow(agendamento)
      
      menu = int(input("Digite qual operação deseja:\n(1- Agendamento 2- Ordem de Serviço 3-Consultar histórico 4- Apagar agenda)\n"))
      seg = 16
      ter = 16
      quar = 16
      quin = 16
      sex = 16
      cliente = ""
      carro = ""
      placa = ""
      servico = 0
      data = 0
      mecanico = ""
      oleo = ""
      conta_oleo = 0
      tempoT = 0
      tempoB = 0
      
      if menu == 1:
           agenda(cliente, carro, placa, servico, data, mecanico)
      elif menu == 2:
          serv = int(input("Informe o serviço:\n(1- Troca de óleo 2- Balanceamento)\n"))
          if serv == 1:
              criar_os_oleo(cliente, carro, placa, mecanico, oleo, conta_oleo, tempoT)
          elif serv == 2:
              criar_os_balanceamento(cliente, carro, placa, mecanico, tempoB)
      elif menu ==3:
          busca_placa = {}
          ordens_oleo = []
          ordens_balanceamento = []
          placa = input("Qual placa deseja procurar?\n")
          print("Cliente\t\tCarro\t\tPlaca\t\tMecânico\t\tÓleo\t\tLitros\t\tMinutos")
          with open("ordem_balanceamento.csv", mode="r", newline="") as file:
              reader = csv.DictReader(file)
              for linha in reader:
                  ordem = {}
                  for coluna in linha.keys():
                      ordem[coluna] = linha[coluna]
                  if placa == ordem["Placa"]:
                      ordens_balanceamento.append(ordem)
                      print(f"{linha['Cliente']}\t\t{linha['Carro']}\t\t{linha['Placa']}\t\t{linha['Mecanico']}\t\t\tX\t\tX\t\t{linha['Minutos']}")
      
          with open("ordem_oleo.csv", mode="r", newline="") as file:
              reader = csv.DictReader(file)
              for linha in reader:
                  ordem = {}
                  for coluna in linha.keys():
                      ordem[coluna] = linha[coluna]
                  if placa == ordem["Placa"]:
                      ordens_oleo.append(ordem)
              for linha in ordens_oleo:
                  print(f"{linha['Cliente']}\t\t{linha['Carro']}\t\t{linha['Placa']}\t\t{linha['Mecanico']}\t\t\t{linha['Oleo']}\t\t{linha['Litros']}\t\t{linha['Minutos']}")
      
      elif menu == 4:
          seg = 16
          ter = 16
          quar = 16
          quin = 16
          sex = 16
            
def Modulo3():
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

    mercearia = Mercearia()

    while True:
        print("\n1 - Adicionar produto ao inventário")
        print("2 - Vender produto")
        print("3 - Alerta de reposição")
        print("4 - Análise de desempenho")
        print("5 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Nome do produto: ")
            tipo = input("Tipo do produto: ")
            quantidade = int(input("Quantidade: "))
            preco = float(input("Preço: "))
            descricao = input("Descrição (opcional): ")
            mercearia.adicionar_produto(nome, tipo, quantidade, preco, descricao)

        elif opcao == '2':
            nome = input("Nome do produto: ")
            quantidade = int(input("Quantidade a ser vendida: "))
            mercearia.vender_produto(nome, quantidade)

        elif opcao == '3':
            mercearia.alerta_reposicao()

        elif opcao == '4':
            nome_produto = input("Nome do produto: ")
            print(mercearia.analise_desempenho(nome_produto))

        elif opcao == '5':
            break

        else:
            print("Opção inválida. Escolha uma opção válida.")


def Modulo5():
    def relatorio_vendas():
        dados = {'dias': ['2023-10-01', '2023-10-02', '2023-10-03', '2023-10-04'], 'vendas': [1000, 1200, 800, 1500]}
        dataframe = panda.DataFrame(dados)
        dataframe.to_csv('relatorio_vendas.csv', index=False)
        grafico.figure(figsize=(10, 5))
        grafico.plot(dataframe['dias'], dataframe['vendas'], color='green', linestyle='-', marker='o')
        grafico.title('Vendas Diárias')
        grafico.xlabel('Data')
        grafico.ylabel('Vendas')
        grafico.xticks(rotation=45)
        grafico.tight_layout()
        grafico.savefig('grafico_vendas.png')
        grafico.grid(True, linestyle='-', alpha=0.7)
        with open('relatorio.txt', 'w') as file:
            file.write("Relatório de Vendas\n")
            file.write(dataframe.to_string(index=False))
        print("Relatório de vendas gerado com sucesso em relatorio de vendas.png")

    def servicos_automotivos():
        servicos = [
            {'servico': 'troca de óleo', 'tempo': 25, 'satisfacao': 4.2},
            {'servico': 'Balanceamento', 'tempo': 47, 'satisfacao': 5.0},
            {'servico': 'troca de oleo', 'tempo': 90, 'satisfacao': 2.5},
        ]
        Tmedio = sum(t['tempo'] for t in servicos) / len(servicos)
        Smedia = sum(s['satisfacao'] for s in servicos) / len(servicos)
        with open('relatorio_desempenho_servicos.txt', 'w') as arq:
            arq.write("Relatório de Desempenho de Serviços\n")
            arq.write((50 * "-") + "\n")
            arq.write(f"Total de Serviços: {len(servicos)}\n")
            arq.write(f"Tempo Médio Gasto: {Tmedio} min\n")
            arq.write(f"Satisfação Média do Consumidor: {Smedia}\n")
            arq.write("Detalhes dos Serviços:\n")
            for servico in servicos:
                arq.write(f"Serviço: {servico['servico']}\n")
                arq.write(f"Tempo de Execução: {servico['tempo']} minutos\n")
                arq.write(f"Satisfação do Cliente: {servico['satisfacao']} de 5\n")
                arq.write(50 * "-")
        print("Relatório salvo em relatorio de desempenho de servicos.txt")

    def Relatorio_Energetico():
        import pandas as pd
import matplotlib.pyplot as grafico
import csv
import random
def relatorio_vendas():

    vendas_data = pd.read_csv('vendas.csv')

 
    vendas_data['data'] = pd.to_datetime(vendas_data['data'])


    plt.figure(figsize=(10, 5))
    plt.plot(vendas_data['data'], vendas_data['quantidade'], color='blue', linestyle='-', marker='o')
    plt.title('Vendas Diárias')
    plt.xlabel('Data')
    plt.ylabel('Quantidade Vendida')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('grafico_vendas_atualizado.png')
    plt.grid(True, linestyle='-', alpha=0.7)
    plt.show()

    print("Relatório de vendas gerado com sucesso.")

def servicos_automotivos():
    servicos = []

    with open("ordem_balanceamento.csv", mode="r", newline="") as file:
        reader = csv.DictReader(file)

        for linha in reader:
            avaliacao = random.uniform(1, 5)
            servico = {
                'servico': linha['Servico'],
                'tempo': int(linha['Minutos']),
                'satisfacao': float(linha['Satisfacao']),
                'avaliacao': round(avaliacao, 1)
            }
            servicos.append(servico)

            print(f"Cliente: {linha['Cliente']}\tCarro: {linha['Carro']}\tPlaca: {linha['Placa']}\tMecânico: {linha['Mecanico']}\tTempo: {linha['Minutos']} minutos")
            print(f"Serviço: {servico['servico']}\tTempo de Execução: {servico['tempo']} minutos\tSatisfação do Cliente: {servico['satisfacao']} de 5\tAvaliação: {servico['avaliacao']} de 5")
            print(50 * "-")

    Tmedio = sum(t['tempo'] for t in servicos) / len(servicos)
    Smedia = sum(s['satisfacao'] for s in servicos) / len(servicos)

    with open('relatorio_desempenho_servicos.txt', 'w') as arq:
        arq.write("Relatório de Desempenho de Serviços\n")
        arq.write((50 * "-") + "\n")
        arq.write(f"Total de Serviços: {len(servicos)}\n")
        arq.write(f"Tempo Médio Gasto: {Tmedio} min\n")
        arq.write(f"Satisfação Média do Consumidor: {Smedia}\n")
        arq.write("Detalhes dos Serviços:\n")
        for servico in servicos:
            arq.write(f"Cliente: {linha['Cliente']}\tCarro: {linha['Carro']}\tPlaca: {linha['Placa']}\tMecânico: {linha['Mecanico']}\tTempo: {linha['Minutos']} minutos\n")
            arq.write(f"Serviço: {servico['servico']}\tTempo de Execução: {servico['tempo']} minutos\tSatisfação do Cliente: {servico['satisfacao']} de 5\tAvaliação: {servico['avaliacao']} de 5\n")
            arq.write(50 * "-")

    print("Relatório salvo")





def Relatorio_Energetico():
  def Relatorio_Energetico():
    with open('dados_energia_solar.csv', 'r', newline='') as file:
        reader = csv.DictReader(file)
        data = list(reader)

    if not data:
        print("No data found in the CSV file.")
        return


    EsolarGerada = float(data[-1]['Energia Gerada (kWh)'])
    Econsumida = float(data[-1]['Energia Consumida (kWh)'])
    instalacao = float(data[-1]['Custo da Instalação'])
    KWh = float(data[-1]['Custo por kWh'])


    eficienciaE = (EsolarGerada / Econsumida) * 100
    economia = (Econsumida - EsolarGerada) * KWh
    retorno = instalacao / economia if economia > 0 else float('inf')


    print("Análise de Eficiência Energética e Economia\n")
    print(50 * '-')
    print(f"Eficiência Energética: {eficienciaE:.2f}%")
    print(f"Economia Atual: {economia:.2f} BRL")
    print(f"Retorno de Investimento: {retorno:.2f} anos")
while True:
  print(50*'-')
  print("\n 1 para acessar os relatorios de vendas \n 2 Desempenho dos servicos automotivos \n 3 para acessar o relatorio de energia \n 4 para retornar")
  caso = int(input(""))
  while caso not in [1,2,3,4]:
    print('ERROR! tente novamente')
  match caso:
    case 1:
      relatorio_vendas()
    case 2:
      servicos_automotivos()
    case 3: 
      Relatorio_Energetico()
    case 4:
      break

def Modulo4():

    class PainelSolar:
        def __init__(self, potencia_nominal, area, eficiencia, alerta_minimo=100):
            self.potencia_nominal = potencia_nominal
            self.area = area
            self.eficiencia = eficiencia
            self.alerta_minimo = alerta_minimo
            self.leituras_energia = []

        def ler_energia_gerada(self, radiacao_solar):
            energia_gerada = self.potencia_nominal * self.area * self.eficiencia * radiacao_solar
            self.leituras_energia.append(energia_gerada)
            return energia_gerada

        def analise_eficiencia_economia(self, energia_convencional):
            if not self.leituras_energia:
                print("Ainda não há leituras de energia gerada.")
                return 0 

            ultima_leitura = self.leituras_energia[-1]
            percentual_economia = (energia_convencional - ultima_leitura) / energia_convencional * 100
            return percentual_economia

        def alerta_falha(self, producao_atual):
            if producao_atual < self.alerta_minimo:
                print("Alerta: Produção de energia solar abaixo do limite mínimo.")

        def salvar_dados_csv(self, arquivo_csv='dados_painel_solar.csv'):
            with open(arquivo_csv, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Energia Gerada (kWh)', 'Percentual de Economia'])

                for energia_gerada in self.leituras_energia:
                    percentual_economia = self.analise_eficiencia_economia(energia_gerada)
                    percentual_economia_str = str(int(percentual_economia)) if percentual_economia is not None else ""
                    writer.writerow([energia_gerada, percentual_economia_str])

    def menu_interativo():
        painel_solar = PainelSolar(potencia_nominal=100, area=10, eficiencia=0.15)

        while True:
            print("=-=" * 10)
            escolha = int(input('''[ 1 ] Ler Energia Gerada
    [ 2 ] Analisar Eficiência e Economia
    [ 3 ] Alerta de Falha
    [ 4 ] Salvar Dados em CSV
    [ 5 ] Sair
    -> '''))

            if escolha == 1:
                radiacao_solar = float(input("Informe a radiação solar: "))
                energia_gerada = painel_solar.ler_energia_gerada(radiacao_solar)
                print(f"Energia gerada: {energia_gerada} kWh")

            elif escolha == 2:
                energia_convencional = float(input("Informe a energia convencional: "))
                percentual_economia = painel_solar.analise_eficiencia_economia(energia_convencional)
                if percentual_economia is not None:
                    print(f"Percentual de economia: {percentual_economia:.2f}%")

            elif escolha == 3:
                producao_atual = float(input("Informe a produção atual: "))
                painel_solar.alerta_falha(producao_atual)

            elif escolha == 4:
                painel_solar.salvar_dados_csv()
                print("Dados salvos em CSV.")

            elif escolha == 5:
                break
            else:
                print("Escolha inválida. Tente novamente.")

    if __name__ == "__main__":
        menu_interativo()



def main():
  while True:

    print('-' * 50)
    print('\n')
    print('Tipos de módulos disponiveis para operação: \n 1 - Módulo de Controle de Estoque de Produtos \n 2 - Módulo de Gerenciamento de Serviços Automativos \n 3 - Módulo de Gestão de Mercearia \n 4 - Módulo de Monitoramento Energetico \n 5 - Módulo de Relatórios e Análises \n 6 - Sair do programa \n')

    escolha = int(input('Digite o número de um módulo que deseja operar: '))

    print('\n')

    match escolha:
      case 1:
        Modulo1()
      case 2:
        Modulo2()
      case 3:
        Modulo3()
      case 4:
        Modulo4()
      case 5:
        Modulo5()
      case 6:
        print('Saindo do programa...')
        exit()
        break
      case _:
        print("Módulo inválido. Tente novamente.")

if __name__ == '__main__':
  main()


