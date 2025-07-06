import pygame

def main():
    pygame.init()
    screen_width, screen_height = 500, 500
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("color changing spite")

    #mapping of color names to rgb value
    colors= {
        "red": pygame.Color("red"),
        "green": pygame.Color("green"),
        "blue": pygame.Color("blue"),
        "yellow": pygame.Color("yellow"),
        "white": pygame.Color("white"),
    }
    current_color = ["white"]

    x, y = 30, 30
    spite_width, spite_height = 60, 60

    clock = pygame.time.Clock()

    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]: x -= 3
        if pressed[pygame.K_RIGHT]: x += 3
        if pressed[pygame.K_UP]: y -= 3
        if pressed[pygame.K_DOWN]: y += 3

        x = min(max(0,x), screen_width - spite_width)
        y = min(max(0,y), screen_height - spite_height)

        #change color based on bouandry contact
        if x == 0: current_color = ["blue"]
        elif x == screen_width - spite_width: current_color = ["yellow"]
        elif y == 0: current_color = ["red"]
        elif y == screen_height - spite_height: current_color = ["green"]
        else:
            current_color = ["white"]

        screen.fill((0,0,0))
        pygame.draw.rect(screen, current_color,
                         (x,y, spite_width, spite_height))
        pygame.display.flip()
        clock.tick()

    pygame.quit()

if __name__ == "__main__":
    main()