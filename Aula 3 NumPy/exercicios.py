# Importando o numpy
import numpy as np

# Exercicio 1
arr1 = np.ones(8,int)
arr2 = np.random.randint(0,10,8)
soma = arr1 + arr2

print('array 1:', arr1)
print('array 2:', arr2)
print('Soma:',soma)
print('Total:', soma.sum())

if soma.sum(axis=0) >= 40:
    final = soma.reshape(4,2)
else:
    final = soma.reshape(2,4)

print(final)

# Exercicio 2
pares1 = np.arange(0,52,2)
print('Pares de 0 a 50:', pares1)

pares2 = np.arange(100,49,-2)
print('Pares de 100 a 50:', pares2)

pares = np.concatenate([pares1,pares2])
print('Concatenando:', pares)

pares.sort()
print('Ordenando:', pares)

# Exercicio 3
campo = np.zeros([2,2],int)
campo[np.random.randint(0,2),np.random.randint(0,2)] = 1

i = 0

while i < 3:
    linha = int(input('Digite a linha: '))
    coluna = int(input('Digite a coluna: '))
    print(f'Você escolheu a posição ({linha}, {coluna})')
    if campo[linha][coluna] == 1:
        print('Game Over! :( Try Again!')
        break
    elif campo[linha][coluna] == 0:
        campo[linha][coluna] = -1
        i+=1
    elif campo[linha][coluna] == -1:
        print('Voce ja escolheu esse numero. Tente novamente.')

if i == 3:
    print('Congratulations! You beat the game! :)')

# Exercicio 4
matriz = np.random.randint(0, 10, size=(np.random.randint(2, 7), np.random.randint(2, 7)))

print("Matriz:")
print(matriz)

linhas, colunas = matriz.shape # Python suporta unpacking, que e atribuir x valores a x variaveis de uma vez

print(f'Numero de linhas: {linhas}\nNumero de colunas: {colunas}')

if (linhas*colunas)%2 == 0:
    print('A matriz seria um vetor unidimensional de numero par')
else:
    print('A matriz seria um vetor unidimensional de numero impar')

# Exercicio 5
np.random.seed(10)
matriz = np.random.randint(1,51,[4,4])

print(f'Matriz:\n{matriz}')

media_linhas = np.mean(matriz, axis=1)
media_colunas = np.mean(matriz, axis=0)

print(f'Media das linhas: {media_linhas}')
print(f'Media das colunas: {media_colunas}')

print(f'Maior valor das medias das linhas: {max(media_linhas)}')
print(f'Maior valor das medias das colunas: {max(media_colunas)}')

valores, contagens = np.unique(matriz, return_counts=True)

for valor, count in zip(valores,contagens): # Zip cria um range onde o primeiro valor de valores se junta com o primeiro valor de contagens e por ai vai
    print(f'{valor} aparece {count} vezes.')

print(f'Valores que aparecem 2 vezes:\n{valores[contagens == 2]}') # Isso funciona porque contagens == 2 retorna os indices em que o array contagens tem valor = 2