import pyttsx3, random, sys, webbrowser, wikipedia, requests, pyautogui, os  
from urllib.request import urlopen
import pyjokes as pj
from bs4 import BeautifulSoup as bs
import speech_recognition as sr  
from datetime import datetime
from requests import get
import requests
import pywhatkit

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 188)

def speak(audio):
    print("Chat Buddy : - ",audio)
    engine.say(audio)
    engine.runAndWait()
speak("Hi there")

d=datetime.now().strftime("%A:%d:%B:%Y")

def myCommand():
    print("Listening...")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration=0.6)
        audio = r.listen(source,phrase_time_limit=5)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-us')
        print("Master: - " + query)

    except sr.UnknownValueError:
        query = myCommand()
    
    except sr.RequestError:
        query = myCommand()

    except sr.WaitTimeoutError:
        query = myCommand()

    return str(query).lower()

def TakeCommand():
        r = sr.Recognizer()
        with sr.Microphone() as source:
                print(": Listening....")
                r.pause_threshold = 1
                audio = r.listen(source)

        try:
                print(": Recognizing...")
                query = r.recognize_google(audio, language='en-in')
                print(f": Your Command : {query}\n")

        except:
                return ""

        return query.lower()


def greetMe():
    currentH = int(datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning Master!')

    elif currentH >= 12 and currentH < 16:
        speak('Good Afternoon Master!')

    elif currentH >= 18 and currentH !=0:
        speak('Good Evening Master!')

if __name__ == "__main__":
    greetMe()

    while 1:
        query = myCommand()
        
        if 'hello' in query or 'hi ' in query or "hey" in query or "get up" in query:
            speak(random.choice(["I'm in",'Hello sir','Hi boss','At your service Sir','I\'m up']))

        elif 'bye' in query or "exit" in query or 'see you later' in query or "close everything" in query:
            speak(random.choice(['Bye Sir, have a good day.','Love you boss!','I will be missing you!!','Bye Sir! Love you']))
            print("     👋")
            print("Exiting...")
            sys.exit()


        #YouTube
        elif 'youtube search' in query or 'on youtube' in query:
                Query = query.replace("Chat Buddy", "")
                query = Query.replace("youtube search", "")
                def YouTubeSearch(term):
                    result = "https://www.youtube.com/results?search_query=" + term
                    webbrowser.open(result)
                    speak("This Is What I Found For Your Search .")
                    pywhatkit.playonyt(term)
                YouTubeSearch(query)
                

        #Locating something
        elif 'where is' in query or 'locate' in query:
                from Features.GoogleMaps import GoogleMaps
                Place = query.replace("where is ", "")
                place = Place.replace("jarvis", "")
                GoogleMaps(place)
        
        #game
        elif "game" in query or 'lets play a game' in query:
                speak("choose among rock paper or scissor")
                moves=["rock", "paper", "scissor"]
                cmove=random.choice(moves)
                Pmove=myCommand().lower()
                pmove=Pmove.lower()
                speak("I chose " + cmove)
                speak("You chose " + pmove)
                if "rock" in pmove == cmove == "rock":
                    speak("The match is draw")
                elif "scissor" in pmove == cmove== "scissor":
                    speak("The match is draw")
                elif "paper" in pmove == cmove== "paper":
                    speak("The match is draw")
                elif "rock" in pmove and cmove== "scissor":
                    speak("You won")
                elif "rock" in pmove and cmove== "paper":
                    speak("I won")
                elif "paper" in pmove and cmove== "rock":
                    speak("You won")
                elif "paper" in pmove and cmove== "scissor":
                    speak("I won")
                elif "scissor" in pmove and cmove== "paper":
                    speak("You won")
                elif "scissor" in pmove and cmove== "rock":
                    speak("I won")
                else:
                    speak("Wrong choice!")

        #Tossing a Coin
        elif "toss a coin" in query:
                moves=["head", "tail"]   
                cmove=random.choice(moves)
                speak("I chose " + cmove + " for you ")
          
        #Rolling of a dice
        elif "roll a dice" in query:
            moves=["1","2","3","4","5","6"]   
            cmove=random.choice(moves)
            speak("I got " + cmove + " for you on dice")

        #Screenshot
        elif "capture" in query or "my screen" in query or "take a screenshot" in query or "what's on my screen" in query or "take screenshot" in query:
                myScreenshot = pyautogui.screenshot()
                strTime = datetime.now().strftime("%H_%M_%S")
                myScreenshot.save('screenshot'+strTime+'.png')
                speak("Screenshot done")
                speak("Here's the screenshot")
                os.startfile('screenshot'+d+'.png')

        #Joke
        elif 'joke' in query or "jokes" in query:
                try:
                    speak(pj.get_joke('en','all'))
                except:
                    res = get('https://icanhazdadjoke.com/',headers={"Accept":"application/json"})
                    if res.status_code == requests.codes.ok:
                        speak(str(res.json()['joke']))
                    else:
                        speak('Oops! I ran out of jokes')

        #Defining terms
        elif "definition of" in query or 'define' in query:
                try:
                    results = wikipedia.summary(query, sentences=2)
                    speak('Got it.')
                    speak(results)
                except:
                    speak("Sorry, I wasn't able to find the definition")

        elif "search for " in query:
                ssc = query.split("search for ")[-1]
                url = "https://google.co.in/search?q=" + ssc
                speak("Here is what I found for " + ssc + " on google")
                webbrowser.get().open(url)

        #time & date
        elif 'the time' in query or 'time now' in query:
            strTime = datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        
        elif "date" in query or "today's date" in query:
            dateT=datetime.now().strftime("%B:%d:%A:%Y")
            speak("Today's date is "+dateT)

        #Time Table
        elif "time table" in query:
             from Features.TimeTable import Time
             Time()
             speak("AnyThing Else Sir ??")

        #Online Classes
        elif 'online' in query or 'join online class' in query:
            speak("Tell Me The Name Of The Class .")
            Class = TakeCommand()
            from Features.OnlineClasses import OnlineClasses
            OnlineClasses(Class)

        #Covid Cases
        elif 'covid cases' in query or 'corona cases' in query or 'cases of corona' in query or 'corona' in query:
            from Features.Covid import CoronaVirus
            speak("Which Country's Information ?")
            def TakeCommand():
                r = sr.Recognizer()
                with sr.Microphone() as source: 
                    print(": Listening....")
                    r.pause_threshold = 1
                    audio = r.listen(source)

                try:
                    print(": Recognizing...")
                    query = r.recognize_google(audio, language='en-in')
                    print(f": Your Command : {query}\n")

                except:
                    return ""

                return query.lower()
            cccc = TakeCommand()
            CoronaVirus(cccc)

        #Notepad
        elif 'write a note' in query:
            from Features.Notepad import Notepad
            Notepad()

        elif 'dismiss' in query or 'close the note' in query:
            from Features.Notepad import CloseNotepad
            CloseNotepad()
        
        #Internet
        elif 'news' in query or 'news feeds' in query or 'get me news' in query:
            speak(random.choice(["Here are the top five news of the day","Here's your latest news",'Just a second']))
            try:
                news_url=get("https://news.google.com/news/rss").content
                soup_page=bs(news_url,"xml")
                news_list=soup_page.findAll("item")
                for news in news_list[:5]:
                    speak(news.title.text)
                speak("These were the top headlines, Have a nice day Sir!!..")
            except Exception as e:
                speak("An Error Occurred")
        else:
            speak("I don't know the answer to your query yet!!")

