#level up this game
import pygame
import random
from  pygame import mixer

#starting the mixer
mixer.init()


surf_color = (0, 142, 204)
color = (0,0,0)

#object class
class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super().__init__()

        self.image = pygame.surface([width, height])
        self.image.fill(surf_color)
        pygame.draw.rect(self.image, color, pygame.Rect(0,0, width, height))
        self.rect = self.image.get_rect()

        def moveRight(self, pixels):
            self.rect.x += pixels
        
        def moveLeft(self, pixels):
            self.rect.x -= pixels

        def moveForward(self, speed):
            self.rect.y += speed*speed/10

        def moveBack(self, speed):
            self.rect.y -= speed*speed/10
        
bg = pygame.image.load("bg.jpeg")
bg = pygame.transform.scale(bg, (500,400))

pygame.init()

screen = pygame.display.set_mode((500,400))
pygame.display.set_caption("sprite collision")

all_sprites_list = pygame.sprite.Group()

#Add a sprite
sp1 = Sprite(color, 20, 30)
sp1.rect.x = random.randint((0, 480))
sp1.rect.y = random.randint((0,370))
all_sprites_list.add(sp1)

# add one enemy
#set the random position
rad = 20
cxp = random.randint((0, 480))
cyp = random.randint((0,370))
sp2 = Sprite((255, 0, 0), 20, 30)
sp2.rect.x = cxp
sp2.rect.y = cyp
all_sprites_list.add(sp2)

exit = True
clock = pygame.time.Clock()

while exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = False
        elif event.type == pygame.KEYDOWN:
            if event.type == pygame.K_x:
                exit = False

    keys = pygame.key.get_pressed()
    if Keys[pygame.K_LEFT]:
        sp1.moveLeft(5)
    if Keys[pygame.K_RIGHT]:
        sp1.moveRight(5)
    if Keys[pygame.K_DOWN]:
        sp1.moveForward(5)
    if Keys[pygame.K_UP]:
        sp1.moveBack(5)
        