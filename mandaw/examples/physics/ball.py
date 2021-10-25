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

ball.ballx, ball.bally = mandaw.width / 2, mandaw.height / 2
ball.vx, ball.vy = 300, 300

@mandaw.draw
def draw():
    ball.draw()

@mandaw.update
def update(dt):
    ball.ballx += ball.vx * dt
    ball.bally += ball.vy * dt

    if ball.ballx < 0 or ball.ballx > mandaw.width - 20:
        ball.vx = -ball.vx
    if ball.bally < 0 or ball.bally > mandaw.height - 20:
        ball.vy = -ball.vy

    ball.x = ball.ballx
    ball.y = ball.bally

mandaw.loop()