import pandas as pd
import numpy as np

ds = pd.read_csv('paises.csv', delimiter=';')
oceania = ds[ds["Region"].str.contains("OCEANIA")]

print(oceania)
print(len(oceania))

print(ds.loc[[ds["Population"].idxmax()], ["Country", "Region"]])

regions = ds.groupby("Region")
print(regions["Literacy (%)"].mean())

ds_noCoast = ds[ds["Coastline (coast/area ratio)"] == 0]

ds_noCoast.to_csv('paises2.csv', sep=';')

def mortalidade(x):
    if x < 9:
        return 'Balanced'
    else:
        return 'Urgent'

novo_ds = ds["Deathrate"].apply(mortalidade).rename("Humanitarian Help")
ds_final = pd.concat([ds,novo_ds], axis=1)
print(ds_final)