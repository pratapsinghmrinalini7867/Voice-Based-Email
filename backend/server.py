from flask import Flask, request
from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
import smtplib
import email
import imaplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
from bson import json_util
import json
import re

def parse_json(data):
    return json.loads(json_util.dumps(data))

app = Flask(__name__)

login = os.getlogin
print ("You are logging from : "+login())

# Global email id and password variables
i = "0"
eid = ""
pswd = ""
file = "audio"
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
imap_url = 'imap.gmail.com'
conn = imaplib.IMAP4_SSL(imap_url)


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

def SpeechConvertor(text, filename):
    filename = filename + '.mp3'
    flag = True
    while flag:
        try:
            tts = gTTS(text=text, lang='en', slow=False)
            tts.save(filename)
            flag = False
        except:
            print('Trying again')
    playsound(filename)
    os.remove(filename)
    return

def TextConvertor():
    global i, addr, passwrd
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        playsound('Filename')
        audio = r.listen(source)
    try:
        response = r.recognize_google(audio)
    except:
        response = 'N'
    return response


@app.route("/login")
def Login():
    global eid, pswd, file, i
    
    playsound('Filename')
    
    flag = True
    while (flag):
        playsound('Filename')

        eid = TextConvertor()
        
        if eid != 'N':
            SpeechConvertor("You meant " + eid + " say yes to confirm or no to enter again", file + i)
            i = i + str(1)
            say = TextConvertor()
            if say == 'yes' or say == 'Yes':
                flag = False
        else:
            SpeechConvertor("could not understand what you meant:", file + i)
            i = i + str(1)


    eid = eid.strip()
    eid = eid.replace(' ', '')
    eid = eid.lower()
    eid = convert_special_char(eid)

    flag1 = True

    while flag1:
        playsound('Filename')

        pswd = TextConvertor()
        
        if pswd != 'N':
            SpeechConvertor("You meant " + pswd + " say yes to confirm or no to enter again", file + i)
            i = i + str(1)
            say = TextConvertor()
            print(say)
            if say == 'yes' or say == 'Yes':
                flag1 = False
        else:
            SpeechConvertor("could not understand what you meant:", file + i)
            i = i + str(1)


    pswd = pswd.strip()
    pswd = pswd.replace(' ', '')
    pswd = pswd.lower()
    pswd = convert_special_char(pswd)

    # connection to gmail account

    imap_url = 'imap.gmail.com'
    conn = imaplib.IMAP4_SSL(imap_url)
    try:
        conn.login(eid, pswd)
        s.login(eid, pswd)
        SpeechConvertor("Congratulations. You have logged in successfully. You will now be redirected to the menu page.", file + i)
        i = i + str(1)
        
        return {"email": eid, "password": pswd, "validity": True}

    except:
        SpeechConvertor("Invalid Login Details. Please try again.", file + i)
        i = i + str(1)
        return parse_json({'validity': False})
    

@app.route("/menu")
def menu():
    global eid, pswd, file, i
    flag = True

    while flag:
        playsound('Filename')

        say = TextConvertor()

        if say == "no" or say == "No":
            flag = False

    SpeechConvertor("Your Choice", file + i)
    i = i + str(1)

    choice = TextConvertor()
    choice = choice.strip()
    choice = choice.replace(' ', '')
    choice = choice.lower()
    print(choice)

    if choice == 'compose':
        return parse_json({'choice' : 'compose'})
    elif choice == 'inbox':
        return parse_json({'choice' : 'inbox'})
    elif choice == 'sent':
        return parse_json({'choice' : 'sent'})
    elif choice == 'trash':
        return parse_json({'choice' : 'trash'})
    
    elif choice == "logout":
        eid = ""
        pswd = ""
        SpeechConvertor("You have been logged out of your account and now will be redirected back to the login page.",file + i)
        i = i + str(1)
    else:
        SpeechConvertor("Invalid action. Please try again.", file + i)
        i = i + str(1)

    return {"choice": choice}


