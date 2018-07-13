import os
import base64
from pygame import mixer
import deepaffects as da
from deepaffects.rest import ApiException

da.configuration.api_key['apikey'] = 'NL47UgAe2MvSk9N7O6CE4fqYM0XiNa4i'
_SOUND_DIR = "sfx"


class DogBot:
    name = ""
    sounds = {}
    er = None

    def __init__(self):
        self.loadSounds()
        self.initEmotionRecognizer()

    def loadSounds(self):
        """Load sound effect files.

        Initializes the pygame mixer and loads sound files from _SOUND_DIR
        into mixer Sound objects that can be accessed from the self.sounds
        dictionary. This prevents redundant loading of sound files.
        """
        mixer.init()
        for entry in os.scandir(_SOUND_DIR):
            if entry.name.endswith(".wav"):
                self.sounds[entry.path] = mixer.Sound(entry.path)

    def initEmotionRecognizer(self):
        self.er = da.EmotionApi()

    def playSound(self, soundPath):
        """Play a sound effect.

        Plays the sound effect that we have preloaded from the specified
        path.

        Arguments:
            soundPath {string} -- path of sound effect to play
        """
        self.sounds[soundPath].play()

    def recognizeEmotion(self, speech_audio):
        """Recognize the emotion for user speech input.

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
            return prediction.to_dict()
        except ApiException as e:
            print("Exception when calling EmotionApi->sync_recognise_emotion: {}\n".format(e))
            return None
