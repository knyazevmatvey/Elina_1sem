import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

rect(screen, (255, 255, 255), (0, 0, 400, 400))
#rect(screen, (0, 0, 255), (100, 100, 200, 200), 5)
#polygon(screen, (255, 255, 0), [(100,100), (200,50),
#                               (300,100), (100,100)])
#polygon(screen, (0, 0, 255), [(100,100), (200,50),
#                               (300,100), (100,100)], 5)
circle(screen, (245, 245, 220), (200, 200), 100)
circle(screen, (0, 0, 0), (200, 200), 100, 3)

circle(screen, (0, 200, 100), (150, 170), 20)
circle(screen, (0, 200, 100), (250, 170), 20)
circle(screen, (0, 0, 0), (150, 170), 7)
circle(screen, (0, 0, 0), (250, 170), 7)

rect(screen, (0, 0, 0), (150, 240, 100, 10))

line(screen, (0, 0, 0), (140, 140), (160, 120), 10)
line(screen, (0, 0, 0), (260, 140), (240, 120), 10)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
