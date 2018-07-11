import os
from pygame import mixer

_SOUND_DIR = "sfx"


class DogBot:
    name = ""
    sounds = {}

    def __init__(self):
        self.loadSounds()

    def loadSounds(self):
        mixer.init()
        for entry in os.scandir(_SOUND_DIR):
            if entry.name.endswith(".wav"):
                self.sounds[entry.path] = mixer.Sound(entry.path)

    def playSound(self, soundPath):
        self.sounds[soundPath].play()
