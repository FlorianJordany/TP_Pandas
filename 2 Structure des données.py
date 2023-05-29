import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pynsee
import pynsee.download
import random

df = pd.read_csv("https://koumoul.com/s/data-fair/api/v1/datasets/igt-pouvoir-de-rechauffement-global/convert", sep=",")
df_city = pynsee.download.download_file("FILOSOFI_COM_2016")

# Vérifier les types des variables. S’assurer que les types des variables communes aux deux bases sont cohérents.
# Pour les variables qui ne sont pas en type float alors qu’elles devraient l’être, modifier leur type.

print(df.dtypes)
print(30*"*")
print(df_city.dtypes)
print(30*"*")

df_city['NBMENFISC16'] = df_city['NBMENFISC16'].astype(float)
df_city['NBPERSMENFISC16'] = df_city['NBPERSMENFISC16'].astype(float)
df_city['MED16'] = df_city['MED16'].astype(float)
df_city['PIMP16'] = df_city['PIMP16'].astype(float)
df_city['TP6016'] = df_city['TP6016'].astype(float)
df_city['TP60AGE116'] = df_city['TP60AGE116'].astype(float)
df_city['TP60AGE216'] = df_city['TP60AGE216'].astype(float)
df_city['TP60AGE316'] = df_city['TP60AGE316'].astype(float)
df_city['TP60AGE416'] = df_city['TP60AGE416'].astype(float)
df_city['TP60AGE516'] = df_city['TP60AGE516'].astype(float)
df_city['TP60AGE616'] = df_city['TP60AGE616'].astype(float)
df_city['TP60TOL116'] = df_city['TP60TOL116'].astype(float)
df_city['TP60TOL216'] = df_city['TP60TOL216'].astype(float)
df_city['PACT16'] = df_city['PACT16'].astype(float)
df_city['PTSA16'] = df_city['PTSA16'].astype(float)
df_city['PCHO16'] = df_city['PCHO16'].astype(float)
df_city['PBEN16'] = df_city['PBEN16'].astype(float)
df_city['PPEN16'] = df_city['PPEN16'].astype(float)
df_city['PPAT16'] = df_city['PPAT16'].astype(float)
df_city['PPSOC16'] = df_city['PPSOC16'].astype(float)
df_city['PPFAM16'] = df_city['PPFAM16'].astype(float)
df_city['PPMINI16'] = df_city['PPMINI16'].astype(float)
df_city['PPLOGT16'] = df_city['PPLOGT16'].astype(float)
df_city['PIMPOT16'] = df_city['PIMPOT16'].astype(float)
df_city['D116'] = df_city['D116'].astype(float)
df_city['D916'] = df_city['D916'].astype(float)
df_city['RD16'] = df_city['RD16'].astype(float)

print(df_city.dtypes)

print(30*"*")
print(30*"*")
print(30*"*")
print(30*"*")

# Vérifier les dimensions des DataFrames

print(df.shape)
print(df_city.shape)

print(30*"*")
print(30*"*")
print(30*"*")
print(30*"*")

# Vérifier le nombre de valeurs uniques des variables géographiques dans chaque base.
# Les résultats apparaissent-ils cohérents ?

print(df_city['LIBGEO'].nunique())
print(df_city['CODGEO'].nunique())

print(30*"*")
print(30*"*")
print(30*"*")
print(30*"*")

# Identifier dans df_city les noms de communes qui correspondent à plusieurs codes
# communes et sélectionner leurs codes. En d’autres termes, identifier les CODGEO tels qu’il existe des doublons de
# LIBGEO et les stocker dans un vecteur x
# (conseil: faire attention à l’index de x)

duplicates = df_city[df_city.duplicated('LIBGEO', keep=False)]
x = duplicates['CODGEO'].unique()
print(x)


print(30*"*")
print(30*"*")
print(30*"*")
print(30*"*")

# Regarder dans df_city ces observations

df_city['Count'] = df_city.groupby('LIBGEO')['CODGEO'].transform('nunique')
obs = df_city[df_city['Count'] > 2]

print(obs)

print(30*"*")
print(30*"*")
print(30*"*")
print(30*"*")

# Pour mieux y voir, réordonner la base obtenue par ordre alphabétique

df_city_sorted = obs.sort_values('LIBGEO')

print(df_city_sorted)

print(30*"*")
print(30*"*")
print(30*"*")
print(30*"*")

#Déterminer la taille moyenne (variable nombre de personnes: NBPERSMENFISC16) et quelques statistiques descriptives
# de ces données. Comparer aux mêmes statistiques sur les données où libellés et codes communes coïncident

taille_moyenne = df_city['NBPERSMENFISC16'].describe()
print(taille_moyenne)

print(30*"*")
print(30*"*")
print(30*"*")
print(30*"*")

# Vérifier les grandes villes (plus de 100 000 personnes), la proportion de villes pour lesquelles un même nom
# est associé à différents codes commune.

villes = df_city[df_city['NBPERSMENFISC16'] > 100000]
proportion = villes.groupby('LIBGEO')['CODGEO'].nunique().mean()
print(proportion)

print(30*"*")
print(30*"*")
print(30*"*")
print(30*"*")

# Vérifier dans df_city les villes dont le libellé est égal à Montreuil. Vérifier également celles qui contiennent
# le terme ‘Saint-Denis’

montreuil = df_city[df_city['LIBGEO'] == 'Montreuil']
saint_denis = df_city[df_city['LIBGEO'].str.contains('Saint-Denis')]

print(montreuil, saint_denis)



