from geopy.geocoders import Nominatim
from geopy.distance import geodesic 
import json
from bson.json_util import dumps
import pandas as pd
import requests
import os
from dotenv import load_dotenv
import sys
sys.path.append('../')

import folium
from folium import Choropleth, Circle, Marker, Icon, Map
from folium.plugins import HeatMap, MarkerCluster

load_dotenv()

def get_coordenadas(direccion):
    """
    Esta función saca las coordenadas de la ciudad que le pases.
    Args: una dirección/ciudad (string).
    Return: Las coordeandas de la ciudad que le paso como argumento (latitud y longitud).
    """
    geolocator = Nominatim(user_agent="Bea")
    location = geolocator.geocode(query=direccion, exactly_one=True,timeout=200)
    return location[1]



def Google_Api_request(direccion,radio):
    """
    Esta función me devuelve un json con todos los box de crossfit que estén en dicho radio de la ciudad seleccionada.
    Args: dirección/ciudad (string)
          radio(int)
    Return: json con todos los box de crossfit que estén en dicho radio de la ciudad seleccionada.
    """
    coord=get_coordenadas(direccion)
    url= "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    parameters={"key": os.getenv("API_KEY"),
            "location": f'{coord[0]}, {coord[1]}',
            "radius": radio,
            "keyword":"Crossfit"
           }
    response=requests.get(url,params=parameters)
    res=response.json()
    return res




def cleaning_box(direccion,radio):
    """
    Esta función me transforma un json en df.
    Args: dirección/ciudad (string)
          radio(int)
    Return: df con las características principales de los box de crossfit.
    """
    res=Google_Api_request(direccion,radio)
    dicc={"Name":[], "Rating":[],"Dirección":[],"Latitud":[], "Longitud":[]}
    for i in range (len(res['results'])):
        dicc['Name'].append(res['results'][i]['name']) #name
        dicc['Rating'].append(res['results'][i]['rating']) #rating
        dicc['Dirección'].append(res['results'][i]['vicinity']) #dirección
        dicc['Latitud'].append(res['results'][i]['geometry']['location']['lat']) #lat
        dicc['Longitud'].append(res['results'][i]['geometry']['location']['lng']) #lng
        
    box_crossfit=pd.DataFrame(dicc)
    return box_crossfit


def map(direccion,radio):
    icon_url= 'https://img2.freepng.es/20180703/oyo/kisspng-crossfit-791-konse-endurance-business-crossfit-eixample-5b3b23f92b1fe9.1553062215306024891767.jpg'
    icon_url2 ='https://e7.pngegg.com/pngimages/758/190/png-clipart-adobe-illustrator-sport-exercise-equipment-exercise-dumbbells-blue-fitness.png'
    icon_url3 = 'https://thumbs.dreamstime.com/b/pesas-de-gimnasia-rojas-5073020.jpg'
    boxes=cleaning_box(direccion, radio)
    coord=list(get_coordenadas(direccion))
    map_rest = Map(location = coord, zoom_start = 15)
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
            
        mark = Marker(**dicc, icon=icono)
        mark.add_to(map_rest)
    return map_rest