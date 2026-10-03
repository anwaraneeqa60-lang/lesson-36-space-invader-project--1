import math
import random
import pygame
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
PLAYER_START_X = 370
PLAYER_START_Y = 380
ENEMY_START_Y_MIN = 50
ENEMY_START_Y_MAM = 150
ENEMY_SPEED_X = 4
ENEMY_SPEED_Y = 40
BULLET_SPEED_Y = 10
COLLISION_DISTANCE = 27
pygame.INIT()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
background = pygame.image.load('space invader.jpg')
pygame.display.set_caption("space invader")
icon = pygame.image.load('air ship.jpg')
pygame.display.set_icon(icon)
playerIgm = pygame.image.load('player.png')
playerX = PLAYER_START_X
playerY = PLAYER_START_Y
playerX_change = 0
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6
for _i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0, SCREEN_WIDTH - 64))
    enemyY.append(random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX))
    enemyX_change.append(ENEMY_SPEED_X)
    enemyY_change.append(ENEMY_SPEED_Y)
bulletimg = pygame.image.load('bullet.jpg')
bulletx = 0
bullety = PLAYER_START_Y
bulletx_change = 0
bullety_change = BULLET_SPEED_Y
bullet_state = "ready"
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textx = 10
texty =10
over_font = pygame.fon.Font('freesansbold.ttf', 64)
def show_score(x,y):
    score = font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))
def player(x, y):
    screen.blit(playerImg[i], (x, y))
def enemy(x, y i):
    screen.blit(enemyImg[i], (x, y))
def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(buletImg, (x + 16,y + 10))
def iscollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((enemyX - bulletX) ** 2 + (enemyY - enemyY) ** 2) 
    return distance < COLLISION_DISTANCE
running = True
while running:
    screen.fill((0, 0, 0, ))
    screen.blit(background, (0, 0,))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running in False
        if event.type ==pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT
            playerX_change = 5
            if event.key == pygame.K_SPACE and bullet_state == "ready":
                bulletX = playerX
                fire_bullet(bulletX, bulletY)
            import sys
import pygame
pygame.init()
pygame.mixer.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Python Background Image and Sound")
try:
    bg_image = pygame.image.load("background.jpg").convert()
    bg_image = pygame.transform.smoothscale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
except pygame.error as e:
    print(f"Could not load image: {e}")
    sys.exit()
try:
    pygame.mixer.music.load("music.mp3")
    pygame.mixer.music.play(-1)
except pygame.error as e:
    print(f"Could not load audio: {e}")
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(bg_image, (0, 0))
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
sys.exit()