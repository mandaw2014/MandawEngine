# MandawEngine
A Game Engine Made in Python with the Turtle Module

# Installation
1) Download the zip
2) Extract the zip
3) Navigate to the folder in cmd or terminal and type
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

mandaw = Mandaw("title", width = 800, height = 600, bgcolor = "black")

while True:
    mandaw.run()
```
Make a simple square
```py
square = GameObject(shape = "square", color = "red", width = 1, height = 1)
```
