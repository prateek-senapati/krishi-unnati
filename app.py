from tensorflow.keras.models import load_model, Model
import cv2
import numpy as np
import tensorflow as tf

IMAGE_SIZE = 224
file_path = r'D:\krishi-unnati\model'
img_path = r'D:\krishi-unnati\images\apple_scab.JPG'
classes = [ 'Apple___Apple_scab', 'Apple___Black_rot',
 'Apple___Cedar_apple_rust', 'Apple___healthy', 'Background_without_leaves',
 'Blueberry___healthy', 'Cherry___Powdery_mildew', 'Cherry___healthy',
 'Corn___Cercospora_leaf_spot Gray_leaf_spot', 'Corn___Common_rust',
 'Corn___Northern_Leaf_Blight', 'Corn___healthy', 'Grape___Black_rot',
 'Grape___Esca_(Black_Measles)', 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)',
 'Grape___healthy', 'Orange___Haunglongbing_(Citrus_greening)',
 'Peach___Bacterial_spot', 'Peach___healthy', 'Pepper,_bell___Bacterial_spot',
 'Pepper,_bell___healthy', 'Potato___Early_blight', 'Potato___Late_blight',
 'Potato___healthy', 'Raspberry___healthy', 'Soybean___healthy',
 'Squash___Powdery_mildew', 'Strawberry___Leaf_scorch', 'Strawberry___healthy',
 'Tomato___Bacterial_spot', 'Tomato___Early_blight', 'Tomato___Late_blight',
 'Tomato___Leaf_Mold', 'Tomato___Septoria_leaf_spot',
 'Tomato___Spider_mites Two-spotted_spider_mite', 'Tomato___Target_Spot',
 'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 'Tomato___Tomato_mosaic_virus',
 'Tomato___healthy']

img = cv2.imread(img_path)
img = cv2.resize(img, (IMAGE_SIZE, IMAGE_SIZE))
img = np.reshape(img, [1, IMAGE_SIZE, IMAGE_SIZE, 3])
img = img/255.

class_confidences = model.predict(x=img)
class_confidences = np.squeeze(class_confidences)
prediction_index = int(np.argmax(class_confidences))
prediction_class = classes[prediction_index]
prediction_confidence = class_confidences[prediction_index] * 100
print(f'Prediction class: {prediction_class}')
print(f'Prediction confidence: {prediction_confidence}%')
