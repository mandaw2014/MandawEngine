from pygame import mixer

class Audio:
    def __init__(self, file, volume):
        self.volume = volume

        mixer.Sound(file)
        mixer.Sound.set_volume(volume)

    def play(self):
        mixer.Sound.play()
    
    def pause(self):
        mixer.Sound.pause()

    def resume(self):
        mixer.Sound.unpause()

    def stop(self):
        mixer.Sound.stop()