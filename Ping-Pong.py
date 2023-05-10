from pygame import *
from random import randint
from time   import time as tm

class GameSprite(sprite.Sprite):
    def __init__(self, img, x, y, sizeX, sizeY, speed=0):
        super().__init__()
        self.img = transform.scale(image.load(img), (sizeX, sizeY))
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    def reset(self):
        mw.blit(self.img, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def __init__(self, x, y, img, sizeX, sizeY, speed=0, id=0):
        super().__init__(img, (maxX - sizeX)//2, maxY - sizeY, sizeX, sizeY, speed)  
        self.id = id
        
    def keyProcessing(self):
        keys = key.get_pressed()
        if self.id == 1:
            if keys[K_LEFT]:
                self.rect.x -= self.speed
            if keys[K_RIGHT]:
                self.rect.x += self.speed
        else:
            if keys[K_a]:
                self.rect.x -= self.speed
            if keys[K_d]:
                self.rect.x += self.speed
    
        if self.rect.x > (maxX - self.rect.width):
            self.rect.x = (maxX - self.rect.width)
        elif self.rect.x < 0:
            self.rect.x = 0


maxX = 1280
maxY = 720
mw = display.set_mode((maxX, maxY))
display.set_caption('Ping Pong')


game = True
clock = time.Clock()
bg = GameSprite('background.jpg', 0, 0, maxX, maxY)

player1 = Player('red.png', maxX//2, 0  100, 25, 15, 1)
player2 = Player('blue.png', maxY, maxX//2 100, 25, 15, 2)

font.init()
font_ = font.SysFont(None, 70)###

Win1 = font_.render('Выйграл красный', True, (0, 255, 0))###
Win2 = font_.render('Выйграл синий', True, (0, 255, 0))###

gameRes = 0
while game:
    bg.reset()
    if gameRes == 0:
        player1.keyProcessing()
        player2.keyProcessing()  
        player1.reset()
        player2.reset()
    elif gameRes == 1:
        mw.blit(Win1, (maxX//2, maxY//2))
    else:
        mw.blit(Win2, (maxX//2, maxY//2))
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    display.update()
    clock.tick(60)