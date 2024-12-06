import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array, load_img
from PIL import Image
import numpy as np

st.set_page_config(page_title="Home page",page_icon=":deciduous_tree:",layout="centered")
st.title("🌳 Forest Cover Mapping with Computer Vision")
st.write("""
          Explore nature from above with advanced machine learning and computer vision. This app transforms satellite images
         into detailed forest cover maps using semantic segmentation. So to all nature lovers and enthusiasts, this app provides
         an effortless way for you to analyze and visualize forest landscapes!.


         **Simply upload a satellite image and get accurate forest cover maps in just a click of a button!**
         """)
landing_page_image=Image.open(r"C:\Users\Pula Advisors\Desktop\Image-Segmentation-for-Forest-Cover-Mapping\Results\forest_cover.jpeg")

st.image(landing_page_image,caption=None,width=800)
st.sidebar.success("Navigate App here")

