from mandaw import *
from player import Player
from enemy import Enemy
from main_menu import MainMenu
import random

mandaw = Mandaw("Chaos", bg_color = (77, 195, 255))

player = Player(mandaw)
player.dead()

main_menu = MainMenu(mandaw)

enemy = Enemy(mandaw, player, main_menu, x = random.randint(90, 625))
enemy1 = Enemy(mandaw, player, main_menu, x = random.randint(90, 625))
enemy2 = Enemy(mandaw, player, main_menu, x = random.randint(90, 625))

ground = GameObject(mandaw, shape = "rect", width = 600, height = 100, x = 0, y = 500, color = "gray")
ground.center_x()

lava = GameObject(mandaw, shape = "rect", width = 5000, height = 100, x = 0, y = 550, color = "orange")
lava.center_x()

platform1 = GameObject(mandaw, shape = "rect", width = 50, height = 10, x = 200, y = 460, color = (125, 125, 125))
platform2 = GameObject(mandaw, shape = "rect", width = 50, height = 10, x = 500, y = 460, color = (125, 125, 125))
platform1.center_x()
platform2.center_x()
platform1.x += 150
platform2.x -= 150

player.objects.append(ground)
player.objects.append(platform1)
player.objects.append(platform2)

while True:
    player.movement()
    player.jump()

    enemy.movement()
    enemy1.movement()
    enemy2.movement()

    if mandaw.controls.is_key_pressed(mandaw.keys["SPACE"]):
        main_menu.enabled = False

    if player.count > player.highscore_count:
        player.highscore_count = player.count

    if player.collide(lava):
        player.dead()
        main_menu.enabled = True
    if enemy.collide(lava):
        enemy.hit = True
    if enemy1.collide(lava):
        enemy1.hit = True
    if enemy2.collide(lava):
        enemy2.hit = True

    if player.enabled == False:
        if mandaw.controls.is_key_pressed(mandaw.keys["SPACE"]):
            player.enabled = True
            player.y = 300
            player.count = 0
            enemy.x = random.randint(90, 625)
            enemy1.x = random.randint(90, 625)
            enemy2.x = random.randint(90, 625)

    player.kills = Text(mandaw, str(player.count), 40, None, "white", 10)
    player.highscore = Text(mandaw, "Highscore: " + str(player.highscore_count), 40, None, "white")

    player.highscore.x = 320
    player.highscore.y = 400

    if player.enabled == True:
        player.draw()

    enemy.draw()
    enemy1.draw()
    enemy2.draw()

    if mandaw.controls.is_key_pressed(mandaw.keys["A"]) or mandaw.controls.is_key_pressed(mandaw.keys["D"]):
        if player.collide(enemy) and enemy.hit == False:
            enemy.hit = True
            player.count += 1
            player.hit.play()
        if player.collide(enemy1) and enemy1.hit == False:
            enemy1.hit = True
            player.count += 1
            player.hit.play()
        if player.collide(enemy2) and enemy.hit == False:
            enemy2.hit = True
            player.count += 1
            player.hit.play()
    
    ground.draw()
    lava.draw()
    platform1.draw()
    platform2.draw()

    player.kills.draw()

    if main_menu.enabled == True:
        player.highscore.draw()
        main_menu.title.draw()
        main_menu.instructions.draw()

    mandaw.run()