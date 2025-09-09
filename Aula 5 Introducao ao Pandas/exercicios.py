import numpy as np
import pandas as pd

# Exercicio 1
seriesAno1 = pd.Series({'Java': 16.25, 'C': 16.04, 'Python': 9.85})
seriesAno2 = pd.Series({'C': 16.21, 'Python': 12.12, 'Java': 11.68})

# Exercicio 2
print(f'Total ano 1: {seriesAno1.sum()}%')
print(f'Total ano 2: {seriesAno2.sum()}%')

# Exercicio 3
mudancas = seriesAno2.sub(seriesAno1)
print(f'Mudanca do ano 1 para o ano 2:\n{mudancas}')

# Exercicio 4
print(f'Os valores positivos sao:\n{mudancas[mudancas > 0]}')

# Exercicio 5
seriesAno4 = seriesAno2 + 2*mudancas

print(f'No ano 4 a linguagem mais popular e: {seriesAno4.nlargest(1)}')

# Exercicio 6
np.random.seed(10)

df = pd.DataFrame(index=['A','B','C','D','E'], columns=['W','X','Y','Z'], data=np.random.randint(1,50,[5,4]))

df_x = df.loc[:]['X']

print(f"A media dos elementos da coluna X que sao menores que 30: {df_x[df_x<30].mean()}")

# Exercicio 7
print(f"Media dos elementos da linha D: {df.loc['D'].mean()}")
print(f"Media dos elementos da linha E: {df.iloc[4].mean()}")

# Exercicio 8
df_slice = df.loc[['A','C','E'],['X','Y']]

print(f"Mostrando as linhas A C e E e as colunas X e Y:\n{df_slice}")
print(f"Soma das linhas:\n{df_slice.sum(axis=1)}")
print(f"Soma das colunas:\n{df_slice.sum()}")