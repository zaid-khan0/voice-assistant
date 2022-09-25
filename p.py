import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import webbrowser
import calendar
import wikipedia
import pywhatkit

engine=pyttsx3.init('sapi5')   
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',150)

#t=datetime.datetime.today()

def speak(command):
    engine.say(command)
    engine.runAndWait()

def takecommand():
    s=sr.Recognizer()
    with sr.Microphone() as source:
        print("speak now")
        s.pause_threshold=1
        s.energy_threshold=1000
        audio=s.listen(source)
    try:
        print("recognizing....")
        query=s.recognize_google(audio,language="en-in")
        print(query)
    except:
        speak("couldn't reacognize your voice")
        return "None"
    return query

def username():
    speak("what's your name")
    name=takecommand()
    speak(f"hello {name} how can i help you")

def wish():
    hr=int(datetime.datetime.now().hour)
    if hr>=0 and hr<12:
        speak("good morning")
    elif hr>=12 and hr<18:
        speak("good afternoon")
    else:
        speak("good evening")

    intro()
   # username()

def intro():
    speak("hello i am jarvis,how can i help you ")

if __name__=="__main__":
    wish()

    while True:
        query=takecommand().lower()
        if 'who are you' in query:
            speak("i am jarvis")

        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com/")
            exit()
        
        elif 'open google' in query:
            webbrowser.open("https://www.google.com/")
            exit()

        elif 'wikipedia' in query:
            speak("searching...")
            query=query.replace('wikipedia',"")
            res=wikipedia.summary(query,sentence=2)
            print(res)
            speak(res)

        elif 'trending video' in query:
            pywhatkit.playonyt("https://www.youtube.com/feed/trending")
            exit()

        elif 'video in youtube' in query:
            query=query.replace('video in youtube','')
            pywhatkit.playonyt(query)
            exit()

        elif 'song in youtube' in query:
            query=query.replace('play song in youtube','')
            pywhatkit.playonyt(query)
            exit()

        elif 'trending song in youtube' in query:
            pywhatkit.playonyt('https://www.youtube.com/playlist?list=PLFgquLnL59alwzM3kQ6cWhwwZXa4TCjN4')
            exit()

        elif 'time' in query:
            time=datetime.datetime.now().strftime('%I %M %p')
            print(f"the time is {time}")
            speak(f"the time is {time}")
           
        elif 'date' in query:
            date=datetime.datetime.now().strftime('%d %B %Y')
            print(f"date is {date}")
            speak(f"date is {date}")

        elif 'today day' in query:
            day=datetime.datetime.now().weekday()
            print(calendar.day_name[day])
            speak(calendar.day_name[day])

        elif 'who made you' in query:
            speak("the very intelligent ,very handsome guy named zaid khan made me")

        elif 'how are you' in query:
            speak("i am fine")
            speak("how are you ")

        elif 'fine' in query or 'good' in query:
            speak(f"it's good to know that you are {query}")

        elif 'quit' in query or 'exit' in query:
            speak("thanks for taking my help")
            break
        else:
            pywhatkit.search(query)
            exit()
