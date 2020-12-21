from django.shortcuts import render
from .serializers import PostSerializer
from .models import Post
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
import base64
import cv2
from tensorflow import keras
from keras.preprocessing.image import load_img, img_to_array
import numpy as np
import json

# Create your views here.
IMAGE_SIZE = 224
classes=['Apple___Apple_scab',
 'Apple___Black_rot',
 'Apple___Cedar_apple_rust',
 'Apple___healthy',
 'Background_without_leaves',
 'Blueberry___healthy',
 'Cherry___Powdery_mildew',
 'Cherry___healthy',
 'Corn___Cercospora_leaf_spot Gray_leaf_spot',
 'Corn___Common_rust',
 'Corn___Northern_Leaf_Blight',
 'Corn___healthy',
 'Grape___Black_rot',
 'Grape___Esca_(Black_Measles)',
 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)',
 'Grape___healthy',
 'Orange___Haunglongbing_(Citrus_greening)',
 'Peach___Bacterial_spot',
 'Peach___healthy',
 'Pepper,_bell___Bacterial_spot',
 'Pepper,_bell___healthy',
 'Potato___Early_blight',
 'Potato___Late_blight',
 'Potato___healthy',
 'Raspberry___healthy',
 'Soybean___healthy',
 'Squash___Powdery_mildew',
 'Strawberry___Leaf_scorch',
 'Strawberry___healthy',
 'Tomato___Bacterial_spot',
 'Tomato___Early_blight',
 'Tomato___Late_blight',
 'Tomato___Leaf_Mold',
 'Tomato___Septoria_leaf_spot',
 'Tomato___Spider_mites Two-spotted_spider_mite',
 'Tomato___Target_Spot',
 'Tomato___Tomato_Yellow_Leaf_Curl_Virus',
 'Tomato___Tomato_mosaic_virus',
 'Tomato___healthy']

def prepare(img_path):
    with open('Cure.json', encoding='utf-8') as fl1:
        data_dict = json.load(fl1)
    print("Data Dictionary == ",data_dict)    
    model = keras.models.load_model('./model.h5')
    img = cv2.imread(img_path) 
    img = cv2.resize(img, (IMAGE_SIZE, IMAGE_SIZE))
    img = np.reshape(img, [1, IMAGE_SIZE, IMAGE_SIZE, 3])
    img = img/255.
    class_confidence = model.predict(x=img) 
    class_index = int(np.argmax(class_confidence, axis=1)) 
    class_confidence = np.squeeze(class_confidence)
    pro=class_confidence[class_index] * 100
    print("classsssssssssss",classes[class_index]);
    return {'probability': pro, 'disease_name': classes[class_index] , 'disease_details': data_dict[class_index]}


class PostView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        posts_serializer = PostSerializer(data=request.data)
        print('sid-+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+')
        if posts_serializer.is_valid():
            posts_serializer.save()
            string = posts_serializer.data['content']
            imgData = base64.b64decode(string)
            filename = "ryu.jpg"
            with open(filename, 'wb') as fl:
                fl.write(imgData)
            som = prepare("ryu.jpg")
            #return Response(posts_serializer.data, status=status.HTTP_201_CREATED)
            return Response(som, status=status.HTTP_201_CREATED)
        else:
            print('error', posts_serializer.errors)
            return Response(posts_serializer.errors, status=status.HTTP_400_BAD_REQUEST)