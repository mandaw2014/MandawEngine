.. _index:

****************************************
Mandaw Engine
****************************************

.. _dsg-introduction:

Introduction
============

Mandaw Engine is a 2D Game Engine made in Python with the Pygame Module

.. _dsg-installation:

Installation
------------
To install mandaw engine, open cmd or terminal and type

.. code-block:: rst
    
    pip install mandaw

or:

.. code-block:: rst
    
    pip3 install mandaw

.. _dsg-window:

Making a window
------------
First we import mandaw

.. code-block:: rst
    
    from mandaw import *

Then we call mandaw

.. code-block:: rst
    
    mandaw = Mandaw("title", width = 800, height = 800, bg_color = "cyan")

And then we run mandaw

.. code-block:: rst

    while True:
        mandaw.run()
