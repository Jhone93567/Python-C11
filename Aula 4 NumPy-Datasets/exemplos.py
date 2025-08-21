import numpy as np

# Criando um numpy array 2D
mtz = np.arange(1,10,1).reshape(3,3)
print(mtz)

# Extraindo apenas uma linha (Terceira linha)
print(mtz[2,:])

# Extraindo apenas uma coluna (Segunda coluna)
print(mtz[:,1])

# Extraidno da primeira coluna pra frente
print(mtz[:,1:])

# Imprimindo so os elementos pares
print(mtz[mtz%2==0])

# Criando array de strings
arr = np.array(['Goku', 'Goten', 'Gohan', 'Trunks', 'Bulma'])
print(arr)
print(np.char.find(arr,'ha')) # Retorna um array com a posicao da string buscada, -1 caso nao encontre (CASE SENSITIVE)
filtro = np.char.find(arr,'ha') >= 0
print(arr[filtro])

# Trabalhando com datasets
ds = np.loadtxt('space.csv', delimiter=';', dtype=str, encoding='utf-8') # O padrao e carregar o dataset como string

# Extraindo a coluna de custos
ds_cost = ds[1:,-2]

# Transformando em float
ds_cost = ds_cost.astype(float)

# Imprimindo a media de custos
print(ds_cost.mean())