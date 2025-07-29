from email.mime import audio
from logging.config import listen
from tkinter import E
from typing import Self  # to GUI
import pyttsx3  # text to speech convert
import subprocess  # to go system on and off or in sleepmode
import pywhatkit  # to open and search queries on application
import datetime  # to tell date and time
import speech_recognition as sr  # google speech api speech to text converter
import wikipedia
import webbrowser
import wolframalpha  # to find results from userquestions of mathematics
import os
import random  # to generate random values
import winshell  # to access specific folder and shell files to copy etc
import pyjokes  # to make quick python jokes
import shutil  # to create file in read or write mode
import json  # to get weather details
import feedparser
import smtplib  # to send mails
import time
import requests  # to get weather details
from twilio.rest import TwilioClient
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen  # to fetch and open the locate usrls
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QMovie
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType

flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint)

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 180)


paths = {
    'notepad': "C:\\Program Files\\Notepad++\\notepad++.exe",
    'discord': "C:\\Users\\ashut\\AppData\\Local\\Discord\\app-1.0.9003\\Discord.exe",
    'calculator': "C:\\Windows\\System32\\calc.exe"
}
url = ('https://newsapi.org/v2/top-headlines?'
       'country = in&'
       'apiKey =')

url += 'f506c90992f2462f97464c2f21711224'

NEWS_API_KEY = " f506c90992f2462f97464c2f21711224"

# import speechRecognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[3].id)
engine.setProperty('voices', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishing():
    hour = int(datetime.datetime.now().hour)
    if (hour >= 0 and hour < 12):
        speak('Good Morning Sir !')

    elif(hour >= 12 and hour < 18):
        speak('Goodafter noon sir !')

    elif(hour >= 18):
        speak('Goodevening sir !')


def getName():
    global username
    speak("Can I please know your name?")
    username = takeuserinput()
    print("Name:", username)
    speak("I am glad to know you!")
    columns = shutil.get_terminal_size().columns
    speak("How can i Help you, ")
    speak(username)


def greet():
    hour = int(datetime.datetime.now().hour)
    if (hour >= 0 and hour < 12):
        speak('Good Morning Sir !')

    elif(hour >= 12 and hour < 18):
        speak('Goodafter !')

    elif(hour >= 18):
        speak('Goodevening !')

    speak(" I am Patrick , Your new ai based Desktop assistant.  How can i help you today ? ")


def send_whatsapp_message(number, message):
    pywhatkit.sendwhatmsg_instantly(f"+91{number}", message)


def takeuserinput():
    # it takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening.......')
        r.pause_threshold = 0.8
        audio = r.listen(source)

    try:
        print('Recognizing..... ')
        userinput = r.recognize_google(audio, language='en-in')
        print(f'user said : {userinput}\n ')

    except Exception as e:
        # print(e)
        print('Say that again please ')
        return "None"
    return userinput


def get_random_advice():
    res = requests.get("https://api.adviceslip.com/advice").json()
    return res['slip']['advice']


def sendEmail(to, content):
    print("Sending mail to ", to)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    # paste your email id and password in the respective places
    server.login('namanmotla@gmail.com', '')
    server.sendmail('your email id', to, content)
    server.close()


def timer():
    speak('of how much time')
    text = str(input())
    print("In how many minutes?")
    local_time = float(input())
    local_time = local_time * 60
    time.sleep(local_time)
    print(text)


def getWeather(city_name):
    # cityName=place.get() #getting input of name of the place from user
    # base url from where we extract weather report
    baseUrl = "http://api.openweathermap.org/data/2.5/weather?"
    url = baseUrl + "appid=" + 'd850f7f52bf19300a9eb4b0aa6b80f0d' + "&q=" + cityName
    response = requests.get(url)
    x = response.json()

    # If there is no error, getting all the weather conditions
    if x["cod"] != "404":
        y = x["main"]
        temp = y["temp"]
        temp -= 273
        pressure = y["pressure"]
        humidity = y["humidity"]
        z = x["weather"]
        description = z[0]["description"]
        info = (" Temperature= " + str(temp)+"°C"+"\n atmospheric pressure (hPa) ="+str(pressure) +
                "\n humidity = " + str(humidity)+"%" + "\n description = " + str(description))
        print(info)
        speak("Here is the weather report at")
        speak(city_name)
        speak(info)
    else:
        speak(" City Not Found ")


def open_notepad():
    os.startfile(paths['notepad'])


def open_discord():
    os.startfile(paths['discord'])


def open_cmd():
    os.system('start cmd')


def open_camera():
    subprocess.run('start microsoft.windows.camera:', shell=True)


def open_calculator():
    subprocess.Popen(paths['calculator'])


def get_latest_news():
    try:
        response = requests.get(url)
    except:
        engine.say("can, t access link, plz check you internet ")

    news = json.loads(response.text)
    for new in news['articles']:
        print("##############################################################\n")
        print(str(new['title']), "\n\n")
        engine.say(str(new['title']))
        print('______________________________________________________\n')

        engine.runAndWait()

        print(str(new['description']), "\n\n")
        engine.say(str(new['description']))
        engine.runAndWait()
        print("..............................................................")
        time.sleep(2)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good morning")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good night")


