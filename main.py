import sys
from PIL import Image
import speech_recognition as sr
from DogBot import DogBot


def main():
    dogbot = DogBot(dogplus=True) if '-dogplus' in sys.argv else DogBot()
    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        dogImg = Image.open('img/dog.jpg')
        dogImg.show()
        while True:
            if not dogbot.isTalking():
                    print("Say something!")
                    audio = r.listen(source)
                    try:
                        transcript = r.recognize_google(audio)
                        print("You said: " + transcript)
                        dogbot.playThinking()
                        dogbot.determineResponse(transcript,
                                                 audio.get_wav_data())
                    except sr.UnknownValueError:
                        print("Could not understand audio")


if __name__ == "__main__":
    main()
