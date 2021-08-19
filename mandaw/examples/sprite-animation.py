from mandaw import *

mandaw = Mandaw("Sprite Animation")

character = Sprite(window = mandaw, image = "assets/adventurer.png", x = 0, y = 0, size = (200, 200))
character.center()

animation = Animation("assets/idle1", 0.14)
run_anim = Animation("assets/normal-run", 0.14)

character.add_animation(animation, "idle")
character.add_animation(run_anim, "run")

while True:
    character.draw()
    if mandaw.controls.is_key_pressed(mandaw.keys["D"]):
        character.play_animation("run")
        character.x += 5
    elif mandaw.controls.is_key_pressed(mandaw.keys["A"]):
        character.play_animation("run", "x")
        character.x -= 5
    else:
        character.play_animation("idle")

    mandaw.run()
