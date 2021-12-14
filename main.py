from re import T
import streamlit as st
from PIL import Image
from multipage import MultiPage
from pages import home
from pages import movimientos
from pages import graficos
from pages import ubicacion

app = MultiPage()


app.add_page("Comenzamos", home.app)
app.add_page("Gráficos", graficos.app)
app.add_page("Movimientos", movimientos.app)
app.add_page("Ubicación",ubicacion.app)


app.run()