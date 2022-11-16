from datetime import datetime
from functools import *
import os
from random import choice
import pyjokes
from threading import Thread
import pyttsx3 as pyt
import speech_recognition as speech
import wikipedia
import pyaudio
import webbrowser
import time
import subprocess
import requests
import json
import urlopen
import pywhatkit
import wolframalpha
from colorama import *
from pyautogui import *
import warnings
@cache
class voice_assistance():
    def __init__(self):
        self.dict = {
            'mother' : '+91 9717852486',
            'rohit' : '+91 7206154231',
            'monitor' : '+91 9205271827',
            'rahul' : '+91 9354664056',
            'kaif' : '+91 8130756130',
            'dad' : '+91 9871184586',
            'tauseef' : '+91 6203926236',
            'adil' or 'aadil' : '+91 9650679096'
        }
        self.engine = pyt.init()
        self.voices = self.engine.getProperty('voices')
        # print(self.voices)
        # self.engine.setProperty('voices',self.voices[33].id)
        self.engine.setProperty('rates',178)
        self.speak('jarvis activated!')
        self.wishme()
        # self.speak('I am jarvis sir, please tell me, how can i help you')
        self.impliment_command()
    def speak(self,audio):
        self.engine.say(audio)
        self.engine.runAndWait()
    def wishme(self):
        self.hour = int(datetime.datetime.now().hour)
        if self.hour>=0 and self.hour <12:
            self.speak('Good morning!')
        elif self.hour>=12 and self.hour<=18:
            self.speak('Good afternoon!')
        else:
            self.speak('Good evening!')
    def take_command(self):
        self.r = speech.Recognizer()
        with speech.Microphone() as source:
            print(Fore.CYAN+'[+] Listening...')
            self.r.pause_threshold = 1
            # self.r.energy_threshold = 1568
            # self.r.dynamic_energy_threshold = True
            self.r.adjust_for_ambient_noise(source,duration=0.2)
            self.audio1 = self.r.listen(source,timeout=6,phrase_time_limit=6)
            # print('.')
        try:
            print(Fore.YELLOW+'[*] Recognizing...')
            self.query1 = self.r.recognize_google(self.audio1,language='en-in')
            print(f'{Fore.GREEN}[*] user said :: {self.query1}')
        except Exception as e:
            self.speak('Sorry, I didn\'t understand')
            # self.i +=1
            return 'None'
        return self.query1
    def countdown(self,n):
        while n:
            self.mins, self.secs = divmod(n, 60)
            self.timer = '{:02d}:{:02d}'.format(self.mins, self.secs)
            print(self.timer, end="\r")
            time.sleep(1)
            n -= 1  
    def whatsapp(self):
        self.speak('please, tell the recipient name do you want to send message through whatsapp')
        self.name = self.take_command().lower()
        self.speak(f'please, tell me the message do you want to send {self.name}')
        self.message = self.take_command()
        if self.name not in self.dict:
            self.speak('Sorry, this name is not in our data set. Please try again!')
            if 'exit' in self.query:
                self.speak('exiting')
                if self.hour>=4 and self.hour<=19:
                    self.speak('Have a nice day, thank you')
                else:
                    self.speak('Good night, love. You are my most precious treasure')
                exit(0)
            if 'quit from whatsapp' in self.query:
                self.speak('exiting from whatsapp')
                self.impliment_command()
            else:
                self.whatsapp()
        else:
            self.min = int((datetime.now().minute)+2)
            pywhatkit.sendwhatmsg(self.dict[self.name],self.message,self.hour,self.min,15,True,2)
            self.speak(f'message sent to {self.name}')
    def impliment_command(self):
        while True:
            self.query = self.take_command().lower()
            # self.i = 0
            if 'wikipedia' in self.query:
                self.speak("Searching Wikipedia ...")
                self.query = self.query.replace("wikipedia", '')
                results = wikipedia.summary(self.query, sentences=2)
                self.speak("According to wikipedia")
                self.speak(results)
            if 'who are you' in self.query:
                self.speak("I am jarvis developed by sahil khan")
            if 'open youtube' in self.query:
                self.speak("opening youtube")
                webbrowser.open("youtube.com")
                # os.open('/home/kalikali/Desktop/chrome-aghbiahbpaijignceidepookljebhfak-Default.desktop')
            if 'open google' in self.query:
                self.speak("opening google")
                webbrowser.open("google.com")
            if 'duck duck go' in self.query or 'duckduckgo' in self.query:
                self.speak('Opening DuckDuckGo search engine in default browser!')
                webbrowser.open('duckduckgo.com')
            if 'open github' in self.query:
                self.speak("opening github")
                webbrowser.open("github.com")
            if 'open stack overflow' in self.query:
                self.speak("opening stackoverflow")
                webbrowser.open("stackoverflow.com")
            if 'open spotify' in self.query:
                self.speak("opening spotify")
                # webbrowser.open("spotify.com")
                self.spotify =subprocess.Popen('spotify')
            if 'close spotify' in self.query:
                self.speak('Closing spotify')
                self.spotify.terminate()
            if 'open whatsapp' in self.query:
                self.speak("opening whatsapp")
                loc = "https://web.whatsapp.com/"
                webbrowser.open(loc)
            if 'play music' in self.query:
                self.speak("opening music")
                webbrowser.open("spotify.com")
            if 'play music' in self.query:
                self.speak("opening music")
                webbrowser.open("spotify.com")
            if 'local disk d' in self.query:
                self.speak("opening local disk D")
                webbrowser.open("/")
            if 'local disk c' in self.query:
                self.speak("opening local disk C")
                webbrowser.open("/")
            if 'local disk e' in self.query:
                self.speak("opening local disk E")
                webbrowser.open("/")
            if 'open firefox' in self.query:
                self.speak('opening firefox')
                self.firefox = subprocess.Popen('firefox')
            if 'close firefox' in self.query:
                self.speak('closing firefox')
                self.firefox.terminate()
            if 'open screen recorder' in self.query:
                self.speak('opening screen recorder')
                self.obs=subprocess.Popen('obs')
            if 'close screen recorder' in self.query:
                self.speak('closing screen recorder')
                self.obs.terminate()
            if 'open genome calculator' in self.query:
                self.speak('opening calculator')
                self.gnome =subprocess.Popen('gnome-calculator')
            if 'close calculator' in self.query:
                if self.s:
                    self.gnome.terminate()
                else:
                    self.mate.terminate()
            if 'open mat calculator' in self.query:
                self.s = self.speak('opening mate calculator')              
                self.mate = subprocess.Popen('mate-calculator')
            if 'open file' in self.query:
                self.speak('opening file manager')
                self.file =subprocess.Popen('thunar')
            if 'close file' in self.query:
                self.speak('closing file manager')
                self.file.terminate()
            if 'open code' in self.query:
                self.speak('opening VS code')
                self.code = subprocess.Popen('code')
            if 'close code' in self.query:
                self.speak('Closing vs code')
                self.code.terminate()
            if 'open wps' in self.query:
                self.speak('opening WPS office')
                self.wps = subprocess.Popen('wps')
            if 'close wps' in self.query:
                self.speak('Closing WPS')
                self.wps.terminate()
            if 'exit' in self.query:
                self.speak('exiting')
                if self.hour>=4 and self.hour<=19:
                    self.speak('Have a nice day, thank you')
                else:
                    self.speak('Good night, love. You are my most precious treasure')
                exit(0)
            if 'open text editor' in self.query:
                self.speak('opening text editor')
                self.gedit = subprocess.Popen('gedit')
            if 'close text editor' in self.query:
                self.speak('closing text editor')
                self.gedit.terminate()
            if 'what is the time' in self.query:
                self.strtime = datetime.now().strftime('%H:%M:%S') 
                self.speak(f'Sir, the time is {self.strtime}')
            if 'how are you' in self.query:
                self.speak('I am fine, Thank you')
                self.speak('How are you, Sir')
            if 'fine' in self.query or 'good' in self.query or 'i am also fine' in self.query or 'i am fine' in self.query:
                self.speak('It\'s good to know that you are fine')
            if 'who made you' in self.query:
                self.speak('I have been created by sahil khan')
            if 'joke' in self.query:
                self.speak(pyjokes.get_joke())
            if 'who are you' in self.query:
                self.speak('I am virtual assistant created by sahil khan')
            if 'shutdown system' in self.query:
                self.speak('shuting down system')
                os.system('systemctl poweroff') 
            if 'reboot system' in self.query:
                self.speak('rebooting system')
                os.system('systemctl reboot')
                # subprocess.call(['shutdown','/r'])
            if 'hibernate system' in self.query:
                self.speak('hibernating system')
                subprocess.call(['shutdown ','/h'])
            if 'don\'t listen' in self.query or 'stop listening' in self.query:
                self.speak('How much time you want to stop jarvis from listening commands')
                self.n = int(self.take_command())
                self.speak(f'The jarvis will stop listening your commands for {self.n} seconds')
                # time.sleep(self.n)
                self.countdown(int(self.n))
                self.speak('Time over')
                self.n = 0
            if "weather" in self.query:
                # Google Open weather website
                # to get API of Open weather
                api_key = "Api key"
                base_url = "http://api.openweathermap.org / data / 2.5 / weather?"
                self.speak(" City name ")
                print("City name : ")
                city_name = self.take_command().lower()
                complete_url = base_url + "appid =" + api_key + "&q =" + city_name
                response = requests.get(complete_url)
                x = response.json()
                if x["code"] != "404":
                    y = x["main"]
                    current_temperature = y["temp"]
                    current_pressure = y["pressure"]
                    current_humidiy = y["humidity"]
                    z = x["weather"]
                    weather_description = z[0]["description"]
                    print(" Temperature (in kelvin unit) = " +str(current_temperature)+"\n atmospheric pressure (in hPa unit) ="+str(current_pressure) +"\n humidity (in percentage) = " +str(current_humidiy) +"\n description = " +str(weather_description))
                else:
                    self.speak(" City Not Found ")
            if 'news' in self.query:
                try:
                    jsonObj = urlopen('''https://newsapi.org / v1 / articles?source = the-times-of-india&sortBy = top&apiKey =\\times of India Api key\\''')
                    data = json.load(jsonObj)
                    i = 1
                    self.speak('here are some top news from the times of india')
                    print('''=============== TIMES OF INDIA ============'''+ '\n')
                    for item in data['articles']:
                        print(str(i) + '. ' + item['title'] + '\n')
                        print(item['description'] + '\n')
                        self.speak(str(i) + '. ' + item['title'] + '\n')
                        i += 1
                except Exception as e:
                    print(str(e))
            if 'hello jarvis' in self.query or 'hey jarvis' in self.query or 'hello' in self.query or 'hi' in self.query:
                self.wishme()
                self.speak('hello sir, I am jarvis, how can i help you')
            if 'thanks' in self.query or 'thank you' in self.query:
                self.reply = [
                    'My pleasure',
                    'You\'re Very Welcome',
                    'Always a Pleasure to Help',
                    'No problem.',
                    'Don\'t worry about it.',
                    'Happy to help',
                    'No big deal.',
                    'Anything for you.',
                    'That\'s OK'
                ]
                self.speak(choice(self.reply))
            if 'whatsapp' in self.query:
                self.whatsapp()
if __name__ =='__main__':
    try:
        warnings.filterwarnings("ignore")
        t1 = Thread(target=voice_assistance,name='t1')
        t1.start()
    except Exception as e:
        print(f'{Fore.RED}[!] Sorry some error occur. we are re-estabiling the voice assitance')
        voice_assistance()