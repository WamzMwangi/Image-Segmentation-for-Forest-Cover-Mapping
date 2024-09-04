import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array, load_img
from PIL import Image
import numpy as np

#load ML model
model=load_model(r'C:\Users\Admin\Desktop\Capstone_project_research\hypertuned_unet_model.keras')

#function to preprocess the uploaded image
def image_processor(uploaded_image):
    img=load_img(uploaded_image,target_size=(256,256))
    img=img_to_array(img)/255.0
    img = np.expand_dims(img, axis=0)
    return img

#set title of the landing page
if 'page' not in st.session_state:
    st.session_state.page='landing'

if st.session_state.page=='landing':

    st.title("🌳 Forest Cover Mapping with Computer Vision")
    st.write("""
          Explore nature from above with advanced machine learning and computer vision. This app transforms satellite images 
         into detailed forest cover maps using semantic segmentation. So to all nature lovers and enthusiasts, this app provides
         an effortless way for you to analyze and visualize forest landscapes!.
         **Simply upload a satellite image and get accurate forest cover maps in just a click of a button!**
         """)
    landing_page_image=Image.open(r'C:\Users\Admin\Desktop\Capstone_project_research\forest_label.webp')
    st.image(landing_page_image,caption=None,use_column_width='auto')
    if st.button('Get Started Here',type='primary'):
        st.session_state.page='upload'
elif st.session_state.page=='upload':
    uploaded_image=st.file_uploader("Upload your satellite image here")
    if uploaded_image is not None:
        image=Image.open(uploaded_image)
        st.image(image,caption='Raw Satellite image')
        if st.button("Run model",type='primary'):
            img_array=image_processor(uploaded_image)
            prediction=model.predict(img_array)
            st.image(prediction)

