import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 150)    # Speed percent
engine.setProperty('volume', 0.9)  # Volume 0-1
engine.say("Good Night Shubhey")
engine.runAndWait()