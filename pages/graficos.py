import streamlit as st
import pandas as pd
from PIL import Image
#import src.manage_data as dat
#import plotly.express as px
#import codecs
#import streamlit.components.v1 as components
import plotly.graph_objects as go
import plotly.figure_factory as ff




def app():
    size2 = ["Elige","Games","Open"]
    input_size = st.selectbox("¿Qué competición quieres analizar?", size2)
    grafico1 = pd.read_csv("data/redi_games.csv")
    grafico2 = pd.read_csv("data/top5_w_open.csv")

        #st.markdown("![Alt Text](https://monophy.com/media/3osBLvoR8tGE6OI5os/monophy.gif)") importar gif sin size
    #st.image(
                #"https://monophy.com/media/3osBLvoR8tGE6OI5os/monophy.gif", 
                #width=700,
            #)
    
    
    if input_size == "Elige":
        st.image(
                "https://monophy.com/media/3osBLvoR8tGE6OI5os/monophy.gif", 
                width=700,
            ),

    
        
    elif input_size == "Games":

        st.write("""
        # Participación en GAMES por países 
        #""")

        fig = go.Figure(go.Choropleth(
            locations = grafico1['countryoforiginname'],
            locationmode = "country names",
            z = grafico1['competitorname'],
            text = grafico1['countryoforiginname'],
            colorscale = 'magma',
            autocolorscale=False,
            reversescale=True,
            marker_line_color='#efefef',
            marker_line_width=0.1,
            #colorbar_ticksuffix = '%',
            colorbar_title = 'Number competitors',
            )
        )
        
        # Establecemos las características del título y la apariencia del mapa base
        fig.update_layout(
            title_text = 'GAMES',
            showlegend = False,
            geo = dict(
                scope='world',
                resolution=50,
                projection_type='miller',
                showcoastlines=True,
                showocean=True,
                showcountries=True,
                oceancolor='#eaeaea',
                lakecolor='#eaeaea',
                coastlinecolor='#dadada'
            )
        ).update_layout(width=800,height=1000)
 
    

        st.plotly_chart(fig),


    else:


    #c = dat.grafico(person)
        st.write("""
        # Participación en OPEN 
        #""")
        #fig = px.line(participacion_por_paises, y="polarity")
        #st.plotly_chart(fig)