import streamlit as st
from PIL import Image   #pillow package que ya está instalado

with st.expander("Start Camara"):
    #start camera
    camara_image = st.camera_input("Camara")  #con esto aparece la camara y puedes tomar fotos.

uploaded_image = st.file_uploader("Upload and image")


if camara_image:
    # Create a pillow image instance
    img = Image.open(camara_image)

    #Convert the pillow image to grayscale
    gray_img = img.convert("L")  #convierte a gray scale

    #Render the gray on the webpage
    st.image(gray_img)


if uploaded_image:
    img = Image.open(uploaded_image)
    gray_img = img.convert("L")
    st.image(gray_img)