def send_whatsapp_message(number, message):
    pywhatkit.sendwhatmsg_instantly(f"+91{number}", message)


def sendEmail(to, content):
    print("Sending mail to ", to)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    # paste your email id and password in the respective places
    server.login('your email id', 'password')
    server.sendmail('your email id', to, content)
    server.close()


def getWeather(city_name):
    # cityName=place.get() #getting input of name of the place from user
    # base url from where we extract weather report
    baseUrl = "http://api.openweathermap.org/data/2.5/weather?"
    url = baseUrl + "appid=" + 'd850f7f52bf19300a9eb4b0aa6b80f0d' + "&q=" + city_name
    response = requests.get(url)
    x = response.json()

    # If there is no error, getting all the weather conditions
    if x["cod"] != "404":
        y = x["main"]
        temp = y["temp"]
        temp -= 273
        pressure = y["pressure"]
        humidity = y["humidity"]
        z = x["weather"]
        description = z[0]["description"]
        info = (" Temperature= " + str(temp)+"°C"+"\n atmospheric pressure (hPa) ="+str(pressure) +
                "\n humidity = " + str(humidity)+"%" + "\n description = " + str(description))
        print(info)
        speak("Here is the weather report at")
        speak(city_name)
        speak(info)
    else:
        speak(" City Not Found ")


def getNews():
    try:
        response = requests.get('https://timesofindia.indiatimes.com/news')
        b4soup = BeautifulSoup(response.text, 'html.parser')
        headLines = b4soup.find('body').find_all('h3')
        unwantedLines = ['BBC World News TV', 'BBC World Service Radio',
                    'News daily newsletter', 'Mobile app', 'Get in touch']

        for x in list(dict.fromkeys(headLines)):
            if x.text.strip() not in unwantedLines:
                print(x.text.strip())
    except Exception as e:
        print(str(e))


def getName():
    global username
    speak("Can I please know your name?")
    username = self.STT()
    print("Name:", username)
    speak("I am glad to know you!")
    columns = shutil.get_terminal_size().columns
    speak("How can i Help you, ")
    speak(username)


paths = {
    'calculator': "C:\\Windows\\System32\\calc.exe"
}


def open_cmd():
    os.system('start cmd')


def open_camera():
    subprocess.run('start microsoft.windows.camera:', shell=True)


def open_calculator():
    subprocess.Popen(paths['calculator'])


