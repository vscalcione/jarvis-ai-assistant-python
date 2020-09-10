import pyttsx3
import datetime

engine = pyttsx3.init()


def speak(audio):
    engine.setProperty("rate", 156)
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

    # Greetings
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak('Good Morning User')
    elif hour >= 12 and hour < 18:
        speak('Good Afternoon User')
    elif hour >= 18 and hour < 24:
        speak('Good Evening User')
    else:
        speak('Good Night User')

    speak('Jarvis at your service. Please tell me how can I help you today?')


wish_me()
