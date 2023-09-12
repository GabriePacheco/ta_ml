import pandas as pd 
# importar librerias necesarias 
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
import pickle


# cargar dataframe
df = pd.read_csv( 'promocionales_2023.csv')


# renombrar columnas 
df.rename( columns =  {"SECCION/BLOQUE": 'SECCION', 'CAMPAÑA': 'CAMPANIA', 'Rat.Prom.Prog': 'RATING' }, inplace = True)

# separar datos en etiquetas y categorias 
X = df[["PROGRAMA", "ITEM", "SECCION", 'CIUDAD', 'TARGET']].copy(deep = True)
y = df['RATING']

#PREPOSESAR CARACTERISTICAS
encoders = {}
for column in X.select_dtypes(include = ['object'] ).columns:

    encoder = LabelEncoder()
    X[column] = encoder.fit_transform( X[column] )
    encoders[column] = encoder
    
    
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= 0.20 , random_state = 42 )

modelo = DecisionTreeRegressor()
modelo.fit(X_train, y_train)

modelName  = "dtrm_model.pkl"
encodersName = "dtr_encoders.pkl"

pickle.dump( modelo,  open(modelName, 'wb')) 
pickle.dump(encoders,  open(encodersName, 'wb')) 


print (encoders)