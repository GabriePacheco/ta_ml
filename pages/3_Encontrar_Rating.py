import streamlit as st 
import pandas as pd 
import pickle 
from logo import add_logo

with open("dtrm_model.pkl", "rb" ) as model: 
    modelo = pickle.load( model )
    

with open("dtr_encoders.pkl", "rb" ) as  coder: 
    ecoder = pickle.load( coder )


@st.cache_data
def getDatas( filename ): 
   d = pd.read_csv( filename ) 
   st.session_state['data'] =  d
   return d["PROGRAMA"].unique(), d["ITEM"].unique(), d["TARGET"].unique()

def predecir( ndf ): 
    for column in ndf.columns: 
        if column in ecoder:
            enco = ecoder[column]
            ndf[column] = enco.transform( ndf[column])
    return modelo.predict( ndf )[0]

def  raiting (): 
    add_logo()
    st.header("T.A. MODELO PROMOCIONALES")
    st.caption("Predice el Raiting que tendra un promocional")

    def getDatos(): 
        prog, items, targets = getDatas( 'promocionales_2023.csv')

        programa = st.sidebar.selectbox("Promgrama" , options = prog)
        item = st.sidebar.selectbox("Promocional" , options =items)
        seccion = st.sidebar.radio("Horario", options = ['A', 'AA', 'AAA', 'LATE', "MAD"])
        ciudad = st.sidebar.radio("Ciudad", options= ["QUITO", "GUAYAQUIL"])
        target = st.sidebar.radio("Target", options= targets)

        return {
            "PROGRAMA":programa,
            "ITEM":item,
            "SECCION": seccion,
            "CIUDAD":ciudad ,
            "TARGET":target
        }

    df = pd.DataFrame(getDatos(), index=[0] )

    st.dataframe( df, use_container_width= True)

    if ( st.button("Predecir el Rating") ): 
        rating = predecir(df)
        st.success("Alcazara un rating de: {0:.5f}".format(rating) )
        


raiting()




    
