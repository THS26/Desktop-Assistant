import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
from email.mime import audio
from logging.config import listen
from tkinter import E
import webbrowser
import sys
import os
import random




listener = sr.Recognizer()
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def greet():
    hour = int(datetime.datetime.now().hour)
    if (hour>=0 and hour<12):
        talk('Good Morning  !')
    
    elif(hour>=12 and hour<18):
        talk('Goodafter !')
        
    elif(hour>=18):
        talk('Goodevening !')
         
    talk(" I am Patrick ")


# def wishing():
#     hour = int(datetime.datetime.now().hour)
#     if (hour>=0 and hour<12):
#         talk('Good Morning Sir !')
    
#     elif(hour>=12 and hour<18):
#         talk('Goodafter sir!')
        
#     elif(hour>=18):
#         talk('Goodevening  sir!')


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'Patrick' in command:
                command = command.replace('Patrick', '')
                print(command)
    except:
        pass
    return command


def run_Patrick():
    greet()
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is ' + time)
    elif 'date' in command:
        date = datetime.datetime.now().strftime('%d /%m /%y')
        print(date)
        talk('Todays date is ' + date)
        
    elif 'wikipedia' in command:
        person = command.replace('wikipedia', '')
        info = wikipedia.summary(person, 2)
        print(info)
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    
    elif 'open youtube' in command:
        webbrowser.open("youtube.com")
            
    elif 'open google' in command:
        webbrowser.open("google.com")

    elif 'find' in command:
        search=pywhatkit.search(command)
        print("Searching on google")
        talk('searching on google' + search)

    elif 'desktop music' in command:
            music_dir = 'C:\\Users\TH. HIMANSHU SINGH\Music'
            songs = os.listdir(music_dir)
            print(songs)
            random.shuffle(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))
    elif 'message 'or'whatsapp' in command:
        talk('sending message')
        pywhatkit.sendwhatmsg("+919389715559","this is a test message from patrick",00 , 10)
        print("Successfully Sent!")

    elif 'exit' or 'close' in command:
        sys.exit()

    else:
        talk('Please say the command again.')


while True:
    run_Patrick()



    
