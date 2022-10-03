import pyttsx3

engine = pyttsx3.init()
user = str(input('Type to text to speech: '))
engine.say(user)
engine.runAndWait()
