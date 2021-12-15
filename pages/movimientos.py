import streamlit as st
import pandas as pd
import sys
import codecs
import streamlit.components.v1 as components
sys.path.append('../')


    

def app():
    data = pd.read_csv("data/movimientos_video.csv")

    
    #st.dataframe(data)
   
    st.write("""
        ## ¿Qué movimiento quieres conocer? 
        #""")
        
    size = list(data.name.unique())
    size.insert(0,"Elige")
    input_size = st.selectbox("Elige", size)
    if input_size == "Elige":
        st.stop()
    df = data[data["name"]==input_size]

    movimiento = df["iframe"].values[0]
    components.html(movimiento, height=800)
