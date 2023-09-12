# importa librerias necesarias
import pandas as pd 
import numpy as np 
# importar librerias necesarias 
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import DecisionTreeRegressor
from sklearn.preprocessing import LabelEncoder
import pickle

# CREAR MODELOS DESITIONA TREE CLASSIFIER 
# cargar dataframe
df = pd.read_csv( 'promocionales_2023.csv')

## limpiar y columnas 
df.drop(['Unnamed: 0', 'HORA_INICIO','HORA_FIN', 'HORA', 'FECHA', 'VERSION' , 'BREAK', 'TARIFA','TIPO', 'SECCION', 'CATEGORIA'], axis = 1, inplace = True )

# renombrar columnas 
df.rename( columns =  { 'CAMPAÑA': 'CAMPANIA', 'Rat.Prom.Prog': 'RATING' }, inplace = True)

# separar datos en etiquetas y categorias 
X = df.drop("PROGRAMA", axis = 1)
y = df['PROGRAMA']


#PREPOSESAR CARACTERISTICAS
encoders = {}
for column in X.select_dtypes(include = ['object'] ).columns:
    encoder = LabelEncoder()
    X[column] = encoder.fit_transform( X[column] )
    encoders[column] = encoder
    
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= 0.20 , random_state = 42 )

modelo = DecisionTreeClassifier()
modelo.fit(X_train, y_train)


modelName  = "tcm_model.pkl"
encodersName = "tcm_encoder.pkl"

pickle.dump( modelo,  open(modelName, 'wb')) 
pickle.dump(encoders,  open(encodersName, 'wb')) 

