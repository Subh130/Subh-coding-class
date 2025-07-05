import pygame 
pygame.init()
white = (255,255,255)

#clock
clock = pygame.time.Clock()

#creating the display surface object
#of specific dimention..e(X, Y)
pygame.display.set_caption("Image")
image = pygame.image.load("download.JFIF")

#set the size of the image
DEFAULT_IMAGE_SIZE = (200,200)

#select the image to the needed size
image = pygame.transform.scale(image, DEFAULT_IMAGE_SIZE)

#set a default positon
DEFAULT_IMAGE_POSITION = (150, 150) 

#infinite loop
while True:
    display_surface.fill(white)
    display_surace.bilt(image, DEFAULT_IMAGE_POSITION)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                pygame.quit()
                #quit the program 
                quit()

            #part of event loop
        pygame.display.flip()
        clock.tick(30)