@app.route("/compose")
def Compose():
    global i, eid, pswd, s, item, subject, body
    if request.method == 'GET':
        text1 = "You have reached the page where you can compose and send an email. "
        SpeechConvertor(text1, file + i)
        i = i + str(1)
        flag = True
        flag1 = True
        fromaddr = eid
        toaddr = list()

        while flag1:
            while flag:
                SpeechConvertor("enter receiver's email address:", file + i)
                i = i + str(1)
                to = ""
                to = TextConvertor()
                if to != 'N':
                    
                    SpeechConvertor("You meant " + to + " say yes to confirm or no to enter again", file + i)
                    i = i + str(1)
                    say = TextConvertor()
                    if say == 'yes' or say == 'Yes':
                        toaddr.append(to)
                        flag = False
                else:
                    SpeechConvertor("could not understand what you meant", file + i)
                    i = i + str(1)
            SpeechConvertor("Do you want to enter more recipients ?  Say yes or no.", file + i)
            i = i + str(1)
            say1 = TextConvertor()
            if say1 == 'No' or say1 == 'no':
                flag1 = False
            flag = True

        newtoaddr = list()
        for item in toaddr:
            item = item.strip()
            item = item.replace(' ', '')
            item = item.lower()
            item = convert_special_char(item)
            newtoaddr.append(item)
            print(item)

        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = ",".join(newtoaddr)
        flag = True
        while (flag):
            SpeechConvertor("enter subject", file + i)
            i = i + str(1)
            subject = TextConvertor()
            if subject == 'N':
                SpeechConvertor("could not understand what you meant", file + i)
                i = i + str(1)
            else:
                flag = False
        msg['Subject'] = subject
        flag = True
        while flag:
            SpeechConvertor("enter body of the mail", file + i)
            i = i + str(1)
            body = TextConvertor()
            if body == 'N':
                SpeechConvertor("could not understand what you meant", file + i)
                i = i + str(1)
            else:
                flag = False

        msg.attach(MIMEText(body, 'plain'))

        SpeechConvertor("any attachment? say yes or no", file + i)
        i = i + str(1)
        x = TextConvertor()
        x = x.lower()
        print(x)
        if x == 'yes':
            SpeechConvertor("Do you want to record an audio and send as an attachment?", file + i)
            i = i + str(1)
            say = TextConvertor()
            say = say.lower()
            print(say)
            if say == 'yes':
                SpeechConvertor("Enter filename.", file + i)
                i = i + str(1)
                filename = TextConvertor()
                filename = filename.lower()
                filename = filename + '.mp3'
                filename = filename.replace(' ', '')
                print(filename)
                SpeechConvertor("Enter your audio message.", file + i)
                i = i + str(1)
                audio_msg = TextConvertor()
                flagconf = True
                while flagconf:
                    try:
                        tts = gTTS(text=audio_msg, lang='en', slow=False)
                        tts.save(filename)
                        flagconf = False
                    except:
                        print('Trying again')
                attachment = open(filename, "rb")
                p = MIMEBase('application', 'octet-stream')
                p.set_payload((attachment).read())
                encoders.encode_base64(p)
                p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
                msg.attach(p)
            elif say == 'no':
                SpeechConvertor("Enter filename with extension", file + i)
                i = i + str(1)
                filename = TextConvertor()
                filename = filename.strip()
                filename = filename.replace(' ', '')
                filename = filename.lower()
                filename = convert_special_char(filename)
                
                attachment = open(filename, "rb")
                p = MIMEBase('application', 'octet-stream')
                p.set_payload((attachment).read())
                encoders.encode_base64(p)
                p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
                msg.attach(p)

        try:
            s.sendmail(eid, msg['To'], msg.as_string())
            SpeechConvertor("Your email has been sent successfully. You will now be redirected to the menu page.", file + i)
            i = i + str(1)
        except:
            SpeechConvertor("Sorry, your email failed to send. please try again. You will now be redirected to the the compose page again.", file + i)
            i = i + str(1)
            return parse_json({'result': 'failure'})
        s.quit()

    return parse_json({"to": newtoaddr, "sub": subject, "desc": msg})

