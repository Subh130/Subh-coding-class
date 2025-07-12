import pygame
import random

#initialize program
pygame.init()

#set custom IDs for color change event
SPRITE_COLOR_CHANGE_EVENT = pygame.USEREVENT + 1
BACKGROUND_COLOR_CHANGE_EVENT = pygame.USEREVENT + 2

#define basic color using pygame.color
#Background colors
BLUE = pygame.Color("blue")
LIGHTBLUE = pygame.Color("lightblue")
DARKBLUE = pygame.Color("darkblue")

#sprite colors
YELLOW = pygame.Color("yellow")
MAGENTA = pygame.Color("magenta")
ORANGE = pygame.Color("orange")
WHITE = pygame.Color("white")

#sprite class representing the moiving object
class Sprite(pygame.sprite.Sprite):
    #constructor method
    def __init__(self, color, height, width):
        super().__init__()

        #create the sprites surface with dimentions and colors
        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        #get the sprites rect defining its position and size
        self.rect = self.image.get_rect()

        #set initial velocity with random direction
        self.velocity = [random.choice([-1,1]), random.choice([-1,1])]

    #method to update the sprites position
    def update(self):
        #move the sprite by its velocity
        self.rect.move_ip(self.velocity)

        #flag to track if the sprite hits a bouandry
        bouantry_hit = False

        #check for collision with left or right bouandaries and reverse direction
        if self.rect.left <= 0 or self.rect.right >= 500:
            self.velocity [0] = -self.velocity[0]
            bouantry_hit = True

        #check for collission with top or bottom bouandaries and reverse direction
        if self.rect.top <= 0 or self.rect.bottom >= 400:
            self.velocity [1] = -self.velocity[1]
            bouantry_hit = True
        
        #if a bouandry was hit, post events to change color
        if bouantry_hit:
            pygame.event.post(pygame.event.Event(SPRITE_COLOR_CHANGE_EVENT))
            pygame.event.post(pygame.event.Event(BACKGROUND_COLOR_CHANGE_EVENT))

    #method to change the sprites color 
    def change_color(self):
        self.image.fill(random.choice([YELLOW,MAGENTA,ORANGE,WHITE]))

#function to change background color 
def change_background_color():
    global bg_color
    bg_color = random.choice([BLUE, LIGHTBLUE, DARKBLUE ])

#create a group to hold the sprite
all_sprite_list = pygame.sprite.Group()

#instantize the sprite 
sp1 = Sprite(WHITE, 20, 30)

#randomly position the sprite
sp1.rect.x = random.randint(0 , 480)
sp1.rect.y = random.randint(0,370)

#add the sprite to the group
all_sprite_list.add(sp1)

#create the game window
screen = pygame.display.set_mode((500, 400))

#set the window title
pygame.display.set_caption("Bouandry sprite")

#set the initial background color
bg_color = BLUE

#apply the background color
screen.fill(bg_color)

#game loop control flag
exit = False

#create a clock object to control the frame rate
clock = pygame.time.Clock()

#main game loop
while not exit:

    #event loop handling
    for event in pygame.event.get():

        #if the windows close button is clicked exit the game
        if event.type == pygame.QUIT:
            exit = True
        
        #if the sprite color change event is triggered , change the background color
        elif event.type == SPRITE_COLOR_CHANGE_EVENT:
            sp1.change_color()

        elif event.type  == BACKGROUND_COLOR_CHANGE_EVENT:
            change_background_color()

    #update all sprites
    all_sprite_list.update()

    #fill the screen
    screen.fill(bg_color)

    #draw all sprites to the screen
    all_sprite_list.draw(screen)

    #Refresh the display
    pygame.display.flip()

    #limit the framerate to 240 fps
    clock.tick(240)

#unitialize all pygame modules and close the window
pygame.quit()