print('>>>>>>> Contador de Dias <<<<<<<')

from datetime import datetime

def contar_dias(data_informada):
    # Obter a data atual
    data_atual = datetime.now().date()

    # Converter a data informada para o formato de data
    data_informada = datetime.strptime(data_informada, "%d-%m-%Y").date()

    # Calcular a diferença de dias
    diferenca = data_atual - data_informada

    return diferenca.days

# Obter a data do usuário
data_informada = input("> Informe uma data (no formato DD-MM-YYYY): ")

dias = contar_dias(data_informada)
print("> Se passaram ", dias, "dias desde a data informada!")
