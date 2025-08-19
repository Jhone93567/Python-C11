import numpy as np

# Importando o dataset
dataset = np.loadtxt('space.csv', delimiter=',',dtype=str, encoding='utf-8')

print(dataset)