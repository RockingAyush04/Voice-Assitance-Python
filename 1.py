# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 14:39:05 2021

@author: Ayush Padhy
"""

import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia  
# from wiki_search import *
import sys
from datetime import date
import webbrowser 
import wolframalpha
import os
import re
import time

listener = sr.Recognizer()
engine = pyttsx3.init()
engine.say("Hello, I am Rocking the personal assistant !")
print("Hello, I am ROCKING, the personal assistant ! ")
engine.say("I am right now capable of playing songs, videos , Searching information, telling the time and many more....")
engine.runAndWait()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

from selenium import webdriver
import pyttsx3 as p

class info():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='C:/WebDrivers/chromedriver.exe')
    
    def get_info(self, query):
        self.query = query
        self.driver.get(url="https://www.wikipedia.org/")
        search = self.driver.find_element_by_xpath('//*[@id="searchInput"]')
        search.click()
        search.send_keys(query)
        
        enter = self.driver.find_element_by_xpath('//*[@id="search-form"]/fieldset/button')
        enter.click()
        
        info = self.driver.find_element_by_xpath('//*[@id="mw-content-text"]/div/p[2]')
        readable_text = info.text

def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            talk("i am Listening...say your command")
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'rocking' in command:
                print(command) 
    except:
        sys.exit()
        pass
    return command
        

        
def run_rocking():
    command = take_command()
    if 'rocking' in command:
        print(command)
        command = command.replace('rocking', '')
        if 'play' in command:
            song = command.replace('play', '') 
            talk('playing ' + song) 
            pywhatkit.playonyt(song) 
        elif 'time' in command: 
            time = datetime.datetime.now().strftime('%I:%M %p') 
            talk('Current time is ' + time) 
        elif 'who is' in command: 
            person = command.replace('who is', '')  
            rocking = info() 
            rocking.get_info(person)
        # info = wikipedia.summary(person, 1)
        # print(info)
        # talk(info)
        elif 'date' in command:
            today = str(date.today())
            print(date)
            talk('todays date is' + today)
 
        elif 'search' in command:

            search=command.replace('search','')
            talk('searching' + search)
            pywhatkit.search(search)
        elif "good" in command:
            talk("Thank you for your wishes... I am always trying to improve myself")
        elif "stop" in command:
            sys.exit()
        elif "live news" in command:
            webbrowser.open('https://www.republicworld.com/livetv.html')   
        elif "read news" in command:
            webbrowser.open("https://www.wionews.com/")
            time.sleep(3)
        elif 'ask' in command:
            talk('I can answer to computational and geographical questions  and what question do you want to ask now')
            command1 = take_command()
            print(command1)
            app_id="VWARHP-74AULHEGVG"
            client = wolframalpha.Client('R2K75H-7ELALHR35X')
            res = client.query(command1)
            answer = next(res.results).text
            talk(answer)
            print(answer) 
        elif "open minecraft" in command: 
            talk("minecraft") 
            os.startfile("C:\Program Files\Minecraft\TLauncher.exe") 
            return
            time.sleep(3)
        elif "open brave" in command:
            talk("brave")
            
            os.startfile("C:\Program Files\BraveSoftware\Brave-Browser\Application\Brave.exe")
            return


        else:
            talk('Please say the command again.') 

    
    
    

while True:
    run_rocking()