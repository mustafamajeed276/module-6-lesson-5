import pygame
import math
import random
screen_width = 800
screen_height = 500
player_start_x = 370
player_start_y = 380
enemy_start_y_min = 50
enemy_start_y_max = 150
enemy_speed_x = 4
enemy_speed_y = 40
bullet_speed_y = 10
collision_distance = 27
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
background = pygame.image.load("background (1).png")
pygame.display.set_caption('space invader')
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)
player = pygame.image.load('player.png')
playerx = player_start_x
playery = player_start_y
playerx_change = 0
enemyimg = []
enemy_x = []
enemy_y = []
enemy_change_x = []
enemy_change_y = []
num_enemies = 6
for _i in range(num_enemies):
    enemyimg.append(pygame.image.load('enemy (1).png'))
    enemy_x.append(random.randint(0, screen_width - 64))
    enemy_y.append(random.randint(enemy_start_y_min, enemy_start_y_max))
    enemy_change_x.append(enemy_speed_x)
    enemy_change_y.append(enemy_speed_y)
bulletimg = pygame.image.load('bullet (1).png')
bullet_x = 0
bullet_y = player_start_y
bulletx_change = 0
bullety_change = bullet_speed_y
bullet_state = "ready"