import os
import re
import random
import base64
import time
from pygame import mixer
import indicoio
#import deepaffects as da
#from deepaffects.rest import ApiException
from settings import DEEP_AFFECTS_API_KEY, INDICOIO_API_KEY

indicoio.config.api_key = INDICOIO_API_KEY
#da.configuration.api_key['apikey'] = DEEP_AFFECTS_API_KEY
_SOUND_DIR = "sfx"


class DogBot:
    name = ""
    sounds = {}
    er = None
    dogplus = False

    def __init__(self, dogplus=False):
        self.dogplus = dogplus if dogplus else False
        self.loadSounds()
        #self.initEmotionRecognizer()

    def loadSounds(self):
        """Load sound effect files.

        Initializes the pygame mixer and loads sound files from _SOUND_DIR
        into mixer Sound objects that can be accessed from the self.sounds
        dictionary. This prevents redundant loading of sound files.
        """
        mixer.init()
        for entry in os.scandir(_SOUND_DIR):
            if entry.name.endswith(".wav"):
                emotionMatch = re.match('[a-z]+_', entry.name)
                if emotionMatch:
                    if 'dogplus' not in entry.name or self.dogplus:
                        self.sounds.setdefault(emotionMatch.group()[:-1], []) \
                                   .append(mixer.Sound(entry.path))

    def initEmotionRecognizer(self):
        self.er = da.EmotionApi()

    def determineResponse(self, speech_text, speech_audio):
        prediction = self.recognizeEmotionText(speech_text)

        # Fallback to analyzing the audio
        if prediction is None:
            # Audio analysis via DeepAffects has proven unreliable
            # prediction = self.recognizeEmotionAudio(speech_audio)
            prediction = 'neutral'

        if prediction in ['sad', 'sadness', 'fear']:
            self.playSound("sad")
        elif prediction in ['happy', 'joy', 'surprise']:
            self.playSound("happy")
        elif prediction in ['angry', 'anger', 'disgust']:
            self.playSound("angry")
        elif prediction == 'neutral':
            self.playSound("neutral")
        elif prediction == 'greeting':
            self.playSound("greeting")

    def playSound(self, soundCategory):
        """Play a dog sound effect from a given emotion category.

        Selects a random sound effect from the sounds we preloaded
        in a given emotion category and plays it.

        Arguments:
            soundCategory {string} -- emotion category of sfx to play
        """
        random.choice(self.sounds[soundCategory]).play()

    def playThinking(self):
        mixer.music.load("sfx/panting1.wav")
        mixer.music.play()

    def isTalking(self):
        return mixer.get_busy()

    def recognizeEmotionText(self, speech_text):
        """Recognize emotion in transcript of user speech.

        Currently using the Indico.io Text Analysis API for Emotion
        Classification.

        Arguments:
            speech_text {string} -- Transcript of what the user said.

        Returns:
            dict -- dict of predicted emotions and associated probabilities
        """
        greetings = ['hey', 'hi', 'hello', 'how are you']
        if any(greeting in speech_text.lower().split() for greeting in greetings):
            time.sleep(1)
            return 'greeting'
        textPredictions = indicoio.emotion(speech_text, threshold=0.4)
        print(textPredictions)
        if textPredictions:
            return max(textPredictions, key=textPredictions.get)
        else:
            return None

    def recognizeEmotionAudio(self, speech_audio):
        """Recognize emotion in audio of user speech.

        Takes in audio of a user speaking and returns a prediction for
        the emotion and its associated probability.

        Currently using the DeepAffects API for the emotion recognition
        step. As a result, the audio must be <2min and match the
        metadata variables declared below.

        Arguments:
            speech_audio {bytes} -- Audio of user talking.

        Returns:
            dict -- Contains the emotion and its probability score.
        """
        encoding = 'Wave'
        sample_rate = 44100
        language_code = 'en-US'
        content = base64.b64encode(speech_audio).decode('utf-8')

        body = da.Audio(encoding=encoding, sample_rate=sample_rate,
                        language_code=language_code, content=content)

        try:
            response = self.er.sync_recognise_emotion(body)
            prediction = max(response, key=lambda x: x.to_dict()['score'])
            print("Prediction: {}".format(prediction.to_str()))
            return prediction.to_dict()['emotion']
        except ApiException as e:
            print("Exception when calling EmotionApi->sync_recognise_emotion: {}\n".format(e))
            return None
