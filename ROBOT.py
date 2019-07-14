import pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import os
import webbrowser
import wikipedia


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Artificial BOT. Please tell me how may I help you")

def takeCommand():
    #It takes microphone input and returns string 
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio=r.listen(source)
    try:
        print("Recognizing voice ......")
        question=r.recognize_google(audio,language='en-in')
        print(f"User said :...{question}\n")

    except Exception as e:
        # print(e)
        print("Speek again..")
        print("Type what you want to do")
        question=input()
        return question
    return question 

if __name__ == "__main__":
    wishMe()
    # takeCommand()
    if 1:
        task=takeCommand().lower()

        if 'about' in task:
            task = task.replace('about','')
            result = wikipedia.summary(task, sentences=2)
            speak("According to wikipedia ..")
            print(result)
            speak(result)
        elif 'wikipedia' in task:
            task = task.replace('wikipedia','')
            result = wikipedia.summary(task, sentences=2)
            speak("According to wikipedia ..")
            print(result)
            speak(result)
        elif 'open youtube' in task:
            webbrowser.open("youtube.com")
        elif 'open google' in task:
            webbrowser.open("https://www.google.com")
        elif 'open 4 wiki' in task:
            webbrowser.open("https://retailweb.us.oracle.com:8443/display/RGBUEnvironmentWiki/16.X+EIT4+(Clustered)#16.XEIT4(Clustered)-RMS")
        
        elif 'run scheduler' in task:
            automation_workspace = 'D:\\EIT_Automation_Workspace'
            direc = os.listdir(automation_workspace)
            print(direc)    
            os.startfile(os.path.join(automation_workspace,'run.bat'))
        elif 'open file' in task:
            automation_workspace = 'D:\\EIT_Automation_Workspace\\master'
            direc = os.listdir(automation_workspace)
            print(direc)    
            os.startfile(os.path.join(automation_workspace,'Execution_Controller.xlsx'))