from pygame import mixer
import speech_recognition as sr
from speech_recognition.__main__ import r, audio

while True:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Tell me something:")
        audio = r.listen(source)
        try:
            print("You said:- " + r.recognize_google(audio))
        except sr.UnknownValueError:
            print("Could not understand audio")
