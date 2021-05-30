import pyttsx3 #import pytsx3,pywin32 in needed
import datetime#in built 
import speech_recognition as sr #install speechRecognition,pyaudio if needed
import wikipedia  # install wikipdia 
import webbrowser
import sys
import os
import smtplib
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("good  morning   sir i am narayan how can i help you ,note please command me using my name")

        speak("good morning sir i am   narayan  how can i help you  ,  note please command me using my name")
    elif hour>=12 and hour<18:
        print("good afernoon sir  i an narayan how can i help you, note please command me using my name")
        speak("good afternoon sir i am     narayan how can i help you,   note please command me using my name ")

    else :
         print("good evening sir i am narayan how can i help you ,note please command me using my name")
         speak("good evening sir i am    narayan how can i help you  ,  note please command me using my name ")
def  takespeech():
    r=sr.Recognizer()
    with sr.Microphone() as source :
        print("listening........")
        r.pause_threshold =0.6
        r.energy_threshold=700
        audio = r.listen(source)
    try:
        query=r.recognize_google(audio, language ='en-in')
        print("user said :",query)
    except Exception :
        print("say that again ")
        return "None"
    return query
def sendmail():
    try:
        print("sir please enter the email address of  the receiver or end client :",end=" ")
        speak("sir please enter the email address of  the receiver or end client  ")
        to = input()
        speak("sir what message should i send ")
        content=takespeech()
        speak("email is being sending")
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.ehlo()
        server.starttls()
        server.login('narayanvijay2020@gmail.com','vijaynarayan2020@')
        server.sendmail('narayanvijay2020@gmail.com',to,content)
        server.close()
        speak("email has been send ")
    except Exception as e:
        print(e)
if __name__=='__main__':
    wishme()
    while(True):
        query=takespeech().lower()
        if "narayan" in query:
            query=query.replace("narayan"," ")
            if "wikipedia" in query :
                query=query.replace("wikipedia"," ")
                query=query.replace("narayan"," ")
                result=wikipedia.summary(query, sentences=2)
                print(result)
                speak("accoding to wikipedia")
                speak(result)
            elif "open youtube"   in query :
                webbrowser.open("youtube.com")
            elif "open facebook" in query :
                webbrowser.open("facebook.com")
            elif "open google" in query :
                webbrowser.open("google.com")
            elif "play genda phool" in query :
                webbrowser.open("https://youtu.be/SD4Z8dlZPd8")
            elif "open gmail"  in query :
                webbrowser.open("gmail.com")
            elif "time" in query :
               strtime1=datetime.datetime.now().strftime("%H:%M:%S")
               speak(f"sir the  time is {strtime1}")
            elif "date" in query :
               strtime2=datetime.datetime.now().strftime("%D")
               speak(f"sir  date is {strtime2}")
            elif "exit" in query :
               sys.exit()
            elif "play video song" in query :
                loc='./video songs' #folder location for video song 
                lst=os.listdir(loc)
                k=1
                for i in lst:
                    print(str(k)+" : "+str(i))
                    k=k+1
                speak("which song video would you like to play sir please enter  video number ")
                print("enter video no :",end=" ")
                n=int(input("enter video no :"))
                os.startfile(os.path.join(loc,lst[n-1]))
                
            elif "open netbeans" in query :
                try:
                    path="C:\\Program Files\\NetBeans 7.3\\bin\\netbeans64.exe"
                    os.startfile(path)
                except Exception :
                    print("error in opening")
            elif "open pycharm" in query :
                try:
                    path="C:\\Program Files\\JetBrains\\PyCharm Community Edition 2019.3\\bin\\pycharm64.exe"
                    os.startfile(path)
                except Exception :
                    print("error in opening")
            elif "send email" in query :
                sendmail()
            
                    
            

        
            

      
