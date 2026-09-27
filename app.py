import streamlit as st


st.title("Mi primera app con Streamlit")
st.write("Una aplicación mínima hecha con Python y Streamlit.")

nombre = st.text_input("¿Cómo te llamas?")

if nombre:
    st.success(f"¡Hola, {nombre}!")