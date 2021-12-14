from re import T
import streamlit as st
from PIL import Image
from multipage import MultiPage
from pages import home
from pages import movimientos
from pages import graficos
from pages import ubicacion

app = MultiPage()


app.add_page("Index", home.app)
app.add_page("Movimientos", movimientos.app)
app.add_page("Graficos", graficos.app)
app.add_page("Mapas",ubicacion.app)


app.run()