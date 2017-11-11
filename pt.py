import pandas as pd
import numpy as np

df = pd.read_csv('cars.csv', encoding='utf-8')
print(df.head())

measuring = df.pivot_table(value='(KM)', index='YEAR', comumns='Make', aggfunc=[np.mean, np.min], margins=True)


print(measuring.head())
