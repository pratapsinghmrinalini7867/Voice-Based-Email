from flask import Flask
from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
from bs4 import BeautifulSoup

import os


app = Flask(__name__)

@app.route("/members")
def hello_world():
    return {"Data": "apple", "People": "Ram", "array": ["1", "2","3","4","5"]}


@app.route("/login")
def login():
    # tts = gTTS(text="Speak Now", lang='en',slow=False)
    # ttsname=("C:\\Users\Mrinalini Pratap\Desktop\sn.mp3") 
    # tts.save(ttsname)
    tts = gTTS(text="Email ID", lang='en',slow=False)
    ttsname=("C:\\Users\Mrinalini Pratap\Desktop\\a.mp3") 
    tts.save(ttsname)
    playsound("C:\\Users\Mrinalini Pratap\Desktop\\a.mp3")
    os.remove(ttsname)
    r = sr.Recognizer()
    with sr.Microphone() as source:
        playsound("C:\\Users\\Mrinalini Pratap\\Desktop\sn.mp3")
        audio=r.listen(source)
        print ("ok done!!")

    try:
        eid=r.recognize_google(audio)
        eid=eid.replace(" ","")
        eid=eid.lower()
        print ("You said : "+eid)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio.")

    tts = gTTS(text="Password", lang='en',slow=False)
    ttsname=("C:\\Users\Mrinalini Pratap\Desktop\\a.mp3") 
    tts.save(ttsname)
    playsound("C:\\Users\Mrinalini Pratap\Desktop\\a.mp3")
    os.remove(ttsname)

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print ("Password: ")
        playsound("C:\\Users\\Mrinalini Pratap\\Desktop\\sn.mp3")
        audio=r.listen(source)
        print ("ok done!!")

    try:
        pswd=r.recognize_google(audio)
        pswd=pswd.replace(" ","")
        pswd=pswd.lower()
        print ("You said : "+pswd)
        
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio.")
        
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e)) 
        
    return {"email": eid, "password": pswd}



@app.route("/menu")

def menu():
    tts = gTTS(text="Choose an option", lang='en',slow=False)
    ttsname=("C:\\Users\Mrinalini Pratap\Desktop\\b.mp3") 
    tts.save(ttsname)
    playsound("C:\\Users\\Mrinalini Pratap\\Desktop\\b.mp3")
    os.remove(ttsname)

    tts = gTTS(text="Check your Inbox", lang='en',slow=False)
    ttsname=("C:\\Users\Mrinalini Pratap\Desktop\\b.mp3") 
    tts.save(ttsname)
    playsound("C:\\Users\\Mrinalini Pratap\\Desktop\\b.mp3")
    os.remove(ttsname)

    tts = gTTS(text="Compose a mail", lang='en',slow=False)
    ttsname=("C:\\Users\Mrinalini Pratap\Desktop\\b.mp3") 
    tts.save(ttsname)
    playsound("C:\\Users\\Mrinalini Pratap\\Desktop\\b.mp3")
    os.remove(ttsname)

    tts = gTTS(text="Check Sent mails", lang='en',slow=False)
    ttsname=("C:\\Users\Mrinalini Pratap\Desktop\\b.mp3") 
    tts.save(ttsname)
    playsound("C:\\Users\\Mrinalini Pratap\\Desktop\\b.mp3")
    os.remove(ttsname)

    r = sr.Recognizer()
    with sr.Microphone() as source:
        playsound("C:\\Users\\Mrinalini Pratap\\Desktop\\sn.mp3")
        audio=r.listen(source)
        print ("ok done!!")

    try:
        choice=r.recognize_google(audio)
        choice=choice.replace(" ","")
        choice=choice.lower()
        print ("You said : "+ choice)
        
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio.")
        
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e)) 
        
    return {"choice": choice}


if __name__ == "__main__":
    app.run(debug=True)
