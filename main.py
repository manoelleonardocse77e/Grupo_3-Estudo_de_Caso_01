import csv
import pandas as panda
import matplotlib.pyplot as grafico
def Modulo1():

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
          with open('estoque.csv', 
                    'w', newline='') as file:
              writer = csv.writer(file)
              for linha in data:
                writer.writerow(linha)
          with open('estoque.csv', 'r', newline='') as file:
              reader = csv.reader(file)
              for linha in reader:
                  if linha and linha[0] == self.nome_produto and len(linha) >= 2:
                      linha[1] = str(self.quantidade)
                  data.append(linha)



  # estoque inicial xD

  # caso 1 para criar produto e definir seu nome, quantidade e limite de aviso
  gasolina = Estoque("Gasolina", 100, 20)
  alcool = Estoque("Álcool", 80, 40)
  diesel = Estoque("Diesel", 100, 20)
  energia_solar = Estoque("Energia Solar", 50, 10)

  # caso 2 em que deve ser usado em um laço de repitação e com limite predefinido de produtos (caso precise)
  # nome = str(input('Insira nome do produto = '))
  # quantidade = float(input('Insira quantidade inicial do produto = '))
  # limite = int(input('Limite quantitativo para aviso ='))
  # produto1 = Estoque(nome, quantidade, limite)

  #exemplo de execução
  gasolina.receber_produto(50)
  gasolina.vender_produto(30)
  gasolina.verificar_estoque()

  energia_solar.vender_produto(60)
  energia_solar.verificar_estoque()

  alcool.vender_produto(60)
  alcool.verificar_estoque()

