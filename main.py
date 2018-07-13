import speech_recognition as sr
from DogBot import DogBot


def main():

    dogbot = DogBot()
    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        while True:
            print("Say something!")
            audio = r.listen(source)
            try:
                print("You said:- " + r.recognize_google(audio))
                dogbot.playSound("sfx/whine1.wav")
                dogbot.recognizeEmotion(audio.get_wav_data())
            except sr.UnknownValueError:
                print("Could not understand audio")


if __name__ == "__main__":
    main()
