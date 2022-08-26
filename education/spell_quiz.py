from voice_recognition import *
from speak import *
import pandas as pd

df = pd.read_csv('dataset.csv')

df=df.sample(3)
speak("Welcome to spell quiz")
def quiz():
    for word in df['word']:
        speak("spell    . ")
        speak(word)
        flag=True
        while flag:
            ans=takeCommand()
            print(ans)
            # for i in word:
            #     ans=takeCommand()
            #     if ans==i: continue
            #     else:
            #         speak("Wrong")
            #         speak("do you want to re try")
            #         ans2=takeCommand()
            #         if 'yes' in ans2 or 'sure' in ans2 or 'retry' in ans2 or 're try' in ans2:
            #             flag=True
            #             continue
            #         else:
            #             flag=False
            #             break

quiz()

