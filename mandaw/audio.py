from pygame import mixer

class Audio:
    def __init__(self, file, volume):
        self.volume = volume

        self.audio = mixer.Sound(file)
        self.audio.set_volume(self.volume)

    def play(self):
        self.audio.play()

    def stop(self):
        self.audio.stop()
