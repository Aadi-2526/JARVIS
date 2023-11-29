import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

#print("Initializing Jarvis")
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
#
def speak(audio):
   engine.say(audio)
   engine.runAndWait()



def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak(Time)
    

def date():
    year = (datetime.datetime.now().year)
    month = (datetime.datetime.now().month)
    date = (datetime.datetime.now().day)
    speak(date)
    speak(month)
    speak(year)

def wishme():
    speak("welcome back sir!")
    
    hour = datetime.datetime.now().hour
    if hour>= 6 and hour<12:
        speak("Good Morning sir!")
    elif hour >=12 and hour<18:
        speak("Good Afternoon sir!")
    elif hour >=18 and hour<24:
        speak("Good Evening sir!")
    else:
        speak("Good Night sir!")
    
    #speak("the current time is")
    #time()
    #speak("today's date is")
    #date()
    #speak("you are looking awesome today")
    speak("this is jarvis,Please tell me how can i help you sir")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        
    try:
        print("Recognizing..")
        query = r.recognize_google(audio,language ='en-in')
        print(f"user said: {query}\n")
        
    except Exception as e:
        print("Say that again please")
        query = None
    return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com,')
    server.sendmail("harry@codewithharry.com",to,content)
    server.close()
takeCommand() 
wishme()

query = takeCommand()

#logic for executing tasks as per the query
if 'wikipedia' in query.lower():
    speak('Searching wikipedia...')
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query,sentences =2)
    print(results)
    speak(results)
    
elif 'open youtube' in query.lower():
    webbrowser.open("youtube.com") 
    
elif 'open google' in query.lower():
    webbrowser.open("google.com")
    
elif 'open whatsapp' in query.lower():
    webbrowser.open("whatsApp.com")
    
elif 'open facebook' in query.lower():
    webbrowser.open("facebook.com")
    
elif'play music' in query.lower():
    songs_dir = "C:\\Users\\Aaditya Tripathi\\Music"
    songs = os.listdir(songs_dir)
    print(songs)
    os.startfile(os.path.join(songs_dir,songs[0]))
    
elif'the time' in query.lower():
    speak("the current time is")
    time()
    
elif 'date' in query.lower():
    speak("sir the date is")
    date()
    
elif 'ok thank you'in query.lower():
    speak("your welcome sir")
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


        
        
        

        
        
