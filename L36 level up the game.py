import pygame
import random
from pygame import mixer

# Initialize mixer and pygame
mixer.init()
pygame.init()

# Colors and background
surf_color = (0, 142, 204)
color = (0, 0, 0)
bg = pygame.image.load("bg.jpeg")
bg = pygame.transform.scale(bg, (500, 400))

# Set up screen
screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Sprite Collision")

# Sprite class
class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(surf_color)
        pygame.draw.rect(self.image, color, pygame.Rect(0, 0, width, height))
        self.rect = self.image.get_rect()

    def moveRight(self, pixels):
        self.rect.x += pixels

    def moveLeft(self, pixels):
        self.rect.x -= pixels

    def moveForward(self, speed):
        self.rect.y += speed * speed / 10

    def moveBack(self, speed):
        self.rect.y -= speed * speed / 10

# Groups and sprites
all_sprites_list = pygame.sprite.Group()

sp1 = Sprite(color, 20, 30)
sp1.rect.x = random.randint(0, 480)
sp1.rect.y = random.randint(0, 370)
all_sprites_list.add(sp1)

sp2 = Sprite((255, 0, 0), 20, 30)
sp2.rect.x = random.randint(0, 480)
sp2.rect.y = random.randint(0, 370)
all_sprites_list.add(sp2)

# Game variables
exit_game = True
clock = pygame.time.Clock()
score = 0
game_over = False

# Font
font = pygame.font.SysFont("arial", 24)
big_font = pygame.font.SysFont("courier", 48)

# Custom event to spawn new enemies every 5 seconds
SPAWN_ENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWN_ENEMY, 5000)

# Start time (in milliseconds)
start_ticks = pygame.time.get_ticks()
time_limit = 30  # in seconds

# Game loop
while exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                exit_game = False
        elif event.type == SPAWN_ENEMY and not game_over:
            new_enemy = Sprite((255, 0, 0), 20, 30)
            new_enemy.rect.x = random.randint(0, 480)
            new_enemy.rect.y = random.randint(0, 370)
            all_sprites_list.add(new_enemy)

    if not game_over:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            sp1.moveLeft(5)
        if keys[pygame.K_RIGHT]:
            sp1.moveRight(5)
        if keys[pygame.K_DOWN]:
            sp1.moveForward(5)
        if keys[pygame.K_UP]:
            sp1.moveBack(5)

        # Collision detection
        for sprite in list(all_sprites_list):
            if sprite != sp1 and sp1.rect.colliderect(sprite.rect):
                all_sprites_list.remove(sprite)
                score += 1
                mixer.music.load("explosion.wav")
                mixer.music.set_volume(0.7)
                mixer.music.play()

        # Check time
        seconds_passed = (pygame.time.get_ticks() - start_ticks) // 1000
        if seconds_passed >= time_limit:
            game_over = True

    # Drawing
    all_sprites_list.update()
    screen.fill(surf_color)
    screen.blit(bg, (0, 0))
    all_sprites_list.draw(screen)

    if not game_over:
        # Show score and timer
        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

        time_left = max(0, time_limit - seconds_passed)
        timer_text = font.render(f"Time Left: {time_left}", True, (255, 255, 255))
        screen.blit(timer_text, (350, 10))
    else:
        # Game over screen
        game_over_text = big_font.render("GAME OVER", True, (255, 0, 0))
        final_score_text = font.render(f"Your Score: {score}", True, (255, 255, 0))
        screen.blit(game_over_text, (250 - game_over_text.get_width() // 2, 140))
        screen.blit(final_score_text, (250 - final_score_text.get_width() // 2, 200))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
