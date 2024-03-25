print('=' * 10 + '\033[0;31m Inicializando o Contador de Dias \033[0m' + '=' * 10)

from datetime import datetime
from alive_progress import alive_bar
import time

def contar_dias(data_informada):
    # Obter a data atual
    data_atual = datetime.now().date()

    # Converter a data informada para o formato de data
    data_informada = datetime.strptime(data_informada, "%d-%m-%Y").date()

    # Calcular a diferença de dias
    diferenca = data_atual - data_informada

    return diferenca.days

# Obter a data do usuário
data_informada = input("\033[0;31m > Informe a data (no formato DD-MM-YYYY):  \033[0m")

# Chamar a função e imprimir o resultado
with alive_bar(100) as bar:
    for _ in range(100):
        time.sleep(0.01)
        bar()

dias = contar_dias(data_informada)
print("\033[0;31m > Fazem ", dias, "dias que nos conhecemos! ❤ \033[0m")
