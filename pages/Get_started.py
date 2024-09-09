import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array, load_img
from PIL import Image
import numpy as np

st.title('Semantic segmentation of satellite images using a U-net model')
st.write("""
This app utilizes semantic segmentation to delineate between forested and unforested land solely from satellite images.
         Semantic segmentation is a computer vision technique that assigns each pixel in an image into a class. 
         This allows us to produce more accurate forest maps and at greater speeds.""")

#load ML model
model=load_model(r'C:\Users\Admin\Desktop\Capstone_project_research\hypertuned_unet_model.keras')

#function to preprocess the uploaded image
def image_processor(uploaded_image):
    img=load_img(uploaded_image,target_size=(256,256))
    img=img_to_array(img)/255.0
    img = np.expand_dims(img, axis=0)
    return img

uploaded_image=st.file_uploader("Upload your satellite image here")
if uploaded_image is not None:
    image=Image.open(uploaded_image)
    st.image(image,caption='Raw Satellite image')
    if st.button("Run model",type='primary'):
        img_array=image_processor(uploaded_image)
        predicted_image=model.predict(img_array)
        st.image(predicted_image,caption='Mapped Forest Cover')