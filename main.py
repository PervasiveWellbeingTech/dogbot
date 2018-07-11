from pygame import mixer
import speech_recognition as sr

while True:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
        try:
            print("You said:- " + r.recognize_google(audio))
            print(type(audio))
        except sr.UnknownValueError:
            print("Could not understand audio")
