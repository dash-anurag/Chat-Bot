import flask
from flask import Flask
from chatbotconfig import Config

app=Flask(__name__)
app.config.from_object(Config)

import keras
import nltk
import pickle
import json
from keras.models import load_model

from nltk.stem import WordNetLemmatizer
lemmatizer=WordNetLemmatizer()

model=load_model('model_codes/mymodel.h5')
intents = json.loads(open('model_codes/intents.json').read())
words = pickle.load(open('model_codes/words.pkl','rb'))
classes = pickle.load(open('model_codes/classes.pkl','rb'))


from chatbot import routes
