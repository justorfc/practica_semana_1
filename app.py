 #Importamos la librería streamlit y la renombramos como 'st' por convención
import streamlit as st

# Título de la aplicación
st.title("Mi Primera App de Estadística con Streamlit y Python  ")

# Encabezado de la aplicación
st.header("Semana1: Fundamentos y Entorno de Trabajo")

# Descripción de la aplicación
st.write("""
Esta aplicación está diseñada para ayudarte a comprender los conceptos básicos de estadística utilizando Python y Streamlit. Aquí encontrarás ejemplos prácticos y visualizaciones interactivas para facilitar tu aprendizaje.
""")

# Sección de contenido
st.subheader("1. Justificación de Herramientas")
st.info("""
 **VSCode + Git/GitHub:** Para un desarrollo ordenado y colaborativo.
        
 **Python+Streamlit:** Para analizar datos y comunicar resultados de forma interactiva.
""")

 #st.text_input() crea un campo de texto para que el usuario ingrese información
nombre = st.text_input("Ingresa tu nombre:")

# Usamos una estructura condicional para reaccionar a la entrada del usuario
if nombre:
    st.success(f"¡Hola, {nombre}! Bienvenido a la aplicación de estadística.")  
else:
    st.warning("Por favor, ingresa tu nombre para continuar.")
    