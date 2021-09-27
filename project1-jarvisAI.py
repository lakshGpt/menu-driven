import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import pyaudio
import webbrowser
import os
import random
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    
    speak("I am Jarvis Sir, Please tell me how may I help you!")

def takeCommand():
    # this takes microphone input from the user and return string output
    r = sr.Recognizer()     # this recogniser class will help in recognising the class
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1      # pause_threshold - seconds of non-speaking audio before a phrase is considered complete
        r.adjust_for_ambient_noise(source,duration=1)
        audio = r.listen(source)    # listen -Records a single phrase from ``source`` (an ``AudioSource`` instance) into an ``AudioData`` instance, which it returns
    try:
        print("Recognizing....")
        query = r.recognize_google(audio,language='en-in')
        print(f"user said : {query}\n")    
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('lakshaygpt14@gmail.com','9911956836')
    server.sendmail('lakshaygpt14@gmail.com',to,content)
    server.close()


if __name__ == "__main__":
    
    #sendEmail('guptalakshay104@gmail.com','i m a good boy') 
    
    speak("hello lakshay!")
    wishMe()
    while True:
        query = takeCommand().lower()

        # logic for executing task based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia....')
            query = query.replace("Wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'open instagram' in query:
            webbrowser.open("instagram.com")

        elif 'quit' in query or 'bye' in query:
            speak("Quitting sir . Thanks for your time")
            exit()

        elif 'who are you' in query:
            speak("I am Jarvis , and I am not a machine!")
        
        elif 'play video songs' in query:
            videoSongs_dir = 'F:\\Video'
            videoSongs = os.listdir(videoSongs_dir)
            os.startfile(os.path.join(videoSongs_dir,videoSongs[random.randint(0,len(videoSongs)-1)]))

        elif 'play music' in query:
            music_dir = 'H:\\old is gold'
            songs = os.listdir(music_dir)
            #print(songs)
            os.startfile(os.path.join(music_dir,songs[random.randint(0,len(songs)-1)]))
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"sir,the time is {strTime}")
            speak(f"Sir,the time is {strTime}")

        elif 'open vs code' in query:
            code_path = "C:\\Users\\LAKSHAY\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(code_path)
        
        elif 'email to naina' in query:
            try:
                speak("what should I say!")
                content = takeCommand()
                to = "guptanaina118@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent !")
            except Exception as e:
                print(e)
                speak('Sorry my friend lakshay bhai, I am not able to send this email')
            
