import subprocess
from unicodedata import category
import wolframalpha
import pyttsx3
import tkinter
import json
import random
import operator
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pyjokes
import feedparser
import smtplib
import ctypes
import time
import requests
import shutil
from twilio.rest import Client
from clint.textui import progress
from ecapture import ecapture as ec
from bs4 import BeautifulSoup
from urllib.request import urlopen
import vlc
from database import *
# from audioBook import *
from speak import *
from jobs import *
from datetime import datetime
import pytz
from datetime import date
import _main as fe
import webbrowser

def wishMe():
	hour = int(datetime.datetime.now().hour)
	if hour>= 0 and hour<12:
		speak("Good Morning Sir !")

	elif hour>= 12 and hour<18:
		speak("Good Afternoon Sir !")

	else:
		speak("Good Evening Sir !")

	assname =("Gods Eye 1 point o")
	speak("I am your Assistant")
	speak(assname)
	

def username(uname):
	speak("Welcome Mister")
	speak(uname)
	columns = shutil.get_terminal_size().columns
	
	print("#####################".center(columns))
	print("Welcome Mr.", uname.center(columns))
	print("#####################".center(columns))
	
	speak("How can i Help you, Sir")

def takeCommand():
	
	r = sr.Recognizer()
	
	with sr.Microphone() as source:
		
		print("Listening...")
		r.pause_threshold = 1
		audio = r.listen(source)

	try:
		print("Recognizing...")
		query = r.recognize_google(audio, language ='en-in')
		print(f"User said: {query}\n")

	except Exception as e:
		print(e)
		print("Unable to Recognize your voice.")
		return "None"
	
	return query


import requests    
 
def NewsFromBBC():
     
    # BBC news api
    # following query parameters are used
    # source, sortBy and apiKey
    query_params = {
      "source": "bbc-news",
      "sortBy": "top",
      "apiKey": "1cbef7fa1a6f485791a74d3159338379"
    }
    main_url = " https://newsapi.org/v1/articles"
 
    # fetching data in json format
    res = requests.get(main_url, params=query_params)
    open_bbc_page = res.json()
 
    # getting all articles in a string article
    article = open_bbc_page["articles"]
 
    # empty list which will
    # contain all trending news
    results = []
    speak("Top 10 haedlines on BBC are as follows")
    for ar in article:
        results.append(ar["title"])
         
    for i in range(len(results)):
        speak(results[i])
 

