import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array, load_img
from PIL import Image
import numpy as np
import cv2
import os


st.title('Semantic segmentation of satellite images using a U-net model')
st.write("""
This app utilizes semantic segmentation to delineate between forested and unforested land solely from satellite images.
         Semantic segmentation is a computer vision technique that assigns each pixel in an image into a class.
         This allows us to produce more accurate forest maps and at greater speeds.""")


@st.cache_resource
def load_model_once():
    # Define the path to the model file
    model_path = os.path.join(
        os.path.expanduser("~"),  # User's home directory
        "Desktop",
        "Image-Segmentation-for-Forest-Cover-Mapping",
        "hypertuned_unet_model.keras"
    )
    # Ensure the model file exists
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file not found at {model_path}")

    # Load and return the model
    return load_model(model_path)

# Load the model
model = load_model_once()

#function to preprocess the uploaded image
def image_processor(uploaded_image):
    img=load_img(uploaded_image,target_size=(256,256))
    img=img_to_array(img)/255.0
    img = np.expand_dims(img, axis=0)
    return img

def forested_area_estimation(threshold_mask):
    forested_area=np.sum(threshold_mask)*30*30
    forested_area=forested_area/1000000
    return forested_area

#user input section
col1,col2=st.columns(2)
uploaded_image=st.file_uploader("Upload your satellite image here")
if uploaded_image is not None:
    image=Image.open(uploaded_image)
    with col1:
        st.image(image,caption='Raw Satellite image')
    if st.button("Run model",type='primary'):
        img_array=image_processor(uploaded_image)
        predicted_image=model.predict(img_array)
        predicted_image = np.squeeze(predicted_image)
        predicted_mask_uint8 = (predicted_image * 255).astype(np.uint8)
        ret,threshold_image=cv2.threshold(predicted_mask_uint8,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        with col2:
            st.image(threshold_image,caption='Mapped Forest Cover')
            forest_area=forested_area_estimation(threshold_image)
            st.write(f"Forested Area: {forest_area:.2f} km²")
        

