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

def draw_gun():
    mouse_pos = pygame.mouse.get_pos()
    gun_point = (WIDTH/2, HEIGHT - 200)
    lasers = ["blue","red", "green"]
    clicks = pygame.mouse.get_pressed()
    if mouse_pos[0] != gun_point[0]:
        slope = (mouse_pos[1] - gun_point[1]) / (mouse_pos[0] - gun_point[0])
    else:
        slope = -9999
    angle = math.atan(slope)
    rotation = math.degrees(angle)
    if mouse_pos[0] < WIDTH / 2:
        gun = pygame.transform.flip(gun[level - 1], True, False)
        if mouse_pos[1] < 600:
            screen.blit(pygame.transform.rotate(gun, 90 - rotation), (WIDTH / 2 - 90, HEIGHT - 250))
        if clicks[0]:
            pygame.draw.circle(screen, lasers[level - 1], mouse_pos, 5)
        else:
            guns = gun[level - 1]
        if mouse_pos[1] < 600:
          screen.blit(pygame.transform.rotate(guns, 270 + rotation), (WIDTH / 2 - 30, HEIGHT - 250))
          if clicks [0]:
              pygame.draw.circle(screen, lasers[level - 1], mouse_pos, 5)


run = True
while run:
    timer.tick(fps)
    screen.fill("black")
    screen.blit(bgs[level, - 1], (0, 0))
    screen.blit(banners[level, - 1], (0, HEIGHT - 200))
    if level > 0:
        draw_gun()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.flip()
pygame.quit()
