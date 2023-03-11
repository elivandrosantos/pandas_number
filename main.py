# import pandas as pd
# import numpy as np
# import random
#
# # ler os dados dos resultados anteriores da Mega-Sena
# try:
#     df = pd.read_csv('numeros.csv')
# except FileNotFoundError:
#     print('Erro ao abrir o arquivo CSV: arquivo não encontrado')
#     exit()
#
# # selecionar as colunas dos números sorteados
# colunas = ['one', 'two', 'three', 'four', 'five', 'six']
# # Transformar os dados em um array
# numeros = df[colunas].to_numpy().flatten()
#
# # calcular as frequências e probabilidades usando numpy
# # Contagem de frequência de cada um dos elementos, com o minlength definindo a composição
# frequencias = np.bincount(numeros, minlength=61)[1:]
# # Calculando a probabilidade
# probabilidades = frequencias / numeros.size
#
# # gerar 6 números aleatórios de acordo com as probabilidades
# # Gerar números aleatórios usando as probabilidades correspondentes
# sorteados = np.random.choice(np.arange(1, 61), 6, p=probabilidades)
# # Ordenar os números sorteados
# numeros_ordenados = np.sort(sorteados)
#
# # Exibir os números sorteados
# print(f'Os números sorteados são: {numeros_ordenados}')
import requests

import requests
username = 'ordnavile'
token = 'c65f93f7bb283d0a5afe0dcbf5c5ba9811ed4227'

response = requests.get(
    'https://www.pythonanywhere.com/api/v0/user/{username}/cpu/'.format(
        username=username
    ),
    headers={'Authorization': 'Token {token}'.format(token=token)}
)
if response.status_code == 200:
    print('CPU quota info:')
    print(response.content)
else:
    print('Got unexpected status code {}: {!r}'.format(response.status_code, response.content))
