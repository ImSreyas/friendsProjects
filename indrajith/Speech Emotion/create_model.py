import librosa
import soundfile
import os, glob, pickle
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from utils import load_data

#Options: Neutral, Calm, Happy, Sad, Angry, Fearful, Disgusted, Surprised
emotions_to_observe = ['Neutral', 'Happy','Angry']

#Load the data and extract features for each sound file from the RAVDESS dataset
# x,y=load_data("/home/moe/Desktop/projects/sound_freq/speech_emotion_app/speech_data/Actor_*/*.wav",
# emotions_to_observe)
x,y=load_data("C:/Users/USER/Desktop/PMG/PMG_Final/Speech Emotion/Actor_*/*.wav",
emotions_to_observe)

# C:\Users\USER\Desktop\PMG\PMG_Final\Speech Emotion
#Initialize multilayer perceptron model (alpha: L2 regularization parameter,
# bath_size: Size of minibatches for stochastic optimizers deafault --> 200)
# max iter: Maximum number of iterations. The solver iterates until convergence or this number of iterations.
model=MLPClassifier(batch_size=256, max_iter=500)

#split data into training and testing
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=24)

#fit the model
model.fit(x_train,y_train)

#predict the emotion using testing features
y_pred=model.predict(x_test)

#calculate accuracy of predictions
accuracy=accuracy_score(y_true=y_test, y_pred=y_pred)
print(f"Accuracy of Model {accuracy*100}")
print(f"Accuracy of Random Guessing {1/len(emotions_to_observe)*100}")

# Save model into .model binary to use in application
pickle.dump(model, open("model.model", "wb"))
