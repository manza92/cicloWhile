import pyttsx3
import SpeechRecognition as sr
import webbrowser
import wikipedia

def speak(audio):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(audio)
    engine.runAndWait()

def Take_query():
    while(True):
        query = takeCommand().lower()
        if "open google" in query:
            speak("Opening Google")
            webbrowser.open("www.google.com")
            continue
        elif "bye" in query:
            speak("Bye. Check Out GFG for more exciting things")
            exit()
        elif "from wikipedia" in query:
            speak("Checking the wikipedia")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=4)
            speak("According to wikipedia")
            speak(result)

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening')
        r.pause_threshold = 0.7
        audio = r.listen(source)
        try:
            print("Recognizing")
            Query = r.recognize_google(audio, language='en-in')
            print("the command is printed=", Query)
        except Exception as e:
            print(e)
