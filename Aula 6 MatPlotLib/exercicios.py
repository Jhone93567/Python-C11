import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Exercicio 1
paises = pd.read_csv('paises.csv', delimiter= ';')
paisesNA = paises[paises['Region'] == 'NORTHERN AMERICA                   ']
paisesNA.plot(x='Country', y=['Birthrate','Deathrate'], kind='line')
plt.show()

# Exercicio 2
space = pd.read_csv('space.csv', delimiter= ';')
spaceSlice = space[space['Location'].str.contains('(USA)|(China)')]
spaceSlice['Country'] = spaceSlice['Location'].str.split().str[-1]
spaceSlice = spaceSlice.drop_duplicates(subset=['Company Name'])
company_count = spaceSlice['Country'].value_counts()
company_count.plot(kind='bar', xlabel='Country', ylabel='Number of companies')
plt.show()

# Exercicio 3
spaceSlice = space[space['Company Name'] == 'Roscosmos']
mission_counts = spaceSlice['Status Mission'].value_counts()
mission_counts.plot(kind='pie', autopct='%1.1f%%', ylabel='')
plt.show()