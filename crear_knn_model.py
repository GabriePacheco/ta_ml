import pandas as pd 
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, confusion_matrix
import pickle


df = pd.read_csv("promocionales_2023.csv")
df_promos = df[[ "CIUDAD", "PROGRAMA", "TARGET","DURACION", "CAMPAÑA", "SECCION", "CATEGORIA", "ITEM"]]

# DIVIDIR EN ETIQUETA Y CARACTERISTICAS 
X = df_promos.drop("CAMPAÑA", axis= 1) # caracteristicas 
y = df_promos["CAMPAÑA"] # etiqueta

# dividir en train y test 
## preprocesar 
encoders = {}
for column in X.select_dtypes( include=['object']).columns: 
    encoder = LabelEncoder()
    X[column] = encoder.fit_transform(X[column])
    encoders[column] = encoder
    
    
## train test 
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size= 0.70, random_state = 42)

# entrenar modelo 
modelo = KNeighborsClassifier();
modelo.fit(X_train, y_train)

model_name = "knn_model.pkl"
encoder_name = "knn_encoder.pkl"

with open( model_name, 'wb') as file: 
    pickle.dump(modelo, file)
    
with open( encoder_name, 'wb') as file2:
    pickle.dump( encoders, file2)

print("Modelos guardados con exito ")