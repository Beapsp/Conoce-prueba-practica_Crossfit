import streamlit as st
from PIL import Image
#import streamlit.components.v1 as components
#import codecs


def app():
    portada = Image.open("imagenes/image1.jpg")
    st.image(portada, use_column_width=True)
    st.write("""
    # Conoce, prueba, practica CROSSFIT
    
    
    """)
    #f=codecs.open("data/pedrito.html", 'r')
    #pedro = f.read()

    #components.html(pedro,height=550,scrolling=True)
