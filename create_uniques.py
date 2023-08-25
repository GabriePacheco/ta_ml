import pandas as pd 

df = pd.read_csv('promocionales_2023.csv')

columnas = ['ITEM','GENERO','CAMPAÑA','TARGET']


for col in columnas:
    uniques = df[col].unique()
    ndf = pd.DataFrame(data= uniques, columns=[col])
    ndf.to_csv(f'{col}.csv')
    
    