class mainT(QThread):
    def __init__(self):
        super(mainT, self).__init__()

    def run(self):
        self.JARVIS()

    def STT(self):
        R = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listning...........")
            R.pause_threshold = 1
            R.energy_threshold = 600
            audio = R.listen(source)
        try:
            print("Recogn......")
            text = R.recognize_google(audio, language='en-in')
            print(">> ", text)
        except Exception:
            speak("Sorry Speak Again")
            return "None"
        text = text.lower()
        return text

    def JARVIS(self):
        greet()
        while True:
            self.query = self.STT()
            if 'good bye' in self.query:
                sys.exit()
                
            elif 'wikipedia' in self.query:
                speak('Serarching Wikipedia.......')
                self.query  = Self.query.replace('wikipedia', "")
                result = wikipedia.summary(self.query,sentences =2)
                speak('According to Wikipedia ')
                print(result)
                speak(result)
            
            elif 'open youtube' in self.query:
                webbrowser.open("youtube.com")
                
            elif 'open google' in self.query:
                webbrowser.open("google.com")
            
            elif 'play music' in self.query :
                music_dir = 'C:\\Users\\naman\\Desktop\\music'
                songs = os.listdir(music_dir)
                print(songs)
                random.shuffle(songs)    
                os.startfile(os.path.join(music_dir, songs[0]))
                
                    
            elif 'how are you' in self.query or 'how have you been' in self.query :
                speak("I am doing Excellent . Just got a new home in your PC.")
                
            elif 'what are you doing' in self.query:
                    speak("I am here speaking to you. That's what I am doing")
        
            elif 'what am i doing' in self.query:
                    speak("You tell me. My guess is you are speaking to me")
            
            elif 'how is life' in self.query or 'how is your life' in self.query:
                    speak("Life in the silicon world is amazing")
            
            elif 'where do you live' in self.query or 'where do you stay' in self.query or 'where is your home' in self.query \
                        or 'what is your address' in self.query:
                    speak('I live in the silicon world. Be born next time as a software. Then you can come live with me too')
            
            elif 'whom am I speaking to' in self.query:
                    speak("You are speaking to Patrick ")
            
            elif 'who created you' in self.query or 'who made you' in self.query or 'who is your creator' in self.query or \
                        "who's creation are you" in self.query or 'who has made you' in self.query or \
                        'who has created you' in self.query:
                    speak('I was created by  with the helpful suggestions from Himanshu and Zubair  which helped in how I turned out to be.')
            
            elif 'your birthday' in self.query or 'when were you created' in self.query or 'when were you born' in self.query:
                    speak('I am a work in progress always.')
            
            elif 'what is your name' in self.query or 'what should I call you' in self.query or \
                        "what's your name" in self.query:
                    speak("I am Patrick")
            
            elif 'to whom do you belong' in self.query or 'who is your owner' in self.query:
                    speak("I am owned and copyrighted by "+username)
            elif "will you be my gf" in self.query or "will you be my bf" in self.query:
                speak("I'm not sure about that, may be you should give me some time")
            elif "i love you" in self.query:
                speak("Thank you! But, It's a pleasure to hear it from you.")
            elif 'joke' in self.query:
                speak(pyjokes.get_joke())
            elif 'timer' in self.query:
                timer()
            
                
            elif 'mail' in self.query:
                try:
                    speak("Whom should I send the mail")
                    to = STT()
                    speak("What is the body?")
                    content = STT()
                    sendEmail(to, content)
                    speak("Email has been sent successfully !")
                except Exception as e:
                        print(e)
                        speak("I am sorry, not able to send this email")

            elif 'exit' in self.query or 'Thankyou patrick' in self.query:
                speak("Thanks for giving me your time")
                exit()

            elif "weather" in self.query:
                speak(" Please tell your city name ")
                print("City name : ")
                cityName = STT()
                getWeather(cityName)

            elif "what is" in self.query or "who is" in self.query:
                
                client = wolframalpha.Client("API_ID")
                res = client.query(self.query)

                try:
                    print (next(res.results).text)
                    speak (next(res.results).text)
                except StopIteration:
                    print ("No results")

            elif 'search' in self.query:
                self.query = self.query.replace("search", "")
                webbrowser.open(self.query)

            elif 'news' in self.query:
                speak(f"I'm reading out the latest news headlines, sir")
                speak(get_latest_news())
                speak("For your convenience, I am printing it on the screen sir.")
                print(*get_latest_news(), sep='\n')
            
            elif "don't listen" in self.query or "stop listening" in self.query:
                speak("for how much time you want to stop me from listening self.querys")
                a = int(STT())
                time.sleep(a)
                print(a)
                
            elif 'shutdown system' in self.query:
                    speak("Hold On a Sec ! Your system is on its way to shut down")
                    subprocess.call('shutdown / p /f')

            elif "restart" in self.query:
                subprocess.call(["shutdown", "/r"])

            elif 'lock window' in self.query:
                    speak("locking the device")
                    ctypes.windll.user32.LockWorkStation()
                    
            elif "where is" in self.query:
                self.query =self.query.replace("where is", "")
                location = self.query
                speak("User asked to Locate")
                speak(location)
                webbrowser.open("https://www.google.com/maps/place/" +location + "")
                
            elif "open notepad" in self.query:
                speak("Opening notepad sir")
                open_notepad()
                
                
            elif "open discord" in self.query:
                speak("Opening discord sir")
                open_discord()
                
                
            elif "open cmd" in self.query or "open command prompt" in self.query:
                speak("Opening command prompt sir")
                open_cmd()
                
            elif "camera" in self.query:
                speak("Opening camera sir")
                open_camera()
                
            elif "calculator" in self.query:
                speak("Opening calculator sir")
                open_calculator()
            
            elif "advice" in self.query:
                speak(f"Here's an advice for you, sir")
                advice = get_random_advice()
                speak(advice)
                speak("For your convenience, I am printing it on the screen sir.")
                print(advice)

            elif "write a note" in self.query:
                speak("What should i write, sir")
                note = STT()
                file = open('Patrick.txt', 'w')
                speak("Sir, Should i include date and time")
                snfm = STT()
                if 'yes' in snfm or 'sure' in snfm:
                    strTime = datetime.datetime.now().strftime("% H:% M:% S")
                    file.write(strTime)
                    file.write(" :- ")
                    file.write(note)
                else:
                    file.write(note)
                    
            elif "show note" in self.query:
                speak("Showing Notes")
                file = open("patrick.txt", "r")
                print(file.read())
                speak(file.read(6))
                    
            elif 'play ' in self.query:
                song = self.query.replace('play', '')
                speak('playing ' + song)
                pywhatkit.playonyt(song)
                exit()
                
            elif 'time' in self.query:
                time = datetime.datetime.now().strftime('%I:%M %p')
                print(time)
                speak('Current time is ' + time)
                
            elif 'date' in self.query:
                date = datetime.datetime.now().strftime('%d /%m /%y')
                print(date)
                speak('Todays date is ' + date)
                    
            elif 'message ' in self.query or 'whatsapp' in self.query or 'send text' in self.query:
                speak('whom u want to send message')
                number = STT()
                speak('what message u want to send ')
                message= STT()
                send_whatsapp_message(number, message)
                speak('sending message')
                print("Successfully Sent!")
                
            else:
                speak("Sorry, I am not able to understand you")
            
        

