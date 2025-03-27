import pandas as pd
import plotly.express as px
import streamlit as st

df = pd.read_csv('vehicles_us.csv')

# Encabezado de la aplicación
st.header("Análisis Exploratorio de Datos de Vehículos")
# Botón para construir un histograma
if st.button("Construir Histograma"):
    st.write("Histograma de la columna 'odometer'")
    if 'odometer' in df.columns:
        fig = px.histogram(df, x='odometer', title='Histograma de Odómetro')
    else:
        fig = px.histogram(df, x=df.columns[0], title=f'Histograma de {df.columns[0]}')
    st.plotly_chart(fig, use_container_width=True)

# Botón para construir un gráfico de dispersión
if st.button("Construir Scatter Plot"):
    st.write("Gráfico de dispersión: Precio vs Odómetro")
    if 'odometer' in df.columns and 'price' in df.columns:
        fig2 = px.scatter(df, x='odometer', y='price', title='Precio vs Odómetro')
        st.plotly_chart(fig2, use_container_width=True)
    else:
        st.write("Las columnas necesarias para el scatter plot no están disponibles.")