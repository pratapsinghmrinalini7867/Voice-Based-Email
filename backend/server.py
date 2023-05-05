from flask import Flask, request, json
from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
from bs4 import BeautifulSoup
import os
import pymongo
from datetime import datetime
from bson import json_util, ObjectId

def parse_json(data):
    return json.loads(json_util.dumps(data))

app = Flask(__name__)

# Global email id and password variables
eid = ""
pswd = ""


def convert_special_char(text):
    temp=text
    special_chars = ['attherate','dot','underscore','dollar','hash','star','plus','minus','space','dash']
    for character in special_chars:
        while(True):
            pos=temp.find(character)
            if pos == -1:
                break
            else :
                if character == 'attherate':
                    temp=temp.replace('attherate','@')
                elif character == 'dot':
                    temp=temp.replace('dot','.')
                elif character == 'underscore':
                    temp=temp.replace('underscore','_')
                elif character == 'dollar':
                    temp=temp.replace('dollar','$')
                elif character == 'hash':
                    temp=temp.replace('hash','#')
                elif character == 'star':
                    temp=temp.replace('star','*')
                elif character == 'plus':
                    temp=temp.replace('plus','+')
                elif character == 'minus':
                    temp=temp.replace('minus','-')
                elif character == 'space':
                    temp = temp.replace('space', '')
                elif character == 'dash':
                    temp=temp.replace('dash','-')
    return temp

@app.route("/login")
def login():
    global eid, pswd
    playsound("<filename>")

    r = sr.Recognizer()
    with sr.Microphone() as source:
        playsound("<filename>")
        audio=r.listen(source)
        print ("ok done!!")
    try:
        eid=r.recognize_google(audio)
        eid=eid.replace(" ","")
        eid=eid.lower()
        print ("You said : "+eid)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio.")

    playsound("<filename>")

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print ("Password: ")
        playsound("<filename>")
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

    isValid = False
    obj = collection.find_one({"username": eid,"password": pswd})
    if obj:
        isValid = True
    else:
        tts = gTTS(text="Wrong email id or password, please speak again", lang='en',slow=False)
        ttsname=("<filename>") 
        tts.save(ttsname)
        playsound("<filename>")
        os.remove(ttsname)

        
    return {"email": eid, "password": pswd, "validity": isValid}

@app.route("/menu")

def menu():
    playsound("<filename>")

    r = sr.Recognizer()
    with sr.Microphone() as source:
        playsound("<filename>")
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

@app.route("/compose")
def Compose():
    to_id = ""
    sub = ""
    desc = ""

    playsound("<filename>")

    r = sr.Recognizer()
    with sr.Microphone() as source:
        playsound("<filename>")
        audio=r.listen(source)
        print ("ok done!!")

    try:
        to_id=r.recognize_google(audio)
        to_id=to_id.replace(" ","")
        to_id=to_id.lower()
        print ("You said : "+ to_id)
        
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio.")
        
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e)) 

    playsound("<filename>")

    r = sr.Recognizer()
    with sr.Microphone() as source:
        playsound("<filename>")
        audio=r.listen(source)
        print ("ok done!!")

    try:
        sub=r.recognize_google(audio)
        sub=sub.replace(" ","")
        sub=sub.lower()
        print ("You said : "+ sub)
        
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio.")
        
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e)) 

    playsound("<filename>")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        playsound("<filename>")
        audio=r.listen(source)
        print ("ok done!!")

    try:
        desc=r.recognize_google(audio)
        desc=desc.replace(" ","")
        desc=desc.lower()
        print ("You said : "+ desc)
        
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio.")
        
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e)) 

    to_id = convert_special_char(to_id)

    dic = {"to": to_id, "subject": sub, "description": desc, "date_created": datetime.utcnow()}
    collection1.insert_one(dic)
    
    tts = gTTS(text='Mail successfully sent. Going back', lang='en', slow=False)
    ttsname = ("C:\\Users\\prata\\OneDrive\\Desktop\\Project\\Voice Folder\\f.mp3")
    tts.save(ttsname)
    playsound("C:\\Users\\prata\\OneDrive\\Desktop\\Project\\Voice Folder\\f.mp3")
    os.remove(ttsname)

    return {"to": to_id, "sub": sub, "desc": desc}

