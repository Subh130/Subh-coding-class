import pygame

pygame.init()
#create the display surface of the specific dimention
window = pygame.display.set_mode((400,400))

#fill the screen with white colors
window.fill((255,255,255))

#define colors
RED = (255,0,0)

#draw solid circle
pygame.draw.circle(window, RED, (300,300),50)

#draw outlined circle
pygame.draw.circle(window, RED, (100,100), 50,3)

#draw the surface object to the screen
pygame.display.update()

#game loop
running = True
while running:
    #event handle
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            running = False
            
#quit pygame
pygame.quit()