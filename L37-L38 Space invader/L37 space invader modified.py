import math
import random
import pygame
from pygame import mixer

# Initialize pygame and mixer
pygame.init()
mixer.init()

# Screen
screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Space Invader")
icon = pygame.image.load("L37-L38 Space invader/ufo.png")
pygame.display.set_icon(icon)

# Background
background = pygame.image.load("L37-L38 Space invader/background.png")

# Background music
mixer.music.load("L37-L38 Space invader/background.wav")
mixer.music.play(-1)

# Player
playerImg = pygame.image.load("L37-L38 Space invader/player.png")
playerX = 370
playerY = 380
playerX_change = 0

# Enemies
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load("L37-L38 Space invader/enemy.png"))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(4)
    enemyY_change.append(40)

# Strong enemy
strong_enemyImg = pygame.image.load("L37-L38 Space invader/enemy.png")  # Use different sprite if available
strong_enemy = {
    'x': random.randint(0, 736),
    'y': random.randint(50, 150),
    'x_change': 2,
    'y_change': 40,
    'health': 2
}

# Bullets (multiple)
bulletImg = pygame.image.load("L37-L38 Space invader/bullet.png")
bullets = []
bulletY_change = 10

# Score
score_value = 0
font = pygame.font.Font("freesansbold.ttf", 32)
textX = 10
textY = 10

# Timer
start_ticks = pygame.time.get_ticks()
time_limit = 30
timer_font = pygame.font.Font("freesansbold.ttf", 24)
game_over = False

# Game Over
over_font = pygame.font.Font("freesansbold.ttf", 64)

# Functions
def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def show_timer(x, y, seconds_left):
    timer = timer_font.render(f"Time Left: {seconds_left}s", True, (255, 255, 255))
    screen.blit(timer, (x, y))

def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 0, 0))
    screen.blit(over_text, (200, 200))
    final_score = font.render(f"Final Score: {score_value}", True, (255, 255, 255))
    screen.blit(final_score, (270, 280))

def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))

def fire_bullet(x, y):
    screen.blit(bulletImg, (x + 16, y + 10))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + math.pow(enemyY - bulletY, 2))
    return distance < 27

# Game loop
running = True
while running:

    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    seconds_passed = (pygame.time.get_ticks() - start_ticks) // 1000
    time_left = max(0, time_limit - seconds_passed)
    if time_left <= 0:
        game_over = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if not game_over:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    playerX_change = -5
                if event.key == pygame.K_RIGHT:
                    playerX_change = 5
                if event.key == pygame.K_SPACE:
                    if len(bullets) < 3:
                        bulletsound = mixer.Sound("L37-L38 Space invader/laser.wav")
                        bulletsound.play()
                        bullets.append({'x': playerX, 'y': playerY, 'state': 'fire'})

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playerX_change = 0

    if not game_over:
        # Player movement
        playerX += playerX_change
        playerX = max(0, min(playerX, 736))

        # Enemies
        for i in range(num_of_enemies):
            if enemyY[i] > 340:
                game_over = True
                break

            enemyX[i] += enemyX_change[i]
            if enemyX[i] <= 0:
                enemyX_change[i] = 4
                enemyY[i] += enemyY_change[i]
            elif enemyX[i] >= 736:
                enemyX_change[i] = -4
                enemyY[i] += enemyY_change[i]

            # Collision with bullets
            for bullet in bullets[:]:
                if isCollision(enemyX[i], enemyY[i], bullet['x'], bullet['y']):
                    explosionsound = mixer.Sound("L37-L38 Space invader/explosion.wav")
                    explosionsound.play()
                    try:
                        bullets.remove(bullet)
                    except:
                        pass
                    score_value += 1
                    enemyX[i] = random.randint(0, 736)
                    enemyY[i] = random.randint(50, 150)

            enemy(enemyX[i], enemyY[i], i)

        # Strong enemy movement
        if strong_enemy['y'] > 340:
            game_over = True

        strong_enemy['x'] += strong_enemy['x_change']
        if strong_enemy['x'] <= 0:
            strong_enemy['x_change'] = 2
            strong_enemy['y'] += strong_enemy['y_change']
        elif strong_enemy['x'] >= 736:
            strong_enemy['x_change'] = -2
            strong_enemy['y'] += strong_enemy['y_change']

        # Collision with strong enemy
        for bullet in bullets[:]:
            if isCollision(strong_enemy['x'], strong_enemy['y'], bullet['x'], bullet['y']):
                explosionsound = mixer.Sound("L37-L38 Space invader/explosion.wav")
                explosionsound.play()
                bullets.remove(bullet)
                strong_enemy['health'] -= 1
                if strong_enemy['health'] <= 0:
                    score_value += 5
                    strong_enemy['x'] = random.randint(0, 736)
                    strong_enemy['y'] = random.randint(50, 150)
                    strong_enemy['health'] = 2

        screen.blit(strong_enemyImg, (strong_enemy['x'], strong_enemy['y']))

        # Bullets movement
        for bullet in bullets[:]:
            if bullet['y'] <= 0:
                bullets.remove(bullet)
            else:
                fire_bullet(bullet['x'], bullet['y'])
                bullet['y'] -= bulletY_change

    else:
        game_over_text()

    # Drawing
    player(playerX, playerY)
    show_score(textX, textY)
    if not game_over:
        show_timer(640, 10, time_left)

    pygame.display.update()
