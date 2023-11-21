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
            return None

        ultima_leitura = self.leituras_energia[-1]
        percentual_economia = (energia_convencional - ultima_leitura) / energia_convencional * 100
        return percentual_economia

    def alerta_falha(self, producao_atual):
        if producao_atual < self.alerta_minimo:
            print("Alerta: Produção de energia solar abaixo do limite mínimo.")

# Exemplo de uso:
painel_solar = PainelSolar(potencia_nominal=300, area=20, eficiencia=0.85, alerta_minimo=200)

# Leitura de energia gerada
radiacao_solar_1 = 5.0
energia_gerada_1 = painel_solar.ler_energia_gerada(radiacao_solar_1)

# Leitura posterior
radiacao_solar_2 = 4.5
energia_gerada_2 = painel_solar.ler_energia_gerada(radiacao_solar_2)

# Análise de eficiência e economia
energia_convencional = 1000
percentual_economia = painel_solar.analise_eficiencia_economia(energia_convencional)
print(f"Percentual de economia: {percentual_economia}%")

# Alerta de falha
producao_atual = 150
painel_solar.alerta_falha(producao_atual)