def get_body(msg):
    if msg.is_multipart():
        return get_body(msg.get_payload(0))
    else:
        return msg.get_payload(None, True)
    
def reply_mail(msg_id, message):
    global i,s
    TO_ADDRESS = message['From']
    FROM_ADDRESS = eid
    print(TO_ADDRESS + " " + FROM_ADDRESS)
    msg = email.mime.multipart.MIMEMultipart()
    msg['to'] = TO_ADDRESS
    msg['from'] = FROM_ADDRESS
    msg['subject'] = message['Subject']
    msg.add_header('In-Reply-To', msg_id)
    print(message['Subject'])
    flag = True
    while(flag):
        SpeechConvertor("Enter body.", file + i)
        i = i + str(1)
        body = TextConvertor()
        print(body)
        try:
            msg.attach(MIMEText(body, 'plain'))
            print("entered try block")
            s.sendmail(msg['from'], msg['to'], msg.as_string())
            print("after send")
            SpeechConvertor("Your reply has been sent successfully.", file + i)
            i = i + str(1)
            flag = False
        except:
            SpeechConvertor("Your reply could not be sent. Do you want to try again? Say yes or no.", file + i)
            i = i + str(1)
            act = TextConvertor()
            act = act.lower()
            if act != 'yes':
                flag = False

def frwd_mail(item, message):
    global i,s
    flag1 = True
    flag = True
    global i
    newtoaddr = list()
    while flag:
        while flag1:
            while True:
                SpeechConvertor("Enter receiver's email address", file + i)
                i = i + str(1)
                to = TextConvertor()
                SpeechConvertor("You meant " + to + " say yes to confirm or no to enter again", file + i)
                i = i + str(1)
                yn = TextConvertor()
                yn = yn.lower()
                if yn == 'yes':
                    to = to.strip()
                    to = to.replace(' ', '')
                    to = to.lower()
                    to = convert_special_char(to)
                    print(to)
                    newtoaddr.append(to)
                    break
            SpeechConvertor("Do you want to add more recepients?", file + i)
            i = i + str(1)
            ans1 = TextConvertor()
            ans1 = ans1.lower()
            print(ans1)
            if ans1 == "no" :
                flag1 = False

        message['From'] = eid
        message['To'] = ",".join(newtoaddr)
        try:
            s.sendmail(eid, newtoaddr, message.as_string())
            SpeechConvertor("Your mail has been forwarded successfully.", file + i)
            i = i + str(1)
            flag = False
        except:
            SpeechConvertor("Your mail could not be forwarded. Do you want to try again? Say yes or no.", file + i)
            i = i + str(1)
            act = TextConvertor()
            act = act.lower()
            if act != 'yes':
                flag = False

