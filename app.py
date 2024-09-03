import streamlit as st

#create the overall layout of the landing page

st.title("Rasilimali")
st.header("Forest Cover Mapping with Computer Vision")

st.write("""
Welcome Nature Lovers and enthusiasts to Rasilimali. An apllication that let's you create forest cover maps 
         from satellite images at the click of a button using the latest advancements in Tech! Have fun exploring!
         """)

#uploading images
uploaded_image=st.file_uploader("Please upload your satellite image here")
 if uploaded_image in not None:
    image=Image.open(uploaded_image)
    st.image(image,caption="Satellite image", use_column_width=True)


#adding a 'map forest cover' button
