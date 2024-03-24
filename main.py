from datetime import datetime

def contar_dias(data_informada):
    # Obter a data atual
    data_atual = datetime.now().date()

    # Converter a data informada para o formato de data
    data_informada = datetime.strptime(data_informada, "%Y-%m-%d").date()

    # Calcular a diferença de dias
    diferenca = data_atual - data_informada

    return diferenca.days

# Obter a data do usuário
data_informada = input("Informe a data (no formato YYYY-MM-DD): ")

# Chamar a função e imprimir o resultado
print("Quantidade de dias desde a data informada:", contar_dias(data_informada), "dias")
