import pyttsx3
from datetime import datetime
import speech_recognition
import wikipedia
import smtplib
import webbrowser
import os
import psutil
import pyjokes
import time
import json
import requests



engine = pyttsx3.init('sapi5')

def text_to_speech(text):
    engine.say(text)
    engine.runAndWait()


def time():
    Time = datetime.now().strftime("%I:%M:%S")
    text_to_speech("Time is ")
    text_to_speech(Time)
    

def date():
    text_to_speech("Today is ")
    year = int(datetime.now().year)
    month = int(datetime.now().month)
    day = int(datetime.now().day)
    text_to_speech(day)
    text_to_speech(month)
    text_to_speech(year)
    

def greetings():
    text_to_speech("Welcome sir")
    part = datetime.now().hour
    if part >= 1 and part < 12:
        text_to_speech("Good Morning")
    elif part >= 12 and part < 16:
        text_to_speech("Good afternoon")
    elif part >= 16 and part < 24:
        text_to_speech("Good evening")
    text_to_speech("At your service")
    

def take_command():
    start = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        start.adjust_for_ambient_noise(source)
        print("Listening...")
        start.pause_threshold = 2
        audio = start.listen(source)

    try:
        print("Recognizing...")
        data = start.recognize_google(audio, language= 'en-in')
        print(data)

    except Exception as e:
        print(e)
        text_to_speech("Sorry, Try again")
        return None

    return data

def send_email(to, content):
    action = smtplib.SMTP("smtp.gmail.com", 587)
    action.ehlo()
    action.starttls()
    #action.login("")
    #action.sendmail("", to, content)
    action.close

def cpu():
    usage = str(psutil.cpu_percent())
    text_to_speech(usage)
    print(usage)

def battery():
    available = psutil.sensors_battery()
    text_to_speech(available)
    print(available)

def jokes():
    text_to_speech(pyjokes.get_joke())

if __name__ == "__main__":
    greetings()
    while True:
        data = take_command().lower()

        if 'time' in data:
            time()

        elif "date" in data:
            date()

        elif 'who are you' in data or 'what can you do' in data:
            text_to_speech('I am your personal assistant. I am programmed to minor tasks like'
                  'opening youtube, google chrome, gmail, search wikipedia, get you weather information.' )


        elif "wikipedia" in data:
            text_to_speech("Searching...")
            data = data.replace("wikipedia", "")
            result = wikipedia.summary(data, sentences = 3)
            print(result)
            text_to_speech(result)

        elif "send email" in data:
            try:
                text_to_speech("What do you want to send?")
                content = take_command()
                #to = ""
                #send_email(to, content)
                text_to_speech("Email has been sent successfully!")

            except Exception as e:
                print(e)
                text_to_speech("Unable to send email!")

        elif "search on chrome" in data:
            text_to_speech("What do you want to search?")
            chromelocation = "C:/Program Files/Google/Chrome/Application/chrome.exe"
            var = take_command().lower()
            webbrowser.open_new_tab(var + ".com")

        elif 'open youtube' in data:
            webbrowser.open_new_tab("https://www.youtube.com")
            text_to_speech("youtube is open now")
            

        elif 'open google' in data:
            webbrowser.open_new_tab("https://www.google.com")
            text_to_speech("Google chrome is open now")
            

        elif 'open gmail' in data:
            webbrowser.open_new_tab("gmail.com")
            text_to_speech("Google Mail open now")
            

        elif "open word" in data: 
            text_to_speech("Opening Microsoft Word") 
            os.startfile('"C:/Program Files/Microsoft Office/root/Office16/WINWORD.EXE"')

        elif "weather" in data:
            api_key="bd0504f9e4fe80faa16c8561f9edd9f0"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            text_to_speech("what is the city name")
            city_name= take_command()
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x=response.json()
            if x["cod"]!="404":
                y=x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                text_to_speech(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))

        elif "logout" in data:
            os.system("shutdown -l")

        elif "shutdown" in data:
            os.system("shutdown /s /t 1")

        elif "restart" in data:
            os.system("shutdown /r /t 1")

        elif "play songs" in data:
            directory = ""
            songs = os.listdir(directory)
            os.startfile(os.path.join(directory, songs[:]))

        elif "cpu" in data:
            cpu()

        elif "battery" in data:
            battery()

        elif "joke" in data:
            jokes()

        elif "goodbye" in data or "stop" in data or "quit" in data:
            quit()

        




    
 




