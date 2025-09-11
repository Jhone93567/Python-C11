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

# Importando datasets com Pandas
ds = pd.read_csv('paises.csv', delimiter=';')
print(ds)

# Imprimindo so o nome das colunas
print(ds.columns)

# Calculando a porcentagem da populacao de cada pais em relacao ao resto
somaPopulacao = np.sum(ds['Population'])
print(somaPopulacao)

populationPerc = ds['Population']/somaPopulacao
print(populationPerc)

# Adicionando uma nova coluna no dataset
ds['PopulationPercent'] = populationPerc
print(ds)

# Exportando a nova versao do dataset
ds.to_csv('paises2.csv', sep=';')

# Agrupar os dados do dataset por regiao
group_region = ds.groupby('Region')
print(group_region.count()['Country'])

# Funcoes customizadas no pandas
def terpercent(x):
    return x*0.9

# Pegando a taxa de mortalidade do dataset
taxaMort = ds['Deathrate']

# Criando uma series descontada 10% da taxa de mortalidade
taxaMort2 = taxaMort.apply(terpercent)
print(taxaMort2)

# Criando um novo dataframe apenas com estas duas series
df2 = pd.concat([taxaMort, taxaMort2], axis=1)
df2.columns = ['Taxa de Mortalidade', 'Taxa de Mortalidade com Desconto'] # Isso muda o nome das colunas
print(df2)

# Removendo linhas com dados ausentes (remove a linha toda mesmo se faltar so uma celula)
novoDataFrame = df2.dropna()