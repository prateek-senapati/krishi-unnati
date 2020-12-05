import streamlit as st
from model import predict

st.title('Krishi Unnati')
st.subheader('A plant and crop disease detection app')
img = st.file_uploader(label='Upload image (PNG, JPG or JPEG)', type=['png', 'jpg', 'jpeg'])
if img is not None:
    st.image(image=img.read(), caption='Uploaded image')
    predict_button = st.button(label='Predict')
    if predict_button:
        prediction_class, prediction_probability = predict(img)
        st.text(f'Prediction: {prediction_class}')
        st.text(f'Prediction probability: {prediction_probability}%')
