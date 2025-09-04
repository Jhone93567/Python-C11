import numpy as np

ds = np.loadtxt('shopping_trends.csv',delimiter=',',dtype=str,encoding='utf-8')

# Questao 1
ds_idade = ds[1:,[1,2]]

ds_idade = ds_idade[ds_idade[:,1] == 'Male']

print(f'A media de idade dos homens e: {round(ds_idade[:,0].astype(int).mean(),2)}')

# Questao 2
ds_gastos = ds[1:,5]

ds_media_gastos = ds_gastos.astype(float).mean()

print(f'{ds_gastos[ds_gastos.astype(int) > ds_media_gastos].size} clientes gastaram mais que a media')

# Questao 3
ds_itens = ds[1:,3]

ds_itens = np.array(np.unique(ds_itens, return_counts=True))

total_vendido = ds_itens[1,:].astype(int).sum()

print(f'O item menos vendido e {ds_itens[0,ds_itens[1,:].astype(int).argmin()]} com {round((ds_itens[1,ds_itens[1,:].astype(float).argmin()].astype(int)*100) / total_vendido,2)}% das vendas')

# Questao 4
ds_discount = ds[1:,-5]

print(f'{ds_discount[ds_discount == 'Yes'].size/ds_discount.size*100}% das compras tiveram algum tipo de desconto')

# Questao 5
ds_season = ds[1:,[8,9]]

ds_season = ds_season[ds_season[:,1] == 'Summer']

ds_season = np.array(np.unique(ds_season[:,0],return_counts=True))

ds_season = ds_season[0,ds_season[1,:].astype(int).argmax()]

print(f'A cor mais popular no verao segundo esse dataset foi {ds_season}.')