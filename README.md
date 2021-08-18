# MandawEngine
A Game Engine Made in Python with the Pygame Module

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

mandaw.run()
    
```
Make a simple square
```py
square = GameObject(mandaw, x = mandaw.width / 2 - 10, y = mandaw.height / 2 - 10, color = "red", width = 20, height = 20)
```
Draw it
```py
def update():
    square.draw()
```
# Full Code
```py
from mandaw import *

mandaw = Mandaw("First Mandaw Game")

square = GameObject(mandaw, x = mandaw.width / 2 - 10, y = mandaw.height / 2 - 10, color = "red", width = 20, height = 20)

def update():
    square.draw_rect()
    
mandaw.run()
```