def Modulo2():
  def criar_os_oleo(cliente, carro, placa, mecanico, oleo, conta_oleo, tempoT):
    cliente = input("Digite o nome do cliente: \n")
    carro = input("Digite as informações do carro:\n")
    placa = input("Placa do carro:\n")
    mecanico = input("Mecânico responsável:\n")
    oleo = input("Óleo usado:\n")
    conta_oleo = int(input("Litros de óleo usado:\n"))
    tempoT = input("Tempo gasto no serviço:\n(Minutos)\n")
    servico = "Troca de oleo"
    
    os_oleo = {
        "Cliente": cliente,
        "Carro": carro,
        "Placa": placa,
        "Mecânico": mecanico,
        "Óleo": oleo,
        "Litros de Óleo": conta_oleo,
        "Minutos": tempoT
    }
    registrar_oleo(os_oleo)

  def registrar_oleo(os_oleo):
    with open("ordem_oleo.csv", mode="a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=os_oleo.keys())

        writer.writerow(os_oleo)

  def criar_os_balanceamento(cliente, carro, placa, mecanico, tempoB):
    cliente = input("Digite o nome do cliente: \n")
    carro = input("Digite as informações do carro:\n")
    placa = input("Placa do carro:\n")
    mecanico = input("Mecânico responsável:\n")
    tempoB = input("Tempo gasto no serviço:\n(minutos)\n")
    servico = "Balanceamento"
    
    os_balanceamento = {
        "Cliente": cliente,
        "Carro": carro,
        "Placa": placa,
        "Mecânico": mecanico,
        "Minutos": tempoB
    }
    registrar_balanceamento(os_balanceamento)

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
    servico = int(input("Informe o serviço solicitado:\n(1-Troca de óleo e 2-Balanceamento)\n"))
    
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

  menu = int(input("Digite qual operação deseja:\n1 - Agendamento \n2 - Ordem de Serviço \n3 - Consultar histórico \n4 - Apagar agenda\n"))
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
      serv = int(input("Informe o serviço:\n1- Troca de óleo \n2- Balanceamento"))
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
        print("Relatório de vendas gerado com sucesso.")

    def servicos_automotivos():
        servicos = [
            {'servico': 'troca de óleo', 'tempo': 25, 'satisfacao': 4.2},
            {'servico': 'troca de pneus', 'tempo': 47, 'satisfacao': 5.0},
            {'servico': 'reparo de freios', 'tempo': 90, 'satisfacao': 2.5},
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
        print("Relatório salvo")

    def Relatorio_Energetico():
        EsolarGerada = 5000
        KWh = 0.12
        instalacao = 15000
        Econsumida = 10000
        eficienciaE = (EsolarGerada / Econsumida) * 100
        economia = (Econsumida - EsolarGerada) * KWh
        if economia > 0:
            retorno = instalacao / economia
        else:
            retorno = float('inf')
        resultado = {'Eficiencia Energetica': eficienciaE,
                     'Economia Atual': economia,
                     'Retorno de Investimento': retorno}
        with open('analise_energia_solar.txt', 'w') as arquivo:
            arquivo.write("Análise de Eficiência Energética e Economia\n")
            arquivo.write(50 * '-' + '\n')
            for chave, valor in resultado.items():
                arquivo.write(f"{chave}:{valor} \n")
        energia_consumida = 10000
        EsolarGerada = 5000
        KWh = 0.12
        instalacao = 15000
        print("Análise salva no arquivo 'analise_energia_solar.txt'")
    while True:
        print(50 * '-')
        print("\n 1 - Para acessar os relatórios de vendas \n 2 - Desempenho dos serviços automotivos \n 3 - Para acessar o relatório de energia \n 4 - Para retornar")
        caso = int(input(""))
        while caso not in [1, 2, 3, 4]:
            print('ERROR! Tente novamente')
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

    def ler_energia_gerada(self, radiacao_solar):
        energia_gerada = self.potencia_nominal * self.area * self.eficiencia * radiacao_solar
        return energia_gerada

    def analise_eficiencia_economia(self, energia_gerada, energia_convencional):
        percentual_economia = (energia_convencional - energia_gerada) / energia_convencional * 100
        return percentual_economia

    def alerta_falha(self, producao_atual):
        if producao_atual < self.alerta_minimo:
            print("Alerta: Produção de energia solar abaixo do limite mínimo.")


  if __name__ == "__main__":
    painel_solar = PainelSolar(potencia_nominal=300, area=20, eficiencia=0.85, alerta_minimo=200)

    while True:
        print("\n1 - Ler energia gerada")
        print("2 - Análise de eficiência e economia")
        print("3 - Alerta de falha")
        print("4 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            radiacao_solar = float(input("Informe a radiação solar: "))
            energia_gerada = painel_solar.ler_energia_gerada(radiacao_solar)
            print(f"Energia gerada pelo painel solar: {energia_gerada} kWh")

        elif opcao == '2':
            energia_gerada = float(input("Energia gerada pelo painel solar: "))
            energia_convencional = float(input("Energia gerada por fontes convencionais: "))
            percentual_economia = painel_solar.analise_eficiencia_economia(energia_gerada, energia_convencional)
            print(f"Percentual de economia: {percentual_economia} %")

        elif opcao == '3':
            producao_atual = float(input("Produção atual: "))
            painel_solar.alerta_falha(producao_atual)

        elif opcao == '4':
            break

        else:
            print("Opção inválida. Escolha uma opção válida.")
while True:
#Começo menu de escolhas
  print('Tipos de módulos disponiveis para operação: \n 1 - Módulo de Controle de Estoque de Produtos \n 2 - Módulo de Gerenciamento de Serviços Automativos \n 3 - Módulo de Gestão de Mercearia \n 4 - Módulo de Monitoramento Energetico \n 5 - Módulo de Relatórios e Análises \n')
  print('-' * 50)
  print('\n')

  escolha = int(input('Digite o número de um módulo que deseja operar: '))

  while escolha not in [1,2,3,4,5]:
    print('Módulo Invalido!')
    escolha = int(input('Digite o número de um módulo que deseja operar: '))

  print('\n')
  print('-' * 50)
  print('\n')

  match escolha:
    case 1:
      Modulo1()
      break
    case 2:
      Modulo2()
      break
    case 3: 
      Modulo3()
      break
    case 4:
      Modulo4()
      break
    case 5:
      Modulo5()
      
      break
#Fim menu de escolhas