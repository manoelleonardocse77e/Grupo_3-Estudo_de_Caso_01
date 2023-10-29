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
        print("\n1. Ler energia gerada")
        print("2. Análise de eficiência e economia")
        print("3. Alerta de falha")
        print("4. Sair")
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
