import speech_recognition as sr
import openai
import os
import win32com.client
import webbrowser 
import datetime
from apikey import ak
import random
import numpy as np


speaker = win32com.client.Dispatch("SAPI.SpVoice")
#while 1:
  #   speaker.Speak("how are u?")



chatStr = []
def chat(query):
    global chatStr
    print(chatStr)
    openai.api_key = ak
    
    chatStr.append({"role": "user", "content": query})
  
    response = openai.ChatCompletion.create(
     model="gpt-3.5-turbo",
     messages=chatStr,
     temperature=1,
     max_tokens=515,
     top_p=1,
     frequency_penalty=0,
     presence_penalty=0
)
    # todo: Wrap this inside of a  try catch block
    try:
        response_text = response['choices'][0]['message']['content']
        chatStr.append({"role": "assistant", "content": response_text})
        speaker.speak(response_text)

        return response_text
    except Exception as e:
        return "some error occured"



def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        #r.pause_threshold =  0.8
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occurred. Sorry from Jarvis"
if __name__=='__main__':
    print("hello")
    speaker.Speak("Hello sir")
    while True:
        print("listening...")
        query=takeCommand()


        sites=[["youtube","https://www.youtube.com"],["google","https://www.google.com"]]
        for site in sites:
            if f"open {site[0]}".lower() in query.lower():
               speaker.speak(f"Opening {site[0]}...")
               webbrowser.open(site[1])

            elif "open music".lower() in query:
                musicpath = r"C:\Users\nikhi\Downloads\man-across-the-spider-verse.mp3"
                speaker.speak("Opening music")
                os.startfile(musicpath)
 
            elif "the time".lower() in query:
                strfTime = datetime.datetime.now().strftime("%H:%M:%S")
                min = datetime.datetime.now().strftime("%M")
                speaker.speak(f"The time is {strfTime}")
        
        #if "Open teams".lower() in query:
         #   os.system(f"C:\Desktop\Display 2022-06-19 04-05-19.mp4")

            elif "reset chat".lower() in query.lower():
                 chatStr = ""
            elif "stop" in query.lower():
                 break
            else:
                print("Chatting...")
                chat(query)

           
    
    