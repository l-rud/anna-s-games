from random import randint
from pgzero.builtins import Actor

score = 0
game_over = False
apple = Actor("apple")
pepper = Actor("pepper")

def draw():
    screen.clear()
    screen.fill("thistle")
    apple.draw()
    pepper.draw()
    screen.draw.text("Score: " + str(score), color="black", topleft=(10, 10))
    if game_over:
        screen.fill("maroon")
        screen.draw.text("Final Score: " + str(score), topleft=(10, 10), fontsize=60)

def place_actors():
    apple.x = randint(10, 800)
    apple.y = randint(10, 600)
    pepper.x = randint(10, 800)
    pepper.y = randint(10, 600)

def time_up():
    global game_over
    game_over = True

def on_mouse_down(pos):
    global score
    if game_over:
        return
    if apple.collidepoint(pos):
        print("Good shot!")
        score += 1
        place_actors()
    elif pepper.collidepoint(pos):
        print("Bad Shot")
        score -= 1
        place_actors()
    else:
        print("You missed!")

clock.schedule(time_up, 15.0)
place_actors()
