import streamlit as st
from streamlit_folium import folium_static
import streamlit.components.v1 as components
import codecs
import folium
import requests

import folium
from folium import Choropleth, Circle, Marker, Icon, Map
from folium.plugins import HeatMap, MarkerCluster
import sys
sys.path.append('../')
import src.geocode as gc

def map(direccion,radio):
        icon_url= 'https://img2.freepng.es/20180703/oyo/kisspng-crossfit-791-konse-endurance-business-crossfit-eixample-5b3b23f92b1fe9.1553062215306024891767.jpg'
        icon_url2 ='https://e7.pngegg.com/pngimages/758/190/png-clipart-adobe-illustrator-sport-exercise-equipment-exercise-dumbbells-blue-fitness.png'
        icon_url3 = 'https://thumbs.dreamstime.com/b/pesas-de-gimnasia-rojas-5073020.jpg'
        boxes=gc.cleaning_box(direccion, radio)
        coord=list(gc.get_coordenadas(direccion))
        map_rest = folium.Map(location = coord, zoom_start = 15)
        for i,row in boxes.iterrows():
            dicc = {"location": [row["Latitud"], row["Longitud"]], "tooltip": row["Name"]}
            
            if row["Rating"] >=3.8 :
                icono = folium.features.CustomIcon(icon_url, icon_size=(30,30))
                #icono = Icon(color = "blue",
                            #prefix="fa",
                            #icon=folium.features.CustomIcon(icon_url, icon_size=(15,15)), 
                            #icon_color="black"
                #)
            elif row["Rating"] < 3.8 and row["Rating"]>= 2.0 :
                icono = folium.features.CustomIcon(icon_url2, icon_size=(30,30))
                #icono = Icon(color = "purple",
                            #prefix="fa",
                            #icon="hand-o-right",
                            #icon_color="black")
                
            elif row["Rating"] < 2.0 :
                icono = folium.features.CustomIcon(icon_url3, icon_size=(30,30))
                #icono = Icon(color = "red",
                            #prefix="fa",
                            #icon="thumbs-o-down",
                            #icon_color="black")
                
            mark = folium.Marker(**dicc, icon=icono)
            mark.add_to(map_rest)
        return map_rest

def app():
    def map(direccion,radio):
        icon_url= 'https://img2.freepng.es/20180703/oyo/kisspng-crossfit-791-konse-endurance-business-crossfit-eixample-5b3b23f92b1fe9.1553062215306024891767.jpg'
        icon_url2 ='https://e7.pngegg.com/pngimages/758/190/png-clipart-adobe-illustrator-sport-exercise-equipment-exercise-dumbbells-blue-fitness.png'
        icon_url3 = 'https://thumbs.dreamstime.com/b/pesas-de-gimnasia-rojas-5073020.jpg'
        boxes=gc.cleaning_box(direccion, radio)
        coord=list(gc.get_coordenadas(direccion))
        map_rest = folium.Map(location = coord, zoom_start = 15)
        for i,row in boxes.iterrows():
            dicc = {"location": [row["Latitud"], row["Longitud"]], "tooltip": row["Name"]}
            
            if row["Rating"] >=3.8 :
                icono = folium.features.CustomIcon(icon_url, icon_size=(30,30))
                #icono = Icon(color = "blue",
                            #prefix="fa",
                            #icon=folium.features.CustomIcon(icon_url, icon_size=(15,15)), 
                            #icon_color="black"
                #)
            elif row["Rating"] < 3.8 and row["Rating"]>= 2.0 :
                icono = folium.features.CustomIcon(icon_url2, icon_size=(30,30))
                #icono = Icon(color = "purple",
                            #prefix="fa",
                            #icon="hand-o-right",
                            #icon_color="black")
                
            elif row["Rating"] < 2.0 :
                icono = folium.features.CustomIcon(icon_url3, icon_size=(30,30))
                #icono = Icon(color = "red",
                            #prefix="fa",
                            #icon="thumbs-o-down",
                            #icon_color="black")
                
            mark = folium.Marker(**dicc, icon=icono)
            mark.add_to(map_rest)
        return map_rest

    st.write("""
    ### Busca tu Box

    """)
    default_value_goes_here = "Calle Campomanes 10, Madrid"
    user_input_dire = st.text_input("Introduce dirección", default_value_goes_here)
    default_value_radio = 10000
    user_input_radio = st.text_input("Introduce radio", default_value_radio)

    #data = requests.get(f"https://geocode.xyz/{user_input}?json=1").json()
    #latlon = [data["latt"],data["longt"]]
    
    
    folium_static(map(user_input_dire, user_input_radio))


    st.write("""
    ### Ya no tienes excusas
    """)

    #f=codecs.open("data/mapa.html", 'r')
    #mapa = f.read()

    #components.html(mapa,height=550,scrolling=True)


    

    #map_1 = folium.Map(location = latlon, zoom_start=15)
    #mark.add_to(map_1)

    #folium_static(map_1)