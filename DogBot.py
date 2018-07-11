import os
from pygame import mixer

_SOUND_DIR = "sfx"


class DogBot:
    name = ""
    sounds = {}

    def __init__(self):
        self.loadSounds()

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

    def playSound(self, soundPath):
        """Play a sound effect.

        Plays the sound effect that we have preloaded from the specified
        path.

        Arguments:
            soundPath {[type]} -- path of sound effect to play
        """
        self.sounds[soundPath].play()
