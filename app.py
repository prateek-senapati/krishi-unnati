from tensorflow.keras.models import load_model, Model
import numpy as np
import tensorflow as tf
import streamlit as st
from PIL import Image
from keras.preprocessing.image import load_img, img_to_array
from model import predict
import keras

# App development
st.title('Krishi Unnati')
st.subheader('A plant and crop disease detection app')
img = st.file_uploader(label='Upload image (PNG, JPG or JPEG)', type=['png', 'jpg', 'jpeg'])
if img is not None:
    img = Image.open(img)
    st.image(image=img, caption='Uploaded image')
    predict_button = st.button(label='Predict')
    if predict_button:
        prediction_class, prediction_probability = predict(img)
        st.text(f'Prediction: {prediction_class}')
        st.text(f'Prediction probability: {prediction_probability}%')
