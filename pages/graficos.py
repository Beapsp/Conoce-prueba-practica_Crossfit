import streamlit as st
import pandas as pd
from PIL import Image
#import src.manage_data as dat
#import plotly.express as px
#import codecs
#import streamlit.components.v1 as components
import plotly.graph_objects as go
import plotly.figure_factory as ff
import plotly.express as px




def app():
    
    st.write("""
        ## ¿Quieres saber un poco más?
        #""")
    
    size2 = ["Competición","Games","Open"]
    input_size = st.selectbox("Elige", size2)
    grafico1 = pd.read_csv("data/redi_games.csv")
    grafico2 = pd.read_csv("data/clean_games.csv")
    grafico5 = pd.read_csv("data/top5_w_open.csv")

        #st.markdown("![Alt Text](https://monophy.com/media/3osBLvoR8tGE6OI5os/monophy.gif)") importar gif sin size
    #st.image(
                #"https://monophy.com/media/3osBLvoR8tGE6OI5os/monophy.gif", 
                #width=700,
            #)
    
    
    if input_size == "Competición":
        st.image(
                "https://monophy.com/media/3osBLvoR8tGE6OI5os/monophy.gif", 
                width=700,
            ),

    
        
    elif input_size == "Games":

        st.write("""
        ## Participación en GAMES por países 
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
            title_text = 'LA MAYOR PARTICIPACIÓN SE DA EN EE.UU, CANADÁ, AUSTRALIA',
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
        ).update_layout(width=900,height=1000)
 
        st.plotly_chart(fig),



        st.write("""
        ## Media de edad participantes 
        ###### LA MEDIA DE EDAD GENERAL ES DE 33 AÑOS, MIENTRAS QUE LA MEDIANA ES DE 30 AÑOS""")
       
        fig3 = px.histogram(grafico2, x="age")
        fig3.add_vline(grafico2.age.median(), line_width=3, line_dash="dash", line_color="purple")
        fig3.add_vline(grafico2.age.mean(), line_width=3, line_dash="dash", line_color="green")
        st.plotly_chart(fig3),
        
        
        st.write("""
        ## Participación general Mujeres y Hombres 
        ###### LA DIFERENCIA DE PARTICIPACIÓN GENERAL ENTRE HOMBRES Y MUJERES ES MUY PEQUEÑA""")
        fig2 = px.histogram(grafico2, x="gender")
        fig2.update_layout(bargap=0.2)
        st.plotly_chart(fig2),


        st.write("""
        ## Participación por rangos de edad 
        ###### PARTICIPACIÓN HOMBRES > MUJER **SOLO** EN RANGO DE EDAD GENERAL""")
        fig4 = px.histogram(grafico2, x="division") #color="gender", barmode="group"
        fig4.update_layout(bargap=0.2)
        st.plotly_chart(fig4),


    else:


    #c = dat.grafico(person)
        st.write("""
        # Participación en OPEN 
        #""")
        #fig = px.line(participacion_por_paises, y="polarity")
        #st.plotly_chart(fig)