import streamlit as st
import pandas as pd
import plotly.express as px   

df = pd.read_csv(r"C:\Codigo\Proyecto Sprint 7\Proyecto-sprint-7\vehicles_us.csv")

# Info general
print("Shape:", df.shape)

st.header("Visualización de Datos: Anuncios de Coches en EE.UU.")

st.write(
    """
    Esta aplicación web te permite explorar un conjunto de datos de anuncios de venta de vehículos en Estados Unidos.  
    Aquí podrás:  
    - Visualizar histogramas del kilometraje y precios.  
    - Construir gráficos de dispersión para analizar la relación entre variables.  
    - Detectar tendencias y patrones en los datos.  

    Usa los botones de abajo para generar las visualizaciones de manera interactiva.
    """
)

# Valores nulos y duplicados
print("Valores nulos:\n", df.isna().sum())
print("Porcentaje de nulos:\n", (df.isna().mean() * 100).round(2))
print("Duplicados:", df.duplicated().sum())

# Conversión de tipos
df['date_posted'] = pd.to_datetime(df['date_posted'])
df['model_year'] = df['model_year'].astype('Int64')
df['cylinders'] = df['cylinders'].astype('Int64')
df['is_4wd'] = df['is_4wd'].astype('Int64')

car_data = df

# Botón para histograma
hist_button = st.button("Construir histograma")

if hist_button:
    st.write("Creación de un histograma para el odómetro de los coches")
    fig = px.histogram(car_data, x="odometer")   
    st.plotly_chart(fig, use_container_width=True)  


scatter_button = st.button("Construir gráfico de dispersión")

if scatter_button:
    st.write("Creación de un gráfico de dispersión (Precio vs Kilometraje)")
    fig = px.scatter(car_data, x="odometer", y="price", opacity=0.5,
                     title="Relación entre Precio y Kilometraje")
    st.plotly_chart(fig, use_container_width=True)