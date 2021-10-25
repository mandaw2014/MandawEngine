# MandawEngine
A Game Engine Made in Python with the Pygame Module

Discord: https://discord.gg/MPPqj9PNt3

# Installation
To Get The Latest Version of MandawEngine:
On Windows:
```
pip install https://github.com/mandaw2014/mandawengine/archive/master.zip
```
On Mac and Linux
```
pip3 install https://github.com/mandaw2014/mandawengine/archive/master.zip
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

mandaw.loop()
```
Make a simple square
```py
square = GameObject(window = mandaw, shape = "rect", x = 0, y = 0, color = "red", width = 20, height = 20)
```
Center it with
```py
square.center()
```
Draw it
```py
@mandaw.draw
def draw():
    square.draw()
```
# Full Code
```py
from mandaw import *

mandaw = Mandaw("First Mandaw Window!")

square = GameObject(window = mandaw, shape = "rect", x = 0, y = 0, color = "red", width = 20, height = 20)
square.center()

@mandaw.draw
def draw():
    square.draw()

mandaw.loop()
```
# Collisions Between GameObjects
What we have so far
```py
from mandaw import *

mandaw = Mandaw("Collisions!", bg_color = "cyan")

square = GameObject(window = mandaw, shape = "rect", x = 0, y = 0, color = "orange", width = 20, height = 30)
square.center()

ground = GameObject(window = mandaw, shape = "rect", x = 0, y = 0, color = "gray", width = 5000, height = 100)
ground.center()
ground.y = 500

@mandaw.draw
def draw():
    square.draw()
    ground.draw()   

mandaw.loop()
```
Here We Can Use The `collide()` Function along with the built in `update()` function. For example, We're Going To Make Gravity Here
```py
from mandaw import *

mandaw = Mandaw("Collisions!", bg_color = "cyan")

square = GameObject(window = mandaw, shape = "rect", x = 0, y = 0, color = "orange", width = 20, height = 30)
square.center()

ground = GameObject(window = mandaw, shape = "rect", x = 0, y = 0, color = "gray", width = 5000, height = 100)
ground.center()
ground.y = 500

@mandaw.draw
def draw():
    square.draw()
    ground.draw()   

@mandaw.update
def update(dt):
    # Collision code here
    if not square.collide(ground):
        # Square's y position += 1 x deltaTime
        square.y += 1 * dt

mandaw.loop()
```

# Platformer Controller Prefab
What we have so far
```py
from mandaw import *

mandaw = Mandaw("Platformer Example", bg_color = "cyan")

mandaw.loop()
```
Import the PlatformerController2D with
```py
from mandaw.prefabs.platformer_controller import PlatformerController2D
```
Then call it
```py
player = PlatformerController2D(mandaw, x = 0, y = 0, centered = True)
```
Then in the ```def update(dt)``` function, call
```py
@mandaw.update
def update(dt)
    player.movement(dt)
``` 
