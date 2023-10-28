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
    print('inserir def do mod 1')
  case 2:
    print('inserir def do mod 2')
  case 3: 
    print('inserir def do mod 3')
  case 4:
    print('inserir def do mod 4')
  case 5:
    print('inserir def do mod 5')
#Fim menu de escolhas