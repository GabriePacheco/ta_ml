import streamlit as st 
import pandas as pd 
import pickle 

modelName  = "tcm_model.pkl"
encodersName = "tcm_encoder.pkl"
dtrm_l =  pickle.load( open(modelName, 'rb' ))
dtrm_e = pickle.load( open(encodersName, 'rb'))


@st.cache_data
def getData( filename ): 
   st.session_state['data'] = pd.read_csv( filename )   
   return pd.read_csv('ITEM.csv')['ITEM'], pd.read_csv('GENERO.csv')['GENERO'],  pd.read_csv('CAMPAÑA.csv')['CAMPAÑA'],  pd.read_csv('TARGET.csv')['TARGET']
    
def clasificar( ndata ):
    for column in ndata.columns: 
        if column in dtrm_e:
            enco = dtrm_e[column]
            ndata[column] = enco.transform(ndata[column])

    return   dtrm_l.predict( ndata )[0]

def getTopTen( programa ): 
    dp = st.session_state['data'][ st.session_state['data']['PROGRAMA'] == programa  ]
    return dp.groupby("ITEM")["RATING"].mean().sort_values(ascending =  False).head(10)

def main(): 
    st.title("T.A. MODELO PROMOCIONALES")
    st.caption("Encuentra el mejor programa para el lanzamiento del promocional")

    st.sidebar.subheader ("Entrada de datos")
    st.sidebar.divider()

    def get_parametros(): 

        items, generos, campanias, targets = getData( 'promocionales_2023.csv')

        campania = st.sidebar.selectbox('Campaña', options = campanias)
        
        item = st.sidebar.selectbox('Promocional', options = items)

        duracion = st.sidebar.slider('Duración  ', min_value= 10.0, max_value= 90.0, step = 10.0, value = 20.0 )

        genero = st.sidebar.selectbox('Genero del Programa',options =  generos)

        ciudad = st.sidebar.radio('Ciudad', options=['QUITO', 'GUAYAQUIL'])

        target = st.sidebar.selectbox('Target' , options =  targets )

        rating = st.sidebar.slider('Rating Esperado', min_value= 0.1, max_value= 20.0, step = 0.1, value = 0.8 )
                

        parametros = {
           'DURACION' : duracion,	
           'ITEM'	: item, 
           'GENERO'	: genero, 
           'CIUDAD'	: ciudad,
           'CAMPANIA': campania, 
           'RATING'	: rating, 
           'TARGET': target
        }
        return pd.DataFrame(parametros, index=[0])
    

    df = get_parametros()
    link = '[Dasboard](https://app.powerbi.com/reportEmbed?reportId=fc993574-f65b-4fd7-a4ba-624750afd5b4&autoAuth=true&ctid=e9763399-4de0-4078-a8dc-a6cb985b4841)'
    st.sidebar.markdown(link, unsafe_allow_html = True)

    st.dataframe(df, use_container_width = True)

    if st.button('Encontrar programa'):
        pr = clasificar (df)
        st.success( f" Mejor programa:  {pr}" )
        dtf = getTopTen(pr)     
        st.bar_chart( dtf )
    
if __name__ == '__main__': 
    main()
