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
    # Read information from the CSV file created in module 4
    with open('dados_energia_solar.csv', 'r', newline='') as file:
        reader = csv.DictReader(file)
        data = list(reader)

    if not data:
        print("No data found in the CSV file.")
        return

    # Extract relevant information from the CSV data
    EsolarGerada = float(data[-1]['Energia Gerada (kWh)'])
    Econsumida = float(data[-1]['Energia Consumida (kWh)'])
    instalacao = float(data[-1]['Custo da Instalação'])
    KWh = float(data[-1]['Custo por kWh'])

    # Perform calculations
    eficienciaE = (EsolarGerada / Econsumida) * 100
    economia = (Econsumida - EsolarGerada) * KWh
    retorno = instalacao / economia if economia > 0 else float('inf')

    # Display the information on the screen
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
