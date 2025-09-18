import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Plots com matplotlib
x = np.array([1,2,3,4,5])
y = x*2
y2 = x*x

# Legendas dos eixos X e Y
plt.xlabel('Valores de X')
plt.ylabel('Valores de Y')

# Criando a matriz de subplots, ou seja, onde vamos tracar os graficos separados
plt.subplot(1,2,1)
plt.plot(x,y, '*:r', linewidth=3, markersize=10)

plt.subplot(1,2,2)
plt.plot(x,y2,'s--g', linewidth=3, markersize=10)

plt.show()

# Grafico de dispersao (SCATTER PLOT)
dfPaises = pd.read_csv('paises.csv', delimiter=';')
print(dfPaises.columns)

# Extraindo os 6 maiores paises em area do mundo
dfMaioresPaises = dfPaises.nlargest(6, 'Area (sq. mi.)')
print(dfMaioresPaises['Country'])

# Tracar um Scatter Plot que ilustre o GDP per capita destes paises
plt.scatter(dfMaioresPaises['Country'], dfMaioresPaises['GDP ($ per capita)'], s=500)
plt.show()

# Grafico em Barras (BAR PLOT)
# Extraindo os 5 paises com maior GDP deste dataset
dfMaioresGDP = dfPaises.nlargest(5,'GDP ($ per capita)')
print(dfMaioresGDP['Country'])

plt.bar(dfMaioresGDP['Country'], dfMaioresGDP['GDP ($ per capita)'])
plt.show()

# Grafico de Pizza (PIE CHART)
# Extraidno os paises que nao tem acesso ao mar
dfNoCoast = dfPaises[dfPaises['Coastline (coast/area ratio)'] == 0]
print(dfNoCoast['Country'])

# Extraindo quantos paises nao tem costa
qtNoCoast = len(dfNoCoast)
qtCoast = len(dfPaises) - qtNoCoast

# Plotando o grafico em pizza
plt.pie([qtNoCoast, qtCoast], labels=['Paises sem costa', 'Paises com costa'], autopct='%1.1f%%')
plt.show()