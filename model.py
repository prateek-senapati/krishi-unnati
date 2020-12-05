from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image
from keras.preprocessing.image import load_img, img_to_array

def predict(img):
    IMAGE_SIZE = 224
    classes = ['Apple - Apple scab', 'Apple - Black rot',
    'Apple - Cedar apple rust', 'Apple - healthy', 'Background without leaves',
    'Blueberry - healthy', 'Cherry - Powdery mildew', 'Cherry - healthy',
    'Corn - Cercospora leaf spot Gray leaf spot', 'Corn - Common rust',
    'Corn - Northern Leaf Blight', 'Corn - healthy', 'Grape - Black rot',
    'Grape - Esca (Black Measles)', 'Grape - Leaf blight (Isariopsis Leaf Spot)',
    'Grape - healthy', 'Orange - Haunglongbing (Citrus greening)',
    'Peach - Bacterial spot', 'Peach - healthy', 'Pepper, bell - Bacterial spot',
    'Pepper, bell - healthy', 'Potato - Early blight', 'Potato - Late blight',
    'Potato - healthy', 'Raspberry - healthy', 'Soybean - healthy',
    'Squash - Powdery mildew', 'Strawberry - Leaf scorch', 'Strawberry - healthy',
    'Tomato - Bacterial spot', 'Tomato - Early blight', 'Tomato - Late blight',
    'Tomato - Leaf Mold', 'Tomato - Septoria leaf spot',
    'Tomato - Spider mites Two-spotted spider mite', 'Tomato - Target Spot',
    'Tomato - Tomato Yellow Leaf Curl Virus', 'Tomato - Tomato mosaic virus',
    'Tomato - healthy']
    model_path = r'model'
    model = load_model(model_path)
    img = Image.open(img)
    img = img.resize((IMAGE_SIZE, IMAGE_SIZE))
    img = img_to_array(img)
    img = img.reshape((1, IMAGE_SIZE, IMAGE_SIZE, 3))
    img = img/255.
    class_probabilities = model.predict(x=img)
    class_probabilities = np.squeeze(class_probabilities)
    prediction_index = int(np.argmax(class_probabilities))
    prediction_class = classes[prediction_index]
    prediction_probability = class_probabilities[prediction_index] * 100
    prediction_probability = round(prediction_probability, 2)
    return prediction_class, prediction_probability
