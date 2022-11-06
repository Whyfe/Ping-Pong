
from pygame import *
font.init()
lose1 = font.render("Player1 lose, 1, (255, 0, 0))
font = font.Font(None, 35)
class GameSprite (sprite.Sprite):
    def __init__ (self, palyer_image, p_x, p_y, p_speed, width, height):
        super.__init__()
        self.image = trnsform.scale(image.load(player_image),(width, height))
        self.speed = p_speed
        self.rect = self.image.get_rect()
        self.rect.x = p_x
        self.rect.y = p_y
        
    def reset (self):
        window.blit(self.image, (self.rect.x, self.rect.y))
        
class Player (GameSprite):
    update_right (self):
        keeys = key.get_pressed()
        if [K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if [K_DOWN] and self.rect.x < 420:
            self.rect.y += self.speed 
    update_left (self):
        keeys = key.get_pressed()
        if [K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if [K_s] and self.rect.x < 420:
            self.rect.y += self.speed
racket_right = Player("Line.png", 520, 200, 10, 50, 150)
racket_left = Player("Line.png", 80, 200, 10, 50, 150)

ball = GameSprite("ball.png", 200, 200, 6, 50, 50)
win_width = 600
win_height = 500

window = win.set_mode ((win_width, win_height))

WHITE = (255, 255, 255)
window.fill (WHITE)

game = True
finish = False

clock = time.Clock()
FPS = 60

speed_x = 3
speed_y = 3

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.fill (BlACK)
        racket_right.update_right()
        racket_left.update_left()
        
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.rect.y > win_height -50 or ball.rect_y < 0:
            speed_y *= -1
        if sprite.collide_recr(racket_right, ball) or sprite.collide_rect(racket_left, ball):
            speed_x *= -1
            speed_y *= -1
        if ball.rect.x < 0:
            finish = True
            game_over = True
        if ball.rect.x > 600:
            finish = True
            game_over = True
        racket_right.reset()
        racket_left.reset()
        ball.reset()
        
    display.update ()
    clock.tick(FPS)         
