import pandas as pd
import random

# abrir o arquivo CSV com o pandas
try:
    df = pd.read_csv('numeros.csv')
except Exception as e:
    print(f"Erro ao abrir o arquivo CSV: {e}")
    exit()

# extrair os dados do DataFrame
colunas_disponiveis = df.columns.tolist()
print(f"Colunas disponíveis: {colunas_disponiveis}")
# colunas_entrada = input("Colunas a serem usadas (separadas por vírgulas): ")
colunas_entrada = 'one, two, three, four, five, six'
colunas = [col.strip() for col in colunas_entrada.split(",")]
if not set(colunas).issubset(set(colunas_disponiveis)):
    print("Alguma(s) coluna(s) não existe(m) no DataFrame.")
    exit()

numeros = df[colunas].values.flatten().tolist()
frequencias = pd.Series(numeros).value_counts(normalize=True)
probabilidades = [frequencias[num] for num in numeros]

# gerar 6 números aleatórios de acordo com as probabilidades
sorteados = random.choices(numeros, weights=probabilidades, k=6)
numeros_ordenados = sorted(sorteados)

# imprimir os números sorteados

numeros_str = " ".join(str(num) for num in numeros_ordenados)
print(f"Os números sorteados são: {numeros_str}")
