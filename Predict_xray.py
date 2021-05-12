#!/usr/bin/env python
# coding: utf-8

# In[5]:


from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image
from keras.models import Model, load_model
import numpy as np
import matplotlib.pyplot as plt
import keras
from keras.layers import *
from keras.models import *
from keras.preprocessing import image
from keras.models import Sequential


# In[6]:


model = load_model("model_a.h5")


# In[7]:


def xray(Image):
    img_path = Image
    img = image.load_img(Image, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_batch = np.expand_dims(img_array, axis=0)
    img_preprocessed = preprocess_input(img_batch)
    prediction = model.predict(img_preprocessed)
    if prediction==[[0.]]:
        result="  is Covid-19 Positive"
    else:
        result="  is Covid-19 Negative"
    return result


# In[ ]:





# In[ ]:




