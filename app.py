import streamlit as st
from model import predict

st.markdown('<style>body{text-align: center;}</style>', unsafe_allow_html=True)
st.title('Krishi Unnati')
st.header('A plant and crop disease detection app')
st.text('')
img = st.file_uploader(label='Upload image (PNG, JPG or JPEG)', type=['png', 'jpg', 'jpeg'])
if img is not None:
    st.image(image=img.read(), caption='Uploaded image')
    predict_button = st.button(label='Predict')
    if predict_button:
        prediction_class, prediction_probability = predict(img)
        st.text('')
        st.subheader('Prediction')
        st.info(f'Classification: {prediction_class}, Probability: {prediction_probability}%')
