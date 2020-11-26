
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os

converter = pyttsx3.init() 
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)
converter.setProperty('rate', 100)
converter.setProperty('volume', 0.9)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour>18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am jarvis. Please tell me how may I help you")

def takeCommand():
    # It takes microphone input from the user and gives string output to user

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.8 
        r.dynamic_energy_threshold = 100
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said:{query}\n")

    except Exception as e:
        # print(e)

        print("Say that again please..")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        # Logic for executing tasks based on query 
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'calculator' in query:
            calcPath = "F:\\python\\calc\\calculator.py"
            os.startfile(calcPath)

        elif 'open youtube' in query:
            speak(f"Opening youtube")
            print(f"Opening youtube")
            webbrowser.open("www.youtube.com")

        elif 'open google' in query:
            speak(f"Opening google")
            print(f"Opening google")
            webbrowser.open("www.google.com")

        elif 'open snap homework' in query:
            speak(f"Opening snap homework")
            print(f"Opening snap homework")
            webbrowser.open("https://web.snapworks.me/parent-students/activities")


        elif 'open whatsapp' in query:
            speak(f"Opening whatsapp")
            print(f"Opening whatsapp")
            webbrowser.open("https://web.whatsapp.com/")

        elif 'open amazon' in query:
            speak(f"Opening amazon")
            print(f"Opening amazon")
            webbrowser.open("https://amazon.com/")

        elif 'open spark adobe' in query:
            speak("Opening spark adobe")
            print(f"Opening spark adobe")
            webbrowser.open("https://spark.adobe.com/sp/")


        elif 'open discord' in query:
            speak(f"Opening discord")
            print(f"Opening discord")
            webbrowser.open("https://discord.com/channels/@me")

        elif 'music' in query:
            speak("Opening music playlist on youtube")
            print(f"Opening music playlist on youtube")
            webbrowser.open("https://www.youtube.com/watch?v=aNsgbgx7tIw&list=PLRBp0Fe2GpgnIh0AiYKh7o7HnYAej-5ph")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S") 
            speak(f"the time is{strTime}")
            print(f"{strTime}")

        elif 'explorer' in query:
            speak("Opening explorer")
            print("Opening explorer")
            ePath = "C:\\Windows\\explorer.exe"
            os.startfile(ePath)

        elif 'open code' in query:
            speak(f"Opening code")
            print(f"Opening code")
            codePath = "F:\\pycharm and visual studio\\visual studio\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'who are you' in query:
            print("My name is Jarvis")
            speak("My name is Jarvis")


        elif 'open chrome' in query:
            speak(f"Opening chrome")
            print(f"Opening chrome")
            chromePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(chromePath)


        elif 'open recorder' in query:
            speak(f"Opening recorder")
            print(f"Opening recorder")
            webbrowser.open("https://www.apowersoft.com/free-online-screen-recorder")

        elif 'open command prompt' in query:
            speak("Opening command prompt")
            print(f"Opening command prompt")
            cmdPath = "C:\\Windows\\System32\\cmd.exe"
            os.startfile(cmdPath)

        elif 'game' in query:
            speak("Opening Game")
            print("Opening Game")
            webbrowser.open("https://poki.com/")

        elif 'you can leave' in query:
            speak("Okk Goodbye")
            print("Okk Goodbye")
            speak("Stay home, Stay safe")
            print("Stay home, Stay safe")
            break

        elif 'open photoshop' in query:
            photoPath = "C:\\Program Files\\Adobe\\Adobe Photoshop CS6 (64 Bit)\\Photoshop.exe"
            speak("Opening Photoshop")
            print("Opening Photoshop")
            os.startfile(photoPath)

        elif 'bye' in query:
            speak("Okk Bye")
            print("Okk Bye")
            break

        elif 'how are you' in query:
            speak("I am fine.. Thank you")
            print("I am fine.. Thank you")

        elif 'powershell' in query:
            speak("Opening Windows Powershell")
            print("Opening Windows Powershell")
            pPath = "C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\powershell.exe"
            os.startfile(pPath)

        elif 'paint' in query:
            speak("Opening paint")
            print("Opening paint")
            msPath = "C:\\Windows\\system32\\mspaint.exe"
            os.startfile(msPath)