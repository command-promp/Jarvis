import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import pyautogui
import time

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

        elif 'open snap homework' in query:
            speak(f"Opening snap homework")
            print(f"Opening snap homework")
            webbrowser.open("https://web.snapworks.me/parent-students/activities")

        elif 'open codeathon' in query:
            speak(f"Opening codeathon")
            print(f"Opening codeathon")
            webbrowser.open("https://www.htcodeathon.com/student/dashboard")

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

        elif 'open e connect' in query:
            speak("Opening e connect")
            print(f"Opening e connect")
            webbrowser.open("https://sajs.schooloncloud.com/ParentDashboard/ParentDashboard")

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

        elif 'who made you' in query:
            print("Aradhya Mathur")
            speak("Aradhya Mathur")

        elif 'open chrome' in query:
            speak(f"Opening chrome")
            print(f"Opening chrome")
            chromePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(chromePath)

        elif 'how to make chilly chicken nuggets' in query:
            speak("Opening how to make chilly chicken nuggets")
            print(f"Opening how to make chilly chicken nuggets")
            webbrowser.open("https://www.youtube.com/watch?v=Ki2yrLV34Fw")

        elif 'how to make kadai chicken' in query:
            speak("Opening how to make kadai chicken")
            print(f"Opening how to make kadai chicken")
            webbrowser.open("https://www.youtube.com/watch?v=Wz4KghV8Kl8")

        elif 'open food by kgs' in query:
            speak("Opening food by kgs youtube channel")
            print(f"Opening food by kgs youtube channel")
            webbrowser.open("https://www.youtube.com/channel/UCxK9TugmWLb-3pyaqaM9JGQ")

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

        elif 'teams' in query:
            speak("Opening Teams")
            print("Opening Teams")
            webbrowser.open("https://teams.microsoft.com/_#/school/conversations/General?threadId=19:a5aae7e848224b9c9030fb2fe42aeda2@thread.tacv2&ctx=channel")

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

        elif 'google' in query:
            speak("What do u want to search??")
            a = input("What do u want to search:\n")
            time.sleep(3)
            webbrowser.open("https://google.com")
            x = 495
            y = 370
            pyautogui.moveTo(x, y, duration=1)
            time.sleep(2)
            pyautogui.click(x, y)
            speak(f"Writing {a} in google")
            time.sleep(1)
            pyautogui.write(a, interval=0.4)
            pyautogui.keyDown("enter")

        elif 'link' in query:
            speak("Write or paste the link:\n")
            b = input("Write or paste the link:\n")
            time.sleep(3)
            webbrowser.open_new_tab("https://google.com")
            z = 271
            o = 52
            pyautogui.moveTo(z, o, duration=1)
            time.sleep(2)
            pyautogui.click(z, o, clicks=3)
            speak(f"Writing {b} in google")
            time.sleep(1)
            pyautogui.write(b, interval=0.4)
            time.sleep(3)
            pyautogui.keyDown("enter")

        elif 'sign in to my account' in query:
            speak("Enter your username:")
            un = input("Enter your username:\n")
            speak("Enter your password:")
            pn = input("Enter your password:\n")
            speak(f"Signing to {un} google account")
            time.sleep(3)
            webbrowser.open_new("https://google.com")

            pyautogui.sleep(4)

            p = 438
            l = 49
            e = 689
            d = 377
            f = 776
            g = 567
            h = 696
            i = 425
            j = 774
            k = 496

            pyautogui.moveTo(p, l, duration=1)
            pyautogui.click(p, l)

            link = "https://accounts.google.com/signin/v2/identifier?service=accountsettings&continue=https%3A%2F%2Fmyaccount.google.com%2F&ec=GAlAwAE&flowName=GlifWebSignIn&flowEntry=AddSession"

            pyautogui.typewrite(link, interval=0.1)
            pyautogui.keyDown("enter")

            pyautogui.sleep(2)

            pyautogui.moveTo(e, d, duration=1)
            pyautogui.click(e, d, clicks=4)
            pyautogui.sleep(1)
            pyautogui.typewrite(un, interval=0.3)

            pyautogui.click(f, g, duration=1)

            pyautogui.moveTo(h, i, duration=1)
            pyautogui.click(h, i, clicks=4)
            pyautogui.sleep(1)
            pyautogui.typewrite(pn, interval=0.3)

            pyautogui.click(j, k, duration=1)