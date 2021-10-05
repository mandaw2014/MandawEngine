import os

class Animation:
    def __init__(self, anim_folder, anim_time):
        self.frames = []
        self.anim_time = anim_time
        self.folder = anim_folder
        
        for f in os.listdir(anim_folder):
            if os.path.splitext(f)[1] == ".png":
                self.frames.append(f)

        self.frames = sorted(self.frames)
        self.count = len(self.frames)
