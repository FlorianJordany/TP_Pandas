import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pynsee
import pynsee.download
import random

df = pd.read_csv("https://koumoul.com/s/data-fair/api/v1/datasets/igt-pouvoir-de-rechauffement-global/convert", sep=",")
df_city = pynsee.download.download_file("FILOSOFI_COM_2016")
meta = pynsee.get_file_list()
find_filosofi = meta.loc[meta['label'].str.contains(r"Filosofi.*2016")]

###### 1 ######
print("10 premières : ", df.head(10))
print("10 dernières : ", df.tail(15))
print("10 aléatoires : ", df.sample(10))
print(30*"*")


###### 2 ######
total_5 = round(len(df) * 0.05)
sample_5 = df.sample(total_5 , replace=False)
print(sample_5)


###### 3 ######
ten_first = df.head(10)
sample_100 = ten_first.sample(100, replace=True)
print(sample_100)


###### 4 ######
prob = [0.5] + [1 / (len(df.head(6)) - 1)] * (len(df.head(6)) - 1)

counts = pd.Series(random.choices(df.head(6).index, k=100, weights=prob)).value_counts()
print(counts)

