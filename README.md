# MandawEngine
A Game Engine Made in Python with the Pygame Module

Discord: https://discord.gg/MPPqj9PNt3

# Installation
To Install, type
```
pip install mandaw
```
To Get The Latest Version of MandawEngine:
1) Download the zip
2) Extract the zip
3) Navigate to the folder in cmd or terminal and type:

On Windows:
```
python setup.py install
```
On Mac and Linux
```
python3 setup.py install
```

# Getting Started
import Mandaw
```py
from mandaw import *
```

Make a window
```py
from mandaw import *

mandaw = Mandaw() 

while True:
    mandaw.run()
```
Make a simple square
```py
square = GameObject(mandaw, "rect", x = 0, y = 0, color = "red", width = 20, height = 20)
```
Center it with
```py
square.center()
```
Draw it
```py
while True:
    square.draw()
```
# Full Code
```py
from mandaw import *

mandaw = Mandaw("First Mandaw Game")

square = GameObject(mandaw, "rect", x = 0, y = 0, color = "red", width = 20, height = 20)
square.center()

while True:
    square.draw()
    mandaw.run()
```
# Collisions Between GameObjects
What we have so far
```py
from mandaw import *

mandaw = Mandaw("Collisions!", bg_color = "cyan")

square = GameObject(mandaw, "rect", x = 0, y = 0, color = "orange", width = 20, height = 30)
square.center()

ground = GameObject(mandaw, "rect", x = 0, y = 0, color = "gray", width = 5000, height = 100)
ground.center()
ground.y = 500

while True:
    square.draw()
    ground.draw()   

    mandaw.run()
```
Here We Can Use The `collide()` Function. For example, We're Going To Make Gravity Here
```py
from mandaw import *

mandaw = Mandaw("Collisions!", bg_color = "cyan")

square = GameObject(mandaw, "rect", x = 0, y = 0, color = "orange", width = 20, height = 30)
square.center()

ground = GameObject(mandaw, "rect", x = 0, y = 0, color = "gray", width = 5000, height = 100)
ground.center()
ground.y = 500

while True:
    # Collision code here
    if not square.collide(ground):
        # Square's y position += 1 x deltaTime
        square.y += 1 * mandaw.dt 

    square.draw()
    ground.draw()   

    mandaw.run()
```

# Platformer Controller Prefab
What we have so far
```py
from mandaw import *

mandaw = Mandaw("Platformer Example", bg_color = "cyan")

while True:
    mandaw.run()
```
Import the PlatformerController2D with
```py
from mandaw.prefabs.platformer_controller import PlatformerController2D
```
Then call it
```py
player = PlatformerController2D(mandaw, x = 0, y = 0, centered = True)
```
Then in the ```while True:``` loop, call
```py
while True:
    player.movement()
``` 
