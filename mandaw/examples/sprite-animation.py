from mandaw import *

m = Mandaw()

sp = sprite.Sprite(m, "assets/adventurer.png", 0, 0, (200, 200))
a = animation.Animation("assets/idle1", 0.14)
run_anim = animation.Animation("assets/normal-run", 0.14)
sp.add_animation(a, "idle")
sp.add_animation(run_anim, "run")


while True:
    sp.draw()
    if m.controls.is_key_pressed(m.keys["D"]):
        sp.play_animation("run")
        sp.x += 5
    elif m.controls.is_key_pressed(m.keys["A"]):
        sp.play_animation("run", "x")
        sp.x -= 5
    else:
        sp.play_animation("idle")

    m.run()