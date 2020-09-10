import pyttsx3
import datetime

engine = pyttsx3.init()


def speak(audio):
    engine.setProperty("rate", 167)
    engine.say(audio)
    engine.runAndWait()


def time_():
    Time = datetime.datetime.now().strftime("%H:%M:%S")
    speak("The current time is")
    speak(Time)


def date_():
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    date = datetime.datetime.now().day
    speak("The current date is ")
    speak(date)
    speak(month)
    speak(year)


def wish_me():
    speak('Welcome back User')


time_()
date_()
