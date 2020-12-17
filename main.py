import wolframalpha
import pyttsx3
import json
import random
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pyjokes
from music2storage import Music2Storage
import smtplib
import time
import requests
import shutil
from twilio.rest import Client
from clint.textui import progress
from ecapture import ecapture as ec
from urllib.request import urlopen
random.seed(random.randint(1, 9000))
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
m2s = Music2Storage()
m2s.use_music_service('youtube')
m2s.use_storage_service('local')
m2s.start_workers()
m2s.add_to_queue('https://www.youtube.com/watch?v=DhHGDOgjie4')
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
 
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        speak("Good Morning!")
  
    elif hour>= 12 and hour<18:
        speak("Good Afternoon!")   
  
    else:
        speak("Good Evening!")  
  
    assiname =("Averse assistant")
    speak("I am your Assistant")
    speak(assiname)
     
 
def usrname():
    global uname
    speak("What should I call you")
    uname = takeCommand()
    speak("Welcome ")
    speak(uname)
    columns = shutil.get_terminal_size().columns
     
    print("#####################".center(columns))
    print("Welcome ", uname.center(columns))
    print("#####################".center(columns))
     
    speak("How can I Help you")
 
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
  
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    speak("What is your email id")
    iid = takeCommand()
    speak("What is your email password")
    pwd = takeCommand()
    server.login(iid, pwd)
    server.sendmail(id, to, content)
    server.close()