def read_mails(mail_list,folder):
    global s, i
    conn.login(eid, pswd)
    conn.select(folder)
    mail_list.reverse()
    mail_count = 0
    to_read_list = list()
    for item in mail_list:
        result, email_data = conn.fetch(item, '(RFC822)')
        raw_email = email_data[0][1].decode()
        message = email.message_from_string(raw_email)
        To = message['To']
        From = message['From']
        Subject = message['Subject']
        Msg_id = message['Message-ID']
        SpeechConvertor("Email number " + str(mail_count + 1) + "    .The mail is from " + From + " to " + To + "  . The subject of the mail is " + Subject, file + i)
        i = i + str(1)
        print('message id= ', Msg_id)
        print('From :', From)
        print('To :', To)
        print('Subject :', Subject)
        print("\n")
        to_read_list.append(Msg_id)
        mail_count = mail_count + 1

    flag = True
    while flag :
        n = 0
        flag1 = True
        while flag1:
            SpeechConvertor("Enter the email number of mail you want to read.",file + i)
            i = i + str(1)
            n = TextConvertor()
            print(n)
            SpeechConvertor("You meant " + str(n) + ". Say yes or no.", file + i)
            i = i + str(1)
            say = TextConvertor()
            say = say.lower()
            if say == 'yes':
                flag1 = False

        n = int(n)
        msgid = to_read_list[n - 1]
        print("message id is =", msgid)
        typ, data = conn.search(None, '(HEADER Message-ID "%s")' % msgid)
        data = data[0]
        result, email_data = conn.fetch(data, '(RFC822)')
        raw_email = email_data[0][1].decode()
        message = email.message_from_string(raw_email)
        To = message['To']
        From = message['From']
        Subject = message['Subject']
        Msg_id = message['Message-ID']
        print('From :', From)
        print('To :', To)
        print('Subject :', Subject)
        SpeechConvertor("The mail is from " + From + " to " + To + "  . The subject of the mail is " + Subject, file + i)
        i = i + str(1)
        Body = get_body(message)
        Body = Body.decode()
        Body = re.sub('<.*?>', '', Body)
        Body = os.linesep.join([s for s in Body.splitlines() if s])
        if Body != '':
            SpeechConvertor(Body, file + i)
            i = i + str(1)
        else:
            SpeechConvertor("Body is empty.", file + i)
            i = i + str(1)


        if folder == 'inbox':
            print("Want to reply?")
            SpeechConvertor("Do you want to reply to this mail? Say yes or no. ", file + i)
            i = i + str(1)
            ans = TextConvertor()
            ans = ans.lower()
            print(ans)
            if ans == "yes":
                reply_mail(Msg_id, message)

        if folder == 'inbox' or folder == 'sent':
            print("Do you want to forward this mail")
            SpeechConvertor("Do you want to forward this mail to anyone? Say yes or no. ", file + i)
            i = i + str(1)
            ans = TextConvertor()
            ans = ans.lower()
            print(ans)
            if ans == "yes":
                frwd_mail(Msg_id, message)


        if folder == 'inbox' or folder == 'sent':
            SpeechConvertor("Do you want to delete this mail? Say yes or no. ", file + i)
            i = i + str(1)
            ans = TextConvertor()
            ans = ans.lower()
            print(ans)
            if ans == "yes":
                try:
                    conn.store(data, '+X-GM-LABELS', '\\Trash')
                    conn.expunge()
                    SpeechConvertor("The mail has been deleted successfully.", file + i)
                    i = i + str(1)
                    print("mail deleted")
                except:
                    SpeechConvertor("Sorry, could not delete this mail. Please try again later.", file + i)
                    i = i + str(1)

        if folder == 'trash':
            print("want to delete this trash mail")
            SpeechConvertor("Do you want to delete this mail? Say yes or no. ", file + i)
            i = i + str(1)
            ans = TextConvertor()
            ans = ans.lower()
            print(ans)
            if ans == "yes":
                try:
                    conn.store(data, '+FLAGS', '\\Deleted')
                    conn.expunge()
                    SpeechConvertor("The mail has been deleted permanently.", file + i)
                    i = i + str(1)
                    print("mail deleted")
                except:
                    SpeechConvertor("Sorry, could not delete this mail. Please try again later.", file + i)
                    i = i + str(1)

        SpeechConvertor("Email ends here.", file + i)
        i = i + str(1)
        SpeechConvertor("Do you want to read more mails?", file + i)
        i = i + str(1)
        ans = TextConvertor()
        ans = ans.lower()
        if ans == "no":
            flag = False



