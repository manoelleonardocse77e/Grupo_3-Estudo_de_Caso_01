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
