import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import keras
import json
import pickle
from tensorflow.keras.applications.inception_v3 import InceptionV3, preprocess_input, decode_predictions
from tensorflow.keras.utils import load_img, img_to_array
from keras.preprocessing import image
from keras.models import Model, load_model
from keras_preprocessing.sequence import pad_sequences
from tensorflow.keras.utils import to_categorical
from keras.layers import Input, Dense, Dropout, Embedding, LSTM
from keras.applications import imagenet_utils
#from keras.layers.merge import add

import collections
import random
from PIL import Image
# for voice
from playsound import playsound
from gtts import gTTS
import os
import time
import cv2



# Get the InceptionV3 model trained on imagenet data
model_inception = InceptionV3(weights='imagenet',input_shape=(299,299,3))
model_inception.make_predict_function()



def preprocess_image(img):
    # Convert all the images to size 299x299 as expected by the
    # inception v3 model
    img = load_img(img, target_size=(299, 299))
    # Convert PIL image to numpy array of 3-dimensions
    x = img_to_array(img)
    # Add one more dimension
    x = np.expand_dims(x, axis=0)
    # preprocess images using preprocess_input() from inception module
    x = preprocess_input(x)
    return x



def encode_image(img):
    img = preprocess_image(img)
    feature_vector = model_inception.predict(img)
    #decode the prediction
    actual_prediction = imagenet_utils.decode_predictions(feature_vector)
    return actual_prediction


def voice(myText):

    # Language we want to use 
    language = 'en'

    output = gTTS(text=myText, lang=language, slow=False)
    t=time.time()
    nm="output"+str(t)+".mp3"
    output.save(nm)
    playsound(nm)




import cv2
import time

def FrameCapture(nm):
    x = encode_image(nm)
    s = x[0][0][1]
    value = s[0]+"  for " + s
    print(value)
    voice(value)
    return