@app.route("/inbox")
def Inbox():
    global i, file, eid, pswd

    imap_url = 'imap.gmail.com'
    conn = imaplib.IMAP4_SSL(imap_url)
    conn.login(eid, pswd)
    conn.select('"INBOX"')
    result, data = conn.search(None, '(UNSEEN)') # data represents all unseen mails in account, result is verifying if it is OK
    unread_list = data[0].split() # represents the unread mails in array format
    no = len(unread_list)
    result1, data1 = conn.search(None, "ALL") # data1 represents all mails in account, result1 is verifying if it is OK
    mail_list = data1[0].split()
    text = "You have reached your inbox. There are " + str(len(mail_list)) + " total mails in your inbox. You have " + str(no) + " unread emails" + ". To read unseen emails say unseen. To search a specific email say search. To go back to the menu page say back. To logout say logout."
    SpeechConvertor(text, file + i)

    i = i + str(1)

    flag = True

    while flag:
        action = TextConvertor()
        print(action)
        action = action.lower()
        if action == 'unseen':
            flag = False
            if no!=0:
                read_mails(unread_list,'inbox')
            else:
                SpeechConvertor("You have no unread emails.", file + i)
                i = i + str(1)

        elif action == 'search':
            flag = False
            emailid = ""
            while True:
                SpeechConvertor("Enter email ID of the person who's email you want to search.", file + i)
                i = i + str(1)
                emailid = TextConvertor()
                SpeechConvertor("You meant " + emailid + " say yes to confirm or no to enter again", file + i)
                i = i + str(1)
                yn = TextConvertor()
                yn = yn.lower()
                if yn == 'yes':
                    break
            emailid = emailid.strip()
            emailid = emailid.replace(' ', '')
            emailid = emailid.lower()
            emailid = convert_special_char(emailid)
            search_specific_mail('INBOX', 'FROM', emailid,'inbox')


        elif action == 'back':
            SpeechConvertor("You will now be redirected to the menu page.", file + i)
            i = i + str(1)
            conn.logout()
            return parse_json({"data": "back"})
        
        elif action == "logout"  or action == "log out":
            eid = ""
            pswd = ""
            SpeechConvertor("You have been logged out of your account and now will be redirected back to the login page.", file + i)
            i = i + str(1)
            return parse_json({"data": "logout"})

        else:
            SpeechConvertor("Invalid action. Please try again.", file + i)
            i = i + str(1)
            
        SpeechConvertor("If you wish to do anything else in the inbox or logout of your mail say yes or else say no.", file + i)
        i = i + str(1)
        ans = TextConvertor()
        ans = ans.lower()
        if ans == 'yes':
           flag = True
           SpeechConvertor("Enter your desired action. Say unseen, search, back or logout. ", file + i)
           i = i + str(1)
        
    SpeechConvertor("You will now be redirected to the menu page.", file + i)
    i = i + str(1)
    conn.logout()

    return parse_json({"data": "success"})

def search_specific_mail(folder,key,value,foldername):
    global i, conn
    conn.select(folder)
    result, data = conn.search(None,key,'"{}"'.format(value))
    mail_list=data[0].split()
    if len(mail_list) != 0:
        SpeechConvertor("There are " + str(len(mail_list)) + " emails with this email ID.", file + i)
        i = i + str(1)
    if len(mail_list) == 0:
        SpeechConvertor("There are no emails with this email ID.", file + i)
        i = i + str(1)
    else:
        print("You want to read this mail")
        read_mails(mail_list,foldername)


