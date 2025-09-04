import pandas as pd
import numpy as np

# Series sao estrutura de dados do Panda UniDimensionais
indices = ['a','b','c']
valores = [10,20,30]
dic = {'a':10,'b':20,'c':30}
dic2 = {'a':10,'b':20,'d':40}

# Duas formas de criar uma Series
series = pd.Series(data=valores,index=indices)
series2 = pd.Series(dic2)

print(series)
print(series2)

# Operacoes entre Series
print(series + series2)
print(series - series2)

# Operacoes usando Pandas
print(series.add(series2,fill_value=0))
print(series.sub(series2,fill_value=0))

np.random.seed(10)

# Dataframes funcionam como planilhas do excel, possuem 2 ou mais dimensoes
df = pd.DataFrame(index=['A','B','C','D','E'], columns=['W','X','Y','Z'], data=np.random.randint(1,50,[5,4]))

print(df)

# Slicing com iloc - indices
print(df.iloc[0:2, :])

# Slicing com loc - mais customizavel
print(df.loc[['A', 'B'], ['W', 'X', 'Y', 'Z']])

# Imprime so as colunas W e Y
print(df[['W','Y']])