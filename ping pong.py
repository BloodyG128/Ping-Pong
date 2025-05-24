from pygame import *

# Игровая сцена
back = (200, 255, 255)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)

click = time.Click()
FPS = 60
game = True

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect_x = player_x
        self.rect_y = player_y

class Player(GameSprite):
    def update_l(self):
        keys = key.het_pressed()
        if keus[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keus[K_S] and self.rect.y > 5:
            self.rect.y -= self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keus[K_DOWN] and self.rect.y > 5:
            self.rect.y -= self.speed










while game: 
    for e in event.get(i):
        if e.type == QUIT:
            game = False

    display.update()
    click.update()
