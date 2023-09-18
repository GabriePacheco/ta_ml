import streamlit as st 
import pandas as pd 
import pickle 
from logo import add_logo

with open("knn_model.pkl", "rb" ) as model: 
    modelo = pickle.load( model )
    

with open("knn_encoder.pkl", "rb" ) as coder: 
    ecoder = pickle.load( coder )


@st.cache_data
def getDatas( filename ): 
   d = pd.read_csv( filename ) 
   st.session_state['data'] =  d
   return  d["PROGRAMA"].unique(), d["TARGET"].unique(),  d["CATEGORIA"].unique(), d["ITEM"].unique()

def predecir( ndf ): 
    for column in ndf.columns: 
        if column in ecoder:
            enco = ecoder[column]
            ndf[column] = enco.transform( ndf[column])
    return modelo.predict( ndf )[0]

def  raiting (): 
    add_logo()
    st.header("T.A. MODELO PROMOCIONALES")
    st.caption("Encuentra la mejor campaña promocional para el espacio")

    def getDatos(): 


        PROGRAMA, TARGET, CATEGORIA, ITEM  = getDatas( 'promocionales_2023.csv')
        
        ciudad = st.sidebar.radio("Ciudad" , options = ["QUITO", "GUAYAQUIL"])
        programa = st.sidebar.selectbox("Promgrama" , options = PROGRAMA)
        target = st.sidebar.radio("Target", options= TARGET)
        duracion = st.sidebar.slider("Duracion", max_value=90, min_value= 10, value= 20, step = 10  )
        
        seccion = st.sidebar.radio("Horario", options = ['A', 'AA', 'AAA', 'LATE', "MAD"])
        categoria = st.sidebar.selectbox("Categotia", options = CATEGORIA)
        item = st.sidebar.selectbox("Promocional" , options = ITEM)
              

        return {
            "CIUDAD" : ciudad,
            "PROGRAMA":programa,
            "TARGET": target,
            "DURACION": duracion,

            "SECCION": seccion,
            "CATEGORIA": categoria,
            "ITEM":item,            
           
        }

    df = pd.DataFrame(getDatos(), index=[0] )

    st.dataframe( df, use_container_width= True)

    if ( st.button("Encontrar campaña") ): 
        c = predecir(df)
        st.success(f"Alcazara un rating de: {c}")
        
raiting()




    
