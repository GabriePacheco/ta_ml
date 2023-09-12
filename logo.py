import streamlit as st  

def add_logo():
    st.markdown(
        """
        <style>
            [data-testid="stSidebarNav"] {
                background-image: url(https://www.teleamazonas.com/wp-content/uploads/2023/09/identidadWEB.png);
                background-repeat: no-repeat;
                padding-top: 10px;
                background-size: cover;
                background-opacity: 0.5;
                position: relative;
            }
            [data-testid="stSidebarNav"]::before {
                content: " ";
                position: absolute;
                width: 100%;
                height: 25%;                                     
                top: 25%;
                background-image: url(https://ister.edu.ec/wp-content/uploads/2021/01/RU-LOGO-COMPLETO.webp);
                background-repeat: no-repeat;
                padding-top: 15px;
                background-size: 90%;
            }

         
                     
        </style>
        """,
        unsafe_allow_html=True,
    )
st.set_page_config( page_title= "Encontrar Programa", page_icon="Home")

