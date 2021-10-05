from mandaw import *
import sdl2.ext

mandaw = Mandaw("Pong", 800, 600)

BLACK = Color(0, 0, 0)
WHITE = Color(255, 255, 255)

PADDLE_SPEED = 3
BALL_SPEED = 4

class CollisionSystem(sdl2.ext.Applicator):
    def __init__(self, minx, miny, maxx, maxy):
        super().__init__()

        self.componenttypes = Velocity, sdl2.ext.Sprite
        self.ball = None
        self.minx = minx
        self.miny = miny
        self.maxx = maxx
        self.maxy = maxy

    def _overlap(self, item):
        sprite = item[1]
        if sprite == self.ball.sprite:
            return False

        left, top, right, bottom = sprite.area
        bleft, btop, bright, bbottom = self.ball.sprite.area

        return (bleft < right and bright > left and btop < bottom and bbottom > top)

    def process(self, world, componentsets):
        collitems = [comp for comp in componentsets if self._overlap(comp)]

        if len(collitems) != 0:
            self.ball.velocity.vx = -self.ball.velocity.vx

            sprite = collitems[0][1]
            ballcentery = self.ball.sprite.y + self.ball.sprite.size[1] // 2
            halfheight = sprite.size[1] // 2
            stepsize = halfheight // 10
            degrees = 0.7
            paddlecentery = sprite.y + halfheight

            if ballcentery < paddlecentery:
                factor = (paddlecentery - ballcentery) // stepsize
                self.ball.velocity.vy = -int(round(factor * degrees))

            elif ballcentery > paddlecentery:
                factor = (ballcentery - paddlecentery) // stepsize
                self.ball.velocity.vy = int(round(factor * degrees))

            else:
                self.ball.velocity.vy = -self.ball.velocity.vy

        if (self.ball.sprite.y <= self.miny or self.ball.sprite.y + self.ball.sprite.size[1] >= self.maxy):
            self.ball.velocity.vy = -self.ball.velocity.vy

        if (self.ball.sprite.x <= self.minx or self.ball.sprite.x + self.ball.sprite.size[0] >= self.maxx):
            self.ball.velocity.vx = -self.ball.velocity.vx

class MovementSystem(sdl2.ext.Applicator):
    def __init__(self, minx, miny, maxx, maxy):
        super().__init__()

        self.componenttypes = Velocity, sdl2.ext.Sprite
        self.minx = minx
        self.miny = miny
        self.maxx = maxx
        self.maxy = maxy

    def process(self, world, componentsets):
        for velocity, sprite in componentsets:
            swidth, sheight = sprite.size
            sprite.x += velocity.vx
            sprite.y += velocity.vy

            sprite.x = max(self.minx, sprite.x)
            sprite.y = max(self.miny, sprite.y)

            pmaxx = sprite.x + swidth
            pmaxy = sprite.y + sheight

            if pmaxx > self.maxx:
                sprite.x = self.maxx - swidth

            if pmaxy > self.maxy:
                sprite.y = self.maxy - sheight

class TrackingAIController(sdl2.ext.Applicator):
    def __init__(self, miny, maxy):
        super().__init__()
        self.componenttypes = PlayerData, Velocity, sdl2.ext.Sprite
        self.miny = miny
        self.maxy = maxy
        self.ball = None

    def process(self, world, componentsets):
        for pdata, vel, sprite in componentsets:
            if not pdata.ai:
                continue

            sheight = sprite.size[1]
            centery = sprite.y + sheight // 2

            if self.ball.velocity.vx < 0:
                if centery < self.maxy // 2 - PADDLE_SPEED:
                    vel.vy = PADDLE_SPEED
                elif centery > self.maxy // 2 + PADDLE_SPEED:
                    vel.vy = -PADDLE_SPEED
                else:
                    vel.vy = 0
            else:
                bcentery = self.ball.sprite.y + self.ball.sprite.size[1] // 2
                if bcentery < centery:
                    vel.vy = -PADDLE_SPEED
                elif bcentery > centery:
                    vel.vy = PADDLE_SPEED
                else:
                    vel.vy = 0

class Velocity(object):
    def __init__(self):
        super().__init__()
        self.vx = 0
        self.vy = 0

class PlayerData(object):
    def __init__(self):
        super().__init__()
        self.ai = False
        self.points = 0

class Player(GameObject):
    def __init__(self, world, x, y, ai=False):
        super().__init__(
            world,
            width = 20,
            height = 100,
            x = x,
            y = y
        )

        self.velocity = Velocity()
        self.playerdata = PlayerData()
        self.playerdata.ai = ai

class Ball(GameObject):
    def __init__(self, world, x = 0, y = 0):
        super().__init__(
            world,
            width = 20,
            height = 20,
            x = x,
            y = y
        )

        self.velocity = Velocity()

        self.xpos = x
        self.ypos = y

    def reset(self):
        self.x = 390
        self.y = 290

movement = MovementSystem(0, 0, 800, 600)
collision = CollisionSystem(0, 0, 800, 600)
aicontroller = TrackingAIController(0, 600)

mandaw.world.add_system(aicontroller)
mandaw.world.add_system(movement)
mandaw.world.add_system(collision)
mandaw.world.add_system(mandaw.sprite_renderer)

player1 = Player(mandaw.world, 0, 250, False)
player2 = Player(mandaw.world, 780, 250, True)

ball = Ball(mandaw.world, 390, 290)
ball.velocity.vx = -BALL_SPEED

collision.ball = ball
aicontroller.ball = ball

while True:
    for event in sdl2.ext.get_events():
        if event.type == mandaw.input.KEYDOWN:
            if event.key.keysym.sym == mandaw.input.UP:
                player1.velocity.vy = -PADDLE_SPEED
            elif event.key.keysym.sym == mandaw.input.DOWN:
                player1.velocity.vy = PADDLE_SPEED
        elif event.type == mandaw.input.KEYUP:
            if event.key.keysym.sym in (mandaw.input.UP, mandaw.input.DOWN):
                player1.velocity.vy = 0
    
    player1.draw()
    player2.draw()
    ball.draw()
    mandaw.run() 