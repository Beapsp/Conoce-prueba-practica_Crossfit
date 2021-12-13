import streamlit as st
import pandas as pd
import sys
sys.path.append('../')


    

def app():
    data = pd.read_csv("data/movimientos_video.csv")

    #st.write("Hola")
    #movimiento = st.selectbox("Elige un movimiento",["hola", "otro", "pressjwdgoiwh", "junkdasgkwhjdgoi"])
    #st.write(movimiento)
    #df_mov_video = pd.read_csv("../data/movimientos_video.csv")
    #data = pd.read_csv("../data/movimientos_video.csv")
    st.dataframe(data)
   

    size = data.name.unique()
    input_size = st.selectbox("¿Qué movimiento quieres conocer?", size)

   