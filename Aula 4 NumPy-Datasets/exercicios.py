import numpy as np

ds = np.loadtxt('space.csv', delimiter=';', dtype=str, encoding='utf-8')

# Exercicio 1
ds_success = ds[1:,-1]

ds_success_rate = ds_success[ds_success == 'Success'].size / ds_success.size

print(f'Porcentagem de missoes que deram certo: {round(ds_success_rate*100,2)}%')

# Exercicio 2
ds_cost = ds[1:,-2]

ds_cost = ds_cost[ds_cost.astype(float) > 0].astype(float)

print(f'Media de gastos de uma missao: ${round(ds_cost.mean(),2)} bilhoes')

# Exercicio 3
ds_local = ds[1:,2]

ds_local = np.char.rsplit(ds_local, sep=' ',maxsplit=1)

ds_local = np.array(ds_local.tolist())[:,-1]

print(f'Missoes realizadas nos EUA: {ds_local[ds_local == 'USA'].size}')

# Exercicio 4
ds_companyCost = ds[1:, [1,-2]]

ds_companyCost = ds_companyCost[ds_companyCost[:,0] == 'SpaceX']

print(f'Missao mais cara realizada pela SpaceX: ${ds_companyCost[:,1].astype(float).max()} bilhoes')

# Exercicio 5
ds_companies = ds[1:,1]

ds_companies = np.column_stack(np.unique_counts(ds_companies))

for i in range(len(ds_companies)):
    print(f'Empresa: {ds_companies[i,0]:<20} | \tNumero de missoes: {ds_companies[i,1]:>3}')