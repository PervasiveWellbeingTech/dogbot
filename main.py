import speech_recognition as sr
from DogBot import DogBot


def main():

    dogbot = DogBot()
    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        while True:
            if not dogbot.isTalking():
                    print("Say something!")
                    audio = r.listen(source)
                    try:
                        dogbot.playThinking()
                        transcript = r.recognize_google(audio)
                        print("You said: " + transcript)
                        dogbot.determineResponse(transcript,
                                                 audio.get_wav_data())
                    except sr.UnknownValueError:
                        print("Could not understand audio")


if __name__ == "__main__":
    main()
