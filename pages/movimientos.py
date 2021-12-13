import streamlit as st
import pandas as pd
import sys
sys.path.append('../')




def app():
    st.write("Hola")
    movimiento = st.selectbox("Elige un movimiento",["hola", "otro", "pressjwdgoiwh", "junkdasgkwhjdgoi"])
    st.write(movimiento)
    df_mov_video = pd.read_csv("../data/movimientos_video.csv",encoding = "ISO-8859-1")
   