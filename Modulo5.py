import pandas as panda
import matplotlib.pyplot as grafico
def relatorio_vendas():
  dados = { 'dias': ['2023-10-01', '2023-10-02', '2023-10-03', '2023-10-04'], 'vendas': [1000, 1200, 800, 1500]}
  dataframe = panda.DataFrame(dados)
  dataframe.to_csv('relatorio_vendas.csv', index=False)
  grafico.figure(figsize=(10, 5))
  grafico.plot(dataframe['dias'], dataframe['vendas'],color='green', linestyle = '-', marker='o')
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
        arq.write(f"Tempo de Execução: {servico['tempo_execucao']} minutos\n")
        arq.write(f"Satisfação do Cliente: {servico['satisfacao']} de 5\n")
        arq.write(50 * "-" )
  print("relatorio salvo")

def Relatorio_Energetico()
  EsolarGerada = 5000 
  KWh = 0.12  
  instalacao = 15000 
  Econsumida = 10000
  eficienciaE = (EsolarGerada/Econsumida) *100
  economia = (Econsumida - EsolarGerada) * KWh
  if economia>0:
    retorno = instalacao/economia
  else:
    retorno = float('inf')
  resultado = {'Eficiencia Energetica': eficienciaE, 
             'Economia Atual': economia,
             'Retorno de Investimento': retorno}
  with open('analise_energia_solar.txt','w') as arquivo:
    arquivo.write("Análise de Eficiência Energética e Economia\n")
    arquivo.write(50* '-' + '\n')
    for chave,valor in resultado.items():
      arquivo.write(f"{chave}:{valor} \n")
  energia_consumida = 10000  
  EsolarGerada = 5000 
  KWh = 0.12  
  instalacao = 15000  
  print("Análise salva no arquivo 'analise_energia_solar.txt'")
while True
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
