'''
Original code:
https://github.com/idgmatrix/pygame-physics/blob/master/pygame_bouncing_ball.py
@author: kaswan

Modified:
@author: mandaw2014
'''

from mandaw import *

mandaw = Mandaw("Bouncing Ball!")

ball = GameObject(mandaw, "ellipse")
ball.center()

ballx, bally = mandaw.width / 2, mandaw.height / 2
vx, vy = 5, 5

while True:
    ballx += vx
    bally += vy

    if ballx < 0 or ballx > mandaw.width - 20:
        vx = -vx
    if bally < 0 or bally > mandaw.height - 20:
        vy = -vy

    ball.x = ballx
    ball.y = bally

    ball.draw()
    mandaw.run()