import streamlit as st  

def add_logo():
    st.set_page_config(
        page_title="Promos - Teleamazonas ",
        page_icon="chart_with_upwards_trend",
        layout="wide",
    )
    st.markdown(
        """
        <style>
            [data-testid="stSidebarNav"] {
                background-image: url(https://ister.edu.ec/wp-content/uploads/2021/01/RU-LOGO-COMPLETO.webp);
                background-repeat: no-repeat;
                background-size: 80%;
                background-position: 25% 15%;
                position: relative;
                
            }
            [data-testid="stSidebarNav"]::before {
                position: absolute;
                content: "  ";
                width: 100%;
                height: 100%;
                background-image: url(https://www.teleamazonas.com/wp-content/uploads/2023/09/identidadWEB.png);
                background-repeat: no-repeat;
                background-size: cover;
                z-index: -1;
                opacity: 0.40;
            }
        </style>
        """,
        unsafe_allow_html=True,

    )


