import pandas as pd
from speak import *

df = pd.read_csv('dataset.csv')

def dailyDict():
    df=df.sample(1)
    speak("Word of the day is ")
    for word in df['word']:
        speak(word)
        for i in word:
            speak(i)
        speak("I repeat")
        for i in word:
            speak(i)