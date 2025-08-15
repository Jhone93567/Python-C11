import numpy as np # Tudo comeca aqui

arr = np.array([10,20,30]) # Criando uma ndarray (N Dimensions Array)

print(arr)
print(type(arr))

mtz = np.array([[0,1,2],[10,20,30]]) # Criando uma matriz
print(mtz)

# FUNCOES PARA ESTRUTURAR NUMPY ARRAYS
# Array de 1D de 1s
arr = np.ones(10)
print(arr)

# Array 2D de 0s com RESHAPE
mtz = np.zeros(10).reshape(5,2)

print(mtz)

mtz = np.zeros([5,2])

print(mtz)

# Cria um array de 10  a 100 incrementado de 10 em 10
arr = np.arange(10,101,10)
print(arr)

# Imprime o minimo
print(arr.min())

# Imprime o maximo
print(arr.max())

# Imprime a media
print(arr.mean())

# Imprime o numero do maior indice
print(arr.argmax())

# Operacao com matriz
arr1 = np.arange(1,10,1)
arr2 = np.arange(9,0,-1)

print(arr1)
print(arr2)

print(arr1 + arr2) # Somando matriz

print(np.concatenate((arr1,arr2))) # Concatenando

mtz = np.array([50,10,100,60,25,100,75,80,100]).reshape(3,3)
print(mtz)

print(mtz.sum(axis=0)) # Soma sobre as colunas

print(mtz.sum(axis=1)) # Soma sobre as linhas

print(mtz.sum(axis=0)[2]) # Soma da coluna 2

print(mtz/10) # Divide todos os elementos por 10

# Numeros aleatorios
arr = np.random.randint(1,101,10) # Array de numeros aleatorios
print(arr)

np.random.seed(10) # Seta a seed dos numeros aleatorios para 10, agora toda vez vai retornar os mesmos numeros
arr = np.random.randint(1,101,10)
print(arr)
print(np.unique(arr, return_counts=1)) # Retorna os numeros unicos e conta quantas vezes cada um se repete