if __name__ == '__main__':
    global assiname
    clear = lambda: os.system('clear')
    clear()
    wishMe()
    usrname()
     
    while True:
         
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 3)
            speak("According to Wikipedia")
            print(results)
            speak(results)
 
        elif 'open youtube' in query:
            speak("Here you go\n")
            webbrowser.open("youtube.com")
 
        elif 'open google' in query:
            speak("Here you go\n")
            webbrowser.open("google.com")
 
        elif 'open stackoverflow' in query:
            speak("Here you go.Happy coding")
            webbrowser.open("stackoverflow.com")   
 
        elif 'play music' in query or "play song" in query:
            speak("Here you go.")
            music_dir = ".\\Music"
            songs = os.listdir(music_dir)
            print(songs)    
            randomsong = os.startfile(os.path.join(music_dir, songs[random.randint(0, len(songs)-1)]))
 
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("% H:% M:% S")    
            speak(f"{uname}, the time is {strTime}")
 
        elif 'email' in query:
            try:
                speak("What should I say")
                content = takeCommand()
                speak("To who")
                to = takeCommand()
                sendEmail(to, content)
                speak("Email has been sent !")
            except Exception as e:
                print(e)
                speak("I am not able to send this email")
 
        elif 'send a email' in query:
            try:
                speak("What should I say")
                content = takeCommand()
                speak("To who")
                to = takeCommand()   
                sendEmail(to, content)
                speak("Email has been sent !")
            except Exception as e:
                print(e)
                speak("I am not able to send this email")
 
        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you")
 
            if 'fine' in query or "good" in query:
                speak("It's good to know that your fine")
 
        elif "change my name to" in query:
            query = query.replace("change my name to", "")
            aname = query
 
        elif "change name" in query:
            speak("What would you like to call me")
            aname = takeCommand()
            speak("Thanks for naming me")
 
        elif "what's your name" in query or "What is your name" in query:
            speak("My friends call me")
            speak(aname)
            print("My friends call me", aname)
 
        elif 'exit' in query:
            speak("Thanks for giving me your time")
            exit()
 
        elif "who made you" in query or "who created you" in query: 
            speak("I have been created by AverseABFun.")
             
        elif 'joke' in query:
            speak(pyjokes.get_joke())
        elif 'search' in query or 'play' in query:
            query = query.replace("search", "") 
            query = query.replace("play", "")          
            webbrowser.open(query) 
 
        elif "who i am" in query:
            speak("If you talk then definately your human.")
 
        elif "why you came to world" in query:
            speak("Thanks to AverseABFun. further It's a secret")
 
        elif 'is love' in query:
            speak("It is 7th sense that destroy all other senses")
 
        elif "who are you" in query:
            speak("I am your virtual assistant created by AverseABFun")
 
        elif 'reason for you' in query:
            speak("I was created as a Minor project by Mister AverseABFun ")

        elif 'news' or 'the news' in query:
             
            try: 
                jsonObj = urlopen('''https://news.google.com/topstories?hl=en-US&gl=US&ceid=US:en''')
                data = json.load(jsonObj)
                i = 1
                 
                speak('here are some top news')
                print('''=============== NEWS ============'''+ '\n')
                 
                for item in data['articles']:
                     
                    print(str(i) + '. ' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    speak(str(i) + '. ' + item['title'] + '\n')
                    i += 1
            except Exception as e:
                 
                print(str(e))
 
        elif "don't listen" in query or "stop listening" in query:
            speak("for how much time you want to stop {assiname} from listening commands")
            a = int(takeCommand())
            time.sleep(a)
            print(a)
 
        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.com / maps / place/" + location + "")
 
        elif "camera" in query or "take a photo" in query:
            ec.capture(0, "Cool Camera ", "img.jpg")
 
        elif "write a note" in query:
            speak("What should i write")
            note = takeCommand()
            file = open('notes.txt', 'w')
            speak("Should i include date and time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = str(datetime.datetime.now().strftime("% H:% M:% S"))
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)
            file.close()
         
        elif "show note" in query:
            speak("Showing Notes")
            file = open("notes.txt", "r") 
            print(file.read())
            speak(file.read(6))
            file.close()
 
        elif "update assistant" in query:
            speak("After downloading file please replace this file with the downloaded one")
            url = 'https://github.com/AverseABFun/voice-assistant'
            r = requests.get(url, stream = True)
             
            with open("main.py", "wb") as Pypdf:
                 
                total_length = int(r.headers.get('content-length'))
                 
                for ch in progress.bar(r.iter_content(chunk_size = 2391975),
                                       expected_size =(total_length / 1024) + 1):
                    if ch:
                      Pypdf.write(ch)
                     
        # NPPR9-FWDCX-D2C8J-H872K-2YT43
        elif "jarvis" in query:
             
            wishMe()
            speak(aname)
            speak(" in your service")
 
        elif "weather" in query:
             
            # Google Open weather website
            # to get API of Open weather 
            api_key = "Api key"
            base_url = "http://api.openweathermap.org / data / 2.5 / weather"
            speak(" City name ")
            print("City name : ")
            city_name = takeCommand()
            complete_url = base_url + "appid =" + api_key + "&q =" + city_name
            response = requests.get(complete_url) 
            x = response.json() 
             
            if x["cod"] != "404": 
                y = x["main"] 
                current_temperature = y["temp"] 
                current_pressure = y["pressure"] 
                current_humidiy = y["humidity"] 
                z = x["weather"] 
                weather_description = z[0]["description"] 
                print(" Temperature (in kelvin unit) = " +str(current_temperature)+"\n atmospheric pressure (in hPa unit) ="+str(current_pressure) +"\n humidity (in percentage) = " +str(current_humidiy) +"\n description = " +str(weather_description)) 
             
            else: 
                speak(" City Not Found ")
             
        elif "send message " in query:
                # You need to create an account on Twilio to use this service
                account_sid = 'Account Sid key'
                auth_token = 'Auth token'
                client = Client(account_sid, auth_token)
 
                message = client.messages \
                                .create(
                                    body = takeCommand(),
                                    from_='Sender No',
                                    to ='Receiver No'
                                )
 
                print(message.sid)
 
        elif "wikipedia" in query:
            webbrowser.open("wikipedia.com")
 
        elif "good morning" in query:
            query.replace("good morning", "")
            speak("A warm" +query)
            speak("How are you")
            speak(aname)
 
        # most asked question from google Assistant
        elif "will you be my gf" in query or "will you be my bf" in query:   
            speak("I'm not sure about, maybe you should give me some time")
 
        elif "how are you" in query:
            speak("I'm fine, glad you asked")
 
        elif "i love you" in query:
            speak("Thanks!")
 
        elif "what is" in query or "who is" in query:
            query.replace("what is", "")
            query.replace("who is", "")
            # Use the same API key 
            # that we have generated earlier
            client = wolframalpha.Client("API_ID")
            res = client.query(query)
             
            try:
                print (next(res.results).text)
                speak (next(res.results).text)
            except StopIteration:
                print ("No results")
                speak("No results!")