@app.route("/inbox")
def Inbox():
    mails = collection2.find()
    improved_emails = parse_json(mails)
    
    for dic in improved_emails:
        tts = gTTS(text='from', lang='en', slow=False)
        ttsname = ("C:\\Users\\prata\\OneDrive\\Desktop\\Project\\Voice Folder\\f.mp3")
        tts.save(ttsname)
        playsound("C:\\Users\\prata\\OneDrive\\Desktop\\Project\\Voice Folder\\f.mp3")
        os.remove(ttsname)


        tts = gTTS(text=dic['from'], lang='en', slow=False)
        ttsname = ("C:\\Users\\prata\\OneDrive\\Desktop\\Project\\Voice Folder\\f.mp3")
        tts.save(ttsname)
        playsound("C:\\Users\\prata\\OneDrive\\Desktop\\Project\\Voice Folder\\f.mp3")
        os.remove(ttsname)

        tts = gTTS(text='subject', lang='en', slow=False)
        ttsname = ("C:\\Users\\prata\\OneDrive\\Desktop\\Project\\Voice Folder\\f.mp3")
        tts.save(ttsname)
        playsound("C:\\Users\\prata\\OneDrive\\Desktop\\Project\\Voice Folder\\f.mp3")
        os.remove(ttsname)

        tts = gTTS(text=dic['subject'], lang='en', slow=False)
        ttsname = ("C:\\Users\\prata\\OneDrive\\Desktop\\Project\\Voice Folder\\f.mp3")
        tts.save(ttsname)
        playsound("C:\\Users\\prata\\OneDrive\\Desktop\\Project\\Voice Folder\\f.mp3")
        os.remove(ttsname)

        tts = gTTS(text='Message', lang='en', slow=False)
        ttsname = ("C:\\Users\\prata\\OneDrive\\Desktop\\Project\\Voice Folder\\f.mp3")
        tts.save(ttsname)
        playsound("C:\\Users\\prata\\OneDrive\\Desktop\\Project\\Voice Folder\\f.mp3")
        os.remove(ttsname)

        tts = gTTS(text=dic['description'], lang='en', slow=False)
        ttsname = ("C:\\Users\\prata\\OneDrive\\Desktop\\Project\\Voice Folder\\f.mp3")
        tts.save(ttsname)
        playsound("C:\\Users\\prata\\OneDrive\\Desktop\\Project\\Voice Folder\\f.mp3")
        os.remove(ttsname)

        tts = gTTS(text='Date Recieved', lang='en', slow=True)
        ttsname = ("C:\\Users\\prata\\OneDrive\\Desktop\\Project\\Voice Folder\\f.mp3")
        tts.save(ttsname)
        playsound("C:\\Users\\prata\\OneDrive\\Desktop\\Project\\Voice Folder\\f.mp3")
        os.remove(ttsname)

        time = dic['date_created']['$date']
        print(time)

        tts = gTTS(text=time, lang='en', slow=True)
        ttsname = ("C:\\Users\\prata\\OneDrive\\Desktop\\Project\\Voice Folder\\f.mp3")
        tts.save(ttsname)
        playsound("C:\\Users\\prata\\OneDrive\\Desktop\\Project\\Voice Folder\\f.mp3")
        os.remove(ttsname)
    
    print(improved_emails)
    return  improved_emails

@app.route("/sentmails")
def Sentmails():
    mails = collection1.find()
    improved_emails = parse_json(mails)
    
    for dic in improved_emails:
        tts = gTTS(text='from', lang='en', slow=False)
        ttsname = ("C:\\Users\\prata\\OneDrive\\Desktop\\Project\\Voice Folder\\f.mp3")
        tts.save(ttsname)
        playsound("C:\\Users\\prata\\OneDrive\\Desktop\\Project\\Voice Folder\\f.mp3")
        os.remove(ttsname)


        tts = gTTS(text=dic['from'], lang='en', slow=False)
        ttsname = ("C:\\Users\\prata\\OneDrive\\Desktop\\Project\\Voice Folder\\f.mp3")
        tts.save(ttsname)
        playsound("C:\\Users\\prata\\OneDrive\\Desktop\\Project\\Voice Folder\\f.mp3")
        os.remove(ttsname)

        tts = gTTS(text='subject', lang='en', slow=False)
        ttsname = ("C:\\Users\\prata\\OneDrive\\Desktop\\Project\\Voice Folder\\f.mp3")
        tts.save(ttsname)
        playsound("C:\\Users\\prata\\OneDrive\\Desktop\\Project\\Voice Folder\\f.mp3")
        os.remove(ttsname)

        tts = gTTS(text=dic['subject'], lang='en', slow=False)
        ttsname = ("C:\\Users\\prata\\OneDrive\\Desktop\\Project\\Voice Folder\\f.mp3")
        tts.save(ttsname)
        playsound("C:\\Users\\prata\\OneDrive\\Desktop\\Project\\Voice Folder\\f.mp3")
        os.remove(ttsname)

        tts = gTTS(text='Message', lang='en', slow=False)
        ttsname = ("C:\\Users\\prata\\OneDrive\\Desktop\\Project\\Voice Folder\\f.mp3")
        tts.save(ttsname)
        playsound("C:\\Users\\prata\\OneDrive\\Desktop\\Project\\Voice Folder\\f.mp3")
        os.remove(ttsname)

        tts = gTTS(text=dic['description'], lang='en', slow=False)
        ttsname = ("C:\\Users\\prata\\OneDrive\\Desktop\\Project\\Voice Folder\\f.mp3")
        tts.save(ttsname)
        playsound("C:\\Users\\prata\\OneDrive\\Desktop\\Project\\Voice Folder\\f.mp3")
        os.remove(ttsname)

        tts = gTTS(text='Date Recieved', lang='en', slow=True)
        ttsname = ("C:\\Users\\prata\\OneDrive\\Desktop\\Project\\Voice Folder\\f.mp3")
        tts.save(ttsname)
        playsound("C:\\Users\\prata\\OneDrive\\Desktop\\Project\\Voice Folder\\f.mp3")
        os.remove(ttsname)

        time = dic['date_created']['$date']
        print(time)

        tts = gTTS(text=time, lang='en', slow=True)
        ttsname = ("C:\\Users\\prata\\OneDrive\\Desktop\\Project\\Voice Folder\\f.mp3")
        tts.save(ttsname)
        playsound("C:\\Users\\prata\\OneDrive\\Desktop\\Project\\Voice Folder\\f.mp3")
        os.remove(ttsname)
    
    return  improved_emails

@app.route('/viewonemail', methods = ['POST'])
def get_query_from_react():
    data = json.loads(request.data)
    
    mail_collected = collection1.find_one({'_id': ObjectId(data['content'])})
    if mail_collected:
        return parse_json(mail_collected)
    else:
        mail_collected = collection2.find_one({'_id': ObjectId(data['content'])})
        return parse_json(mail_collected)


if __name__ == "__main__":
     print("Connected to database")
     client = pymongo.MongoClient("<connectionString>")
     print(client)
     db = client['emails']
     collection = db['login']
     collection1 = db['sentMails']
     collection2 = db['inbox']
     app.run(debug=True)
