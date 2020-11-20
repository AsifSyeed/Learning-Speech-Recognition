import speech_recognition as sr
from gtts import gTTS
import os

sp = sr.Recognizer()


i=0
while i<2:   
        try:
                
                with sr.Microphone() as source:
                        print("Speak: ")
                        audio = sp.listen(source)

                txt = sp.recognize_google(audio)
                if format(txt) == "say my name":
                        
                        reply="My name is Heisenberg"
                        print("You said : {}".format(txt))
                        lng='en'
                        output=gTTS(text=reply, lang=lng, slow=False)
                        output.save("output1.mp3")
                        os.system("start output1.mp3")
                        print(reply)
                        
                
                if format(txt) == "are you in danger":

                        reply="I'm not in danger. I'm the danger. I'm the one who knocks"
                        print("You said : {}".format(txt))
                        lng='en'
                        output=gTTS(text=reply, lang=lng, slow=False)
                        output.save("output2.mp3")
                        os.system("start output2.mp3")
                        print(reply)
                i+=1
        except:
                print("Can't understand")