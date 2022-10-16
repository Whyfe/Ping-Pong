
from pygame import 8

class GameSprite (sprite.Sprite):
    def __init__ (self):
        pass
    def reset (self):
        pass
class Player (GameSprite):
    update_right (self):
        pass
    update_left (self):
        pass
win_width = 600
win_height = 500

window = win.set_mode ((win_width, win_height))

BLACK = (0, 0, 0)
window.fill (BLACK)

game = True
finish = False

clock = time.Clock()
FPS = 60

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.fill (BlACK)
    display.update ()
    clock.tick(FPS)         
