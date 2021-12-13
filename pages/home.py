import streamlit as st
from PIL import Image
#import streamlit.components.v1 as components
#import codecs
#gif = 'https://i.pinimg.com/originals/74/65/1d/74651dc9fc122bf6847c597d97da7ed0.gif'

def app():

    st.write("""
    # Conoce, prueba, practica CROSSFIT
    
    """)
    portada = Image.open("imagenes/image5.jpg")
    #portada = Image.open(gif)
    st.image(portada, use_column_width=True)
    #f=codecs.open("data/pedrito.html", 'r')
    #pedro = f.read()

    #components.html(pedro,height=550,scrolling=True)


