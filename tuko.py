import sys
from winreg import QueryInfoKey, QueryReflectionKey, QueryValue
import pyttsx3
import datetime
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pyautogui


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')


# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning sir!")
        speak("i am marcus! how may i help you")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon sir!")
        speak("i am marcus! how may i help you")

    else:
        speak("Good Evening sir!")

        speak("i am marcus! how may i help you")


def takeCommand():
    # it takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)

        print("Say that again please...")
        return "None"
    return query


if __name__ == "__main__":
    # speak("Hello ash i am tooku how may i help you")
    wishMe()
    while True:
        query = takeCommand().lower()

        # logic for execution of tasks based on query
        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak('Opening youtube...')
            webbrowser.open('youtube.com')

        elif 'open google' in query:
            speak('Opening google...')
            webbrowser.open('google.com')

        elif 'open stackoverflow' in query:
            speak('Opening stackoverflow...')
            webbrowser.open('stackoverflow.com')

        elif 'play music' in query:
            music_dir = 'D:\\music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
            speak("playing musics")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S:")
            speak(f"sir, the current time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\ashak\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            speak("code")

        elif 'open chrome' in query:
            codePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(codePath)
            speak("opening chrome")

        elif 'you can quit now' in query:
            speak("thankyou for using me sir,  see you soon,  have a great day.")
            sys.exit()

        elif 'volume up' in query:
            pyautogui.press("volume up")

        elif 'volume down' in query:
            pyautogui.press("volume down")

        elif 'volumemute' in query:
            pyautogui.press("volumemute")
