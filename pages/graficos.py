import streamlit as st
import pandas as pd
#import src.manage_data as dat
#import plotly.express as px
#import codecs
#import streamlit.components.v1 as components
import plotly.graph_objects as go
import plotly.figure_factory as ff




def app():
    grafico1 = pd.read_csv("data/redi_games.csv")




    #c = dat.grafico(person)
    #st.write("""
    #Participación en GAMES por países: 
    #""", person)
    #fig = px.line(participacion_por_paises, y="polarity")
    #st.plotly_chart(fig)


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
        title_text = 'Players per Country',
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
).update_layout(width=900,height=800) 
 

# Mostramos la figura generada
    

    st.plotly_chart(fig)