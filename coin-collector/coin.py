from random import randint 
WIDTH = 400
HEIGHT = 400
score = 0
game_over = False
fox = Actor("fox")
fox.pos = 100, 100

coin = Actor("coin")
coin.pos = 200, 200

def draw():
    screen.fill("green")
    fox.draw()
    coin.draw()
    screen.draw.text("Score: " + str(score), color="black", topleft=(10, 10))

    if game_over:
        screen.fill("pink")
        screen.draw.text("Final Score: " + str(score), topleft=(10, 10), fontsize=60)

def place_coin():
    coin.x = randint(20, (WIDTH - 20))
    coin.y = randint(20, (HEIGHT - 20))
    pass

def time_up():
    global game_over
    game_over = True
    pass

def update():
    global score

    if keyboard.left:
        fox.x = fox.x - 4
    elif keyboard.right:
        fox.x = fox.x + 4
    elif keyboard.up:
        fox.y = fox.y - 4
    elif keyboard.down:
        fox.y = fox.y + 4

        coin_collected = fox.colliderect(coin)

    if fox.colliderect(coin):
        score += 1
        place_coin()
        
    pass

clock.schedule(time_up, 15.0)
place_coin()