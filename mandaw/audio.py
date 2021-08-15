import os

class Audio:
    def __init__(self, path):
        super().__init__()

        os.system("afplay " + path + "&")