@app.route("/sentmails")
def Sentmails():
    global i, file, eid, pswd

    imap_url = 'imap.gmail.com'
    conn = imaplib.IMAP4_SSL(imap_url)
    conn.login(eid, pswd)
    conn.select('"[Gmail]/Sent Mail"')
    result1, data1 = conn.search(None, "ALL") # data1 represents all mails in account, result1 is verifying if it is OK
    mail_list = data1[0].split()
    text = "You have reached your sent mails folder. You have " + str(len(mail_list)) + " mails in your sent mails folder. To search a specific email say search. To go back to the menu page say back. To logout say logout."
    SpeechConvertor(text, file + i)
    print(text)

    i = i + str(1)

    flag = True

    while flag:
        action = TextConvertor()
        print(action)
        if action == 'search':
            flag = False
            emailid = ""
            while True:
                SpeechConvertor("Enter email ID of receiver.", file + i)
                i = i + str(1)
                emailid = TextConvertor()
                SpeechConvertor("You meant " + emailid + " say yes to confirm or no to enter again", file + i)
                i = i + str(1)
                yn = TextConvertor()
                yn = yn.lower()
                if yn == 'yes':
                    break
            emailid = emailid.strip()
            emailid = emailid.replace(' ', '')
            emailid = emailid.lower()
            emailid = convert_special_char(emailid)
            search_specific_mail('"[Gmail]/Sent Mail"', 'TO', emailid,'sent')
        elif action == 'back':
            SpeechConvertor("You will now be redirected to the menu page.", file + i)
            i = i + str(1)
            conn.logout()
            return parse_json({'result': 'back'})
        elif action == 'log out':
            eid = ""
            pswd = ""
            SpeechConvertor("You have been logged out of your account and now will be redirected back to the login page.", file + i)
            i = i + str(1)
            return parse_json({'result': 'logout'})
        else:
            SpeechConvertor("Invalid action. Please try again.", file + i)
            i = i + str(1)


        SpeechConvertor("If you wish to do anything else in the sent mails folder or logout of your mail say yes or else say no", file + i)
        i = i + str(1)
        say = TextConvertor()
        if say == "yes":
            flag = True
            SpeechConvertor("Enter your desired action. Say search, back or logout. ", file + i)
            i = i + str(1)

    SpeechConvertor("You will now be redirected to the menu page.", file + i)
    i = i + str(1)
    conn.logout()
    

    return parse_json({"data": "success"})    

@app.route("/trash")
def Trash():
    global i, eid, pswd, conn
    
    imap_url = 'imap.gmail.com'
    conn = imaplib.IMAP4_SSL(imap_url)
    conn.login(eid, pswd)
    conn.select('"[Gmail]/Trash"')
    result1, data1 = conn.search(None, "ALL")
    mail_list = data1[0].split()
    text = "You have reached your trash folder. You have " + str(len(mail_list)) + " mails in your trash folder. To search a specific email say search. To go back to the menu page say back. To logout say logout."
    SpeechConvertor(text, file + i)
    i = i + str(1)
    flag = True
    while (flag):
        act = TextConvertor()
        act = act.lower()
        print(act)
        if act == 'search':
            flag = False
            emailid = ""
            while True:
                SpeechConvertor("Enter email ID of sender.", file + i)
                i = i + str(1)
                emailid = TextConvertor()
                SpeechConvertor("You meant " + emailid + " say yes to confirm or no to enter again", file + i)
                i = i + str(1)
                yn = TextConvertor()
                yn = yn.lower()
                if yn == 'yes':
                    break
            emailid = emailid.strip()
            emailid = emailid.replace(' ', '')
            emailid = emailid.lower()
            emailid = convert_special_char(emailid)
            search_specific_mail('"[Gmail]/Trash"', 'FROM', emailid, 'trash')
        elif act == 'back':
            SpeechConvertor("You will now be redirected to the menu page.", file + i)
            i = i + str(1)
            conn.logout()
            return parse_json({'result': 'success'})
        elif act == 'log out':
            eid =""
            pswd = ""
            SpeechConvertor("You have been logged out of your account and now will be redirected back to the login page.",
                file + i)
            i = i + str(1)
            return parse_json({'result': 'logout'})
        else:
            SpeechConvertor("Invalid action. Please try again.", file + i)
            i = i + str(1)
        SpeechConvertor("If you wish to do anything else in the trash folder or logout of your mail say yes or else say no.", file + i)
        i = i + str(1)
        ans = TextConvertor()
        ans = ans.lower()
        print(ans)
        if ans == 'yes':
            flag = True
            SpeechConvertor("Enter your desired action. Say search, back or logout. ", file + i)
            i = i + str(1)
    SpeechConvertor("You will now be redirected to the menu page.", file + i)
    i = i + str(1)
    conn.logout()
    return parse_json({'result': 'back'})


if __name__ == "__main__":
     app.run(debug=True)
