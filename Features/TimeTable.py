from datetime import datetime
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

FiveTo6 = '''
In This Time , 
You Have To Get Up & Do some exercise .
5:00 Am To 6:00 Am 
Thanks.
'''

SixTo7 = '''
In This Time , 
You Have To Read newspaper or listen something positive .
6:00 Am To 7:00 Am .
Thanks .
'''

SevenTo9 = '''
In This Time , 
You Have To Study .
7:00 Am To 9:00 Am .
Thanks .
'''

NineTo10 = '''
In This Time ,
Get ready for college and go to college .
9:00 Am To 10:00 Am .
Thanks .
'''

TenTo15 = '''
In This Time ,
You are im the college .
Study sincerely .
10:00 Am To 15:00 Pm .
Thanks .
'''

FifteenTo16 = '''
In This Time
You are on way to your home
15:00 Pm To 16:00 Pm .
'''

SixteenTo17 = '''
In This Time ,
You Have To take some rest or get some snacks .
16:00 Pm To 17:00 Pm .
Thanks .
'''

SeventeenteenTo19 = '''
In This Time ,
You Have To go to market and buy some vegetables .
17:00 Pm To 19:00 Pm .
Thanks .
'''

NineteenTo22 = '''
In This Time ,
You have to study .
19:00 Pm To 22:00 Pm'''

TwentyTwoTo23 = '''
In This Time ,
You Have to take dinner .
22:00 Pm To 23:00 Pm .
Thanks .
'''

def Time():

    hour = int(datetime.now().strftime("%H"))

    if hour>=5 and hour<6:
        Speak(FiveTo6)
        return FiveTo6
        
    elif hour>=6 and hour<7:
        Speak(SixTo7)
        return SixTo7

    elif hour>=7 and hour<9:
        Speak(SevenTo9)
        return SevenTo9

    elif hour>=9 and hour<10:
        Speak(NineTo10)
        return NineTo10

    elif hour>=10 and hour<15:
        Speak(TenTo15)
        return TenTo15

    elif hour>=15 and hour<16:
        Speak(FifteenTo16)
        return FifteenTo16
    
    elif hour>=16 and hour<17:
        Speak(SixteenTo17)
        return SixteenTo17
    
    elif hour>=17 and hour<19:
        Speak(SeventeenteenTo19)
        return SeventeenteenTo19
    
    elif hour>=19 and hour<22:
        Speak(NineteenTo22)
        return NineteenTo22
    
    elif hour>=22 and hour<23:
        Speak(TwentyTwoTo23)
        return TwentyTwoTo23
        
    else:
        Speak("In This Time , You Have To Sleep ")

        return '''In This Time , You Have To Sleep .'''