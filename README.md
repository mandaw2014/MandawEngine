# MandawEngine
A Game Engine Made in Python with the Pygame Module

# Installation
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
from mandaw import *

mandaw = Mandaw("First Mandaw Game")

square = GameObject(mandaw.window, x = mandaw.width / 2 - 10, y = mandaw.height / 2 - 10, color = "red", width = 20, height = 20)

while True:
    square.draw_rect()
    
    mandaw.run()
```
