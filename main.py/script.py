import pygame
import math
pygame.init()
fps = 60
timer = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 32)
WIDTH = 900
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Circle Animation")
bgs = []
banners = []
gun = []
level = 0
for i in range(1, 4):
    bgs.append(pygame.image.load(f"assets/bg/{i}.png"))
    banners.append(pygame.image.load(f"assets/banner/{i}.png"))
    gun.append(pygame.image.load(f"assets/gun/{i}.png"))
run = True
while run:
    timer.tick(fps)
    screen.fill("black")
    screen.blit(bgs[level, - 1], (0, 0))
    screen.blit(banners[level, - 1], (0, HEIGHT - 200))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.flip()
pygame.quit()
