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
                return 0  # Retorna 0 quando não há leituras

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
