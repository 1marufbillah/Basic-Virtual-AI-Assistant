import datetime
import sys
import randfacts
import pyttsx3 as p
import speech_recognition as sr
from Wikipedia import *
from Youtube import *
from News import *
from Weather import *
from Email import *

engine = p.init('sapi5')
rate = engine.getProperty('rate')
engine.setProperty('rate', 170)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(sound):
    engine.say(sound)
    engine.runAndWait()


def greetMe():
    hour = (datetime.datetime.now().hour)
    if 0 <= hour <= 11:
        return 'Good Morning!'
    elif 12 <= hour < 18:
        return 'Good Afternoon!'
    else:
        return 'Good Evening!'


today = datetime.datetime.now()
speak(greetMe() + "sir, " + " I am your AI Assistant.")
print(today.strftime('%d %B %Y ') + today.strftime('%I:%M %p'))
speak('today is ' + today.strftime('%d') + " of " + today.strftime('%B %Y') +
      ', And it currently ' + today.strftime('%I:%M %p'))
print(str(temperature()))
print(str(description()))
speak('Temperature in Bogura is ' + str(temperature()) + " degree Celsius" + ' and with' + str(description()))
speak('How are you?')


def pack():
    r = sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        r.energy_threshold = 1000
        r.adjust_for_ambient_noise(source, 1.2)
        print('listening...')
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
        except Exception:
            print('say that again please...')
            return 'None'

    if 'what' and 'about' and 'you' in text:
        speak('I am having a good day')
    speak('What can I do for you?')

    with sr.Microphone(device_index=1) as source:
        r.energy_threshold = 1000
        r.adjust_for_ambient_noise(source, 1.2)
        print('listening...')
        audio = r.listen(source)
        try:
            command = r.recognize_google(audio)
        except Exception:
            print('say that again please...')
            return 'None'

    if 'information' in command:
        speak('you need information to which topic?')
        with sr.Microphone(device_index=1) as source:
            r.energy_threshold = 1000
            r.adjust_for_ambient_noise(source, 1.2)
            print('listening...')
            audio = r.listen(source)
            try:
                info = r.recognize_google(audio)
            except Exception:
                print('say that again please...')
                return 'None'
            print(f'user said:{info}')
        speak(f'Searching {info} in wikipedia')
        assist = infowiki()
        assist.get_info(info)

    elif 'play' and 'video' in command:
        speak('you want me to play which video?')
        with sr.Microphone(device_index=1) as source:
            r.energy_threshold = 1000
            r.adjust_for_ambient_noise(source, 1.2)
            print('listening...')
            audio = r.listen(source)
            try:
                video = r.recognize_google(audio)
            except Exception:
                print('say that again please...')
                return 'None'
        speak(f'Playing {video} on youtube')
        assist = youtube()
        assist.play(video)

    elif 'news' in command:
        speak('definitely, Now I will read news for you.')
        arr = news()
        for i in range(len(arr)):
            print(arr[i])
            speak(arr[i])

    elif 'fact' in command:
        x = randfacts.getFact()
        print(f'Fact: {x}')
        speak('Did you know that, ' + x)

    elif 'send the email' in command:
        try:
            sendEmail()
            speak('Email sent successfully')
        except Exception as em:
            print(em)
            speak('Sorry , Something went wrong. I am not able to send this email. Please try again')
            return 'None'
    elif 'stop' in command:
        sys.exit()


while True:
    pack()
