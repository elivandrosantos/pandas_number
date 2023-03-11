import pandas as pd
import random

lotofacil = 'loto.csv'
# abrir o arquivo CSV com o pandas
try:
    df = pd.read_csv(lotofacil)
except Exception as e:
    print(f"Erro ao abrir o arquivo CSV: {e}")
    exit()

# extrair os dados do DataFrame
colunas_disponiveis = df.columns.tolist()
print(f"Colunas disponíveis: {colunas_disponiveis}")
# colunas_entrada = input("Colunas a serem usadas (separadas por vírgulas): ")
colunas_entrada = 'bola1, bola2, bola3, bola4, bola5, bola6, bola7, bola8, bola9, bola10, bola11, bola12, bola13, ' \
                  'bola14, bola15'
colunas = [col.strip() for col in colunas_entrada.split(",")]
if not set(colunas).issubset(set(colunas_disponiveis)):
    print("Alguma(s) coluna(s) não existe(m) no DataFrame.")
    exit()

numeros = df[colunas].values.flatten().tolist()
frequencias = pd.Series(numeros).value_counts(normalize=True)
probabilidades = [frequencias[num] for num in numeros]

# gerar 6 números aleatórios de acordo com as probabilidades
sorteados = random.sample(numeros, k=15)
numeros_ordenados = sorted(sorteados)

# imprimir os números sorteados

numeros_str = " ".join(str(num) for num in numeros_ordenados)
print(f"Os números sorteados são: {numeros_str}")
