# MandawEngine
A 2D Python GameEngine Made With PySDL2

Discord: https://discord.gg/MPPqj9PNt3

# Installation
To install:
Type in CMD or Terminal:
```
pip install mandaw
```
Or to download the latest version from github
Type in CMD or Terminal:
```
pip install https://github.com/mandaw2014/mandawenginesdl/archive/master.zip
```

# Creating A Window
First, import mandaw
```py
from mandaw import *
```
Call Mandaw
```py
mandaw = Mandaw(title = "Mandaw", width = 800, height = 600)
```
To run it, type
```py
while True:
    mandaw.run()
```

# Creating A Square
Here is what we have so far
```py
from mandaw import *

mandaw = Mandaw(title = "Mandaw", width = 800, height = 600)

while True:
    mandaw.run()
```
To create a square, type
```py
square = GameObject(window = mandaw, width = 20, height = 20, color = Color(255, 0, 0))
```
Then draw it
```py
while True:
    square.draw()
    ...
```
Like this
```py
from mandaw import *

mandaw = Mandaw(title = "Mandaw", width = 800, height = 600)

square = GameObject(mandaw, width = 20, height = 20, color = Color(255, 0, 0))

while True:
    square.draw()
    mandaw.run()
```

# Classes in MandawEngineSDL
Our starting template
```py
from mandaw import *

mandaw = Mandaw("Classes!", 800, 600)

while True:
    mandaw.run()
```
To make a GameObject class in MandawEngineSDL do:
```py
class Cube(GameObject):
    def __init__(self):
```
Next, make the `super().__init__()`
```py
super().__init__(
    window = mandaw,
    width = 20,
    height = 20,
    x = 0,
    y = 0,
    color = Color(0, 255, 255)
)
```
In the `__init__` funtion, you can also include `self.center()` or any other variables
```py
self.center()
```
When you want to call the class, you do
```py
cube = Cube()
```
And don't forget to draw it
```py
while True:
    cube.draw()
```
Full Code:
```py
from mandaw import *

mandaw = Mandaw("Classes!", 800, 600)

class Cube(GameObject):
    def __init__(self):
        super().__init__(
            window = mandaw,
            width = 20,
            height = 20,
            x = 0,
            y = 0,
            color = Color(0, 255, 255)
        )

        self.center()

cube = Cube()

while True:
    cube.draw()
    mandaw.run()
```