if __name__ == '__main__':
	clear = lambda: os.system('cls')
	
	# This Function will clean any
	# command before execution of this python file
	clear()
	# wishMe()
	usname="Apoorv"
	userID=1
	username(usname)
	
	while True:
		
		query = takeCommand().lower()
		
		if 'wikipedia' in query:
			speak('Searching Wikipedia...')
			query = query.replace("wikipedia", "")
			results = wikipedia.summary(query, sentences = 3)
			speak("According to Wikipedia")
			print(results)
			speak(results)
            
        

		elif 'music' in query or "play song" in query:
			speak("Here you go with music")
			# music_dir = "G:\\Song"
			music_dir = "Music"
			songs = os.listdir(music_dir)
			print(songs)
			random = os.startfile(os.path.join(music_dir, songs[0]))
		elif 'date' in query:
			today = date.today()
			speak(today)

		elif 'time' in query:
			timezone = pytz.timezone('Asia/Kolkata')
			now = datetime.now(tz = timezone)
			txt = now.strftime("%H:%M:%S")
			x = txt.split(":")
			if x[0][0]=='0': x[0]=str(x[1])
			if x[1][0]=='0': x[1]=str(x[2])
			txt=x[0]+" hour, "+x[1]+" minutes"
			speak(txt)
			print("date and time =", txt)	
		
		elif 'employement' in query or 'job' in query:
			jobsportal(userID)

		elif 'how are you' in query:
			speak("I am fine, Thank you")
			speak("How are you, Sir")

		elif 'fine' in query or "good" in query:
			speak("It's good to know that your fine")

		elif "what's your name" in query or "your name" in query:
			speak("My friends call me")
			speak("Gods Eye")
			print("My friends call me Gods Eye")
		elif 'courses' in query or 'admission' in query or 'course' in query or 'subscribe' in query:
			speak("do you want to apply for a new course or listen to already applied courses")
			ans=takeCommand()
			if 'new' in ans or 'apply' in ans:
				speak("here is the list of courses you can apply for")
				out=courses_available()
				for row in out:
					speak("title "+row[1])
					speak("description "+row[2])
					speak("do you want to subscribe to this course ?")
					ans=takeCommand()
					if 'yes' in ans or 'sure' in ans or 'yeah' in ans or 'subscribe' in ans or 'add' in ans or 'apply' in ans:
						speak("Successfully applied for this course")
						subscribe(userID, row[0])
						speak("do you want to know about other course or want to exit from this section")
						ans=takeCommand()
						if 'exit' in ans:
							break
					elif 'exit' in ans:
						speak("exiting this section")
						break
			else:
				speak("You have applied for the following courses")
				out=courses_applied(userID)
				for row in out:
					speak("title  "+row[0])
					speak("do you want to listen to this course")
					ans=takeCommand()
					if 'yes' in ans or 'sure' in ans or 'yeah' in ans or 'want to'in ans:
						filepath = os.path.join("courses/"+row[1],"1.mp3")
						src = os.path.abspath(filepath)
						p = vlc.MediaPlayer(src)
						p.play()
						ans=takeCommand()
						if 'stop' in ans:
							p.stop()
						elif 'exit' in ans:
							break
					speak("let me see another course in your course list")
				speak("No more courses available in your course list")
		elif 'audiobook' in query or 'audio' in query or 'audiobooks' in query:
			speak("we have following audiobooks")
			speak("Currently i am having audiobooks for N C E R T books only")
			speak("In which class you are in ?")
			ans=takeCommand()
			if '1' in ans or 'one' in ans or 'class 1' in ans:
				speak("sorry to inform you that i am not able to find any audio book for this class")
			elif '2' in ans or 'two' in ans or 'class 2' in ans:
				speak("sorry to inform you that i am not able to find any audio book for this class")
			elif '3' in ans or 'three' in ans or 'class 3' in ans:
				speak("sorry to inform you that i am not able to find any audio book for this class")
			elif '4' in ans or 'four' in ans or 'class 4' in ans:
				speak("sorry to inform you that i am not able to find any audio book for this class")
			elif '5' in ans or 'five' in ans or 'class 5' in ans:
				speak("sorry to inform you that i am not able to find any audio book for this class")
			elif '6' in ans or 'six' in ans or 'class 6' in ans:
				print("abcd")


		elif 'exit' in query or 'quit' in query or ' end ' in query:
			speak("Do you want to give feedback ?")
			ans=takeCommand()
			if 'yes' in ans or 'sure' in ans or 'yeah' in ans:
				speak("rate the application out of 5")
				ans=takeCommand()
				if '5 out of 5' in ans or '5' in ans or 'five' in ans:
					rating=5
				elif '4 out of 5' in ans or '4' in ans or 'four' in ans:
					rating=4
				elif '3 out of 5' in ans or '3' in ans or 'three' in ans:
					rating=3
				elif '2 out of 5' in ans or '2' in ans or 'two' in ans:
					rating=2
				elif '1 out of 5' in ans or '1' in ans or 'one' in ans:
					rating=1
				else:
					rating=0
				feedback(userID, rating)
				exit()
			elif 'no' in ans or "don't" in ans or "do not" in ans:
				speak("Thanks for giving me your time")
				exit()
			

		elif "who made you" in query or "who created you" in query:
			speak("I have been created by Team Vikngs")
			
		elif 'joke' in query or 'laugh' in query:
			speak(pyjokes.get_joke())
			
		elif "calculate" in query:
			app_id = "K53L7U-3PLH57R825"
			client = wolframalpha.Client(app_id)
			indx = query.lower().split().index('calculate')
			query = query.split()[indx + 1:]
			res = client.query(' '.join(query))
			answer = next(res.results).text
			print("The answer is " + answer)
			speak("The answer is " + answer)

		elif "why you came to world" in query:
			speak("To rule the world....ha ha")

		elif 'is love' in query:
			speak("It is 7th sense that destroy all other senses")

		elif "who are you" in query:
			speak("I am your virtual assistant")

		elif 'reason for you' in query:
			speak("I was created to help Visually impaired children ")

		elif 'news' in query:
			try:
				NewsFromBBC()
			except Exception as e:
				
				print(str(e))

		elif "Gods Eye" in query:
			
			wishMe()
			speak("Gods Eye 1 point o in your service Mister")
			speak(usname)

		elif "weather" in query:
			
			# Google Open weather website
			# to get API of Open weather
			api_key = "Api key"
			base_url = "http://api.openweathermap.org / data / 2.5 / weather?"
			speak(" City name ")
			print("City name : ")
			city_name = takeCommand()
			complete_url = base_url + "appid =" + api_key + "&q =" + city_name
			response = requests.get(complete_url)
			x = response.json()
			
			if x["code"] != "404":
				y = x["main"]
				current_temperature = y["temp"]
				current_pressure = y["pressure"]
				current_humidiy = y["humidity"]
				z = x["weather"]
				weather_description = z[0]["description"]
				print(" Temperature (in kelvin unit) = " +str(current_temperature)+"\n atmospheric pressure (in hPa unit) ="+str(current_pressure) +"\n humidity (in percentage) = " +str(current_humidiy) +"\n description = " +str(weather_description))
			
			else:
				speak(" City Not Found ")
			
		elif "message" in query:
				# You need to create an account on Twilio to use this service
				account_sid = 'AC375cad920882f36db6ec89c3aa2188a3'
				auth_token = 'd52be137d04f06d8e896a7d2047920f7'
				client = Client(account_sid, auth_token)
				speak("tell me what to write")
				msg=takeCommand()
				print(msg)
				speak("Phone number of the receiver")
				to=takeCommand()
				to=to.replace(" ", "")
				to="+91"+to
				print(to)
				message = client.messages \
								.create(
									body = msg,
									from_='+18787897854',
									to =to
								)

				print(message.sid)



		elif "Good Morning" in query:
			speak("A warm" +query)
			speak("How are you Mister")
			speak(usname)

		# most asked question from google Assistant
		elif "will you be my gf" in query or "will you be my bf" in query:
			speak("I'm not sure about, may be you should give me some time")

		elif "how are you" in query:
			speak("I'm fine")

		elif "i love you" in query:
			speak("It's hard to understand")

		elif "what is" in query or "who is" in query:
			
			# Use the same API key
			# that we have generated earlier
			client = wolframalpha.Client("API_ID")
			res = client.query(query)
			
			try:
				print (next(res.results).text)
				speak (next(res.results).text)
			except StopIteration:
				print ("No results")

		# elif "" in query:
			# Command go here
			# For adding more commands
		elif 'object' in query or 'detection' in query: 
			speak('Turning Object Detection mode on...')
			fe.startvideo(1)
		elif 'text' in query or 'read' in query:
			speak('Turning OCR mode on...')
			fe.startvideo(3)
		elif 'mentoring' in query:
			speak("Turning mentoring mode on...")
			webbrowser.open(
                'https://us04web.zoom.us/j/79941375580?pwd=2_9ULUfMB0SS1id9RzxU-GTPGzBuwG.1')
