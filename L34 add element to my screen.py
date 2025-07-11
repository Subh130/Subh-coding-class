import pygame
pygame.init()

screen_width, screen_height = 640, 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My first game screen")

font = pygame.font.SysFont("Arial", 36) 
text_surface = font.render("Hello", True, (0, 0, 0))  

rect_width, rect_height = 60, 60

filled_rect_x = screen_width // 4 - rect_width // 2
filled_rect_y = screen_height // 2 - rect_height // 2

hollow_rect_x = 3 * screen_width // 4 - rect_width // 2
hollow_rect_y = screen_height // 2 - rect_height // 2

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    screen.fill((255, 255, 255))  

    pygame.draw.rect(screen, (0, 125, 255), pygame.Rect(filled_rect_x, filled_rect_y, rect_width, rect_height))

    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(hollow_rect_x, hollow_rect_y, rect_width, rect_height), 3)

    screen.blit(text_surface, (100, 100))

    pygame.display.flip()
c