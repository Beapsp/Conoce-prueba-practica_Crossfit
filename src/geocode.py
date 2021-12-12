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




def cleaning_rest(direccion,radio):
    """
    Esta función me transforma un json en df.
    Args: ciudad (string)
          radio(int)
    Return: df con las características principales de los restaurantes.
    """
    res=Google_Api_request(direccion,radio)
    dicc={"Name":[], "Rating":[],"Dirección":[],"Latitud":[], "Longitud":[]}
    for i in range (len(res['results'])):
        dicc['Name'].append(res['results'][i]['name']) #name
        dicc['Rating'].append(res['results'][i]['rating']) #rating
        dicc['Dirección'].append(res['results'][i]['vicinity']) #dirección
        dicc['Latitud'].append(res['results'][i]['geometry']['location']['lat']) #lat
        dicc['Longitud'].append(res['results'][i]['geometry']['location']['lng']) #lng
    restaurants=pd.DataFrame(dicc)
    return restaurants
