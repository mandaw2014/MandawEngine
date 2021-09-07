from mandaw import *


mandaw = Mandaw("Particles")
particle = ParticleSpawner(mandaw, 10, (100, 100), 20, (-2, 2), (-2, 2), 0.1, "white", True, 0, [])
# Args: window, particle count, position, size, velocityx, velocityy, shrink per frame, color, collide, gravity,
# collide_rects

# Randomizing:
# You can use randomize with particlespawner. You need to create list or tuple (eg. (min_value, max_value))
# You can use this feature only with particle count, size, velocityx, velocityy

# Collide: You can give collide to particles. You need give True value to collide arg.
# And you need to give GameObjects or Sprite.rect to collide_rects

while True:
    particle.draw()
    mandaw.run()