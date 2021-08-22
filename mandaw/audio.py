from pygame import mixer

class Audio:
    def __init__(self, file, volume):
        self.volume = volume

        mixer.Sound(file)
        mixer.Sound.set_volume(self.volume)

    def play(self):
        mixer.Sound.play()

    def stop(self):
        mixer.Sound.stop()
