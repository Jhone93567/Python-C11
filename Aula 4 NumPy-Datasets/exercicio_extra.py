import numpy as np

ds = np.loadtxt('paises.csv', delimiter=';', dtype=str, encoding='utf-8')

# Questao 1
ds_slice = ds[1:,0:4]

print(ds_slice)

# Questao 2
ds_regions = ds[1:,1]

ds_unique_regions = np.unique(ds_regions)

print(ds_unique_regions)

# Questao 3
ds_literacy = ds[1:,-11]

ds_literacy = ds_literacy[ds_literacy.astype(float) > 0].astype(float).mean()

print(f'Taxa media de alfabetizacao do planeta: {round(ds_literacy,2)}')

# Questao 4
filtro = ds_regions == 'NORTHERN AMERICA                   '

print(f'Numero de paises da america do norte: {len(ds_regions[filtro])}')

# Questao 5
ds_gdp = ds[1:,[0,1,-12]]

ds_gdp = ds_gdp[ds_gdp[:,1] == 'LATIN AMER. & CARIB    ']

indice_do_maior = ds_gdp[:,2].astype(int).argmax()

print(f'Pais da america latina e caribe com maior GDP: {ds_gdp[indice_do_maior,:]}')