import webbrowser as web
from time import sleep
from pyautogui import click
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

def Speak(audio):
    print(" ")
    print(f": {audio}")
    engine.say(audio)
    engine.runAndWait()
    print(" ")

def OnlineClasses(Subject):

    if 'science' in Subject:
        Speak("Joining The Class Sir .")
        from FileStore.OnlineClasses.Links import Science
        Link = Science()
        web.open(Link)
        sleep(10)
        click(x=412, y=571)
        sleep(1)
        click(x=1011, y=443)

        Speak("Class Joined Sir .")

    elif 'mathematics' in Subject:
        Speak("Joining The Class Sir .")
        from FileStore.OnlineClasses.Links import Maths
        Link = Maths()
        web.open(Link)
        sleep(10)
        click(x=412, y=571)
        sleep(1)
        click(x=1011, y=443)

        Speak("Class Joined Sir .")

    elif 'social' in Subject:
        Speak("Joining The Class Sir .")
        from FileStore.OnlineClasses.Links import sst
        Link = sst()
        web.open(Link)
        sleep(10)
        click(x=412, y=571)
        sleep(1)
        click(x=1011, y=443)

        Speak("Class Joined Sir .")

    elif 'hindi' in Subject:
        Speak("Joining The Class Sir .")
        from FileStore.OnlineClasses.Links import Hindi
        Link = Hindi()
        web.open(Link)
        sleep(10)
        click(x=412, y=571)
        sleep(1)
        click(x=1011, y=443)

        Speak("Class Joined Sir .")

    elif 'english' in Subject:
        Speak("Joining The Class Sir .")
        from FileStore.OnlineClasses.Links import English
        Link = English()
        web.open(Link)
        sleep(10)
        click(x=412, y=571)
        sleep(1)
        click(x=1011, y=443)

        Speak("Class Joined Sir .")