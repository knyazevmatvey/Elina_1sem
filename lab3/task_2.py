import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 600))

rect(screen, (135, 206, 250), (0, 0, 400, 270))
rect(screen, (0, 255, 0), (0, 270, 400, 330))
#polygon(screen, (255, 255, 0), [(100,100), (200,50),
#                               (300,100), (100,100)])
#polygon(screen, (0, 0, 255), [(100,100), (200,50),
#                               (300,100), (100,100)], 5)
circle(screen, (255, 200, 0), (380, 50), 70)
rect(screen, (150, 75, 0), (50, 270, 20, 200))
ellipse(screen, (34, 139, 34), (0, 240, 120, 150))
ellipse(screen, (34, 139, 34), (0, 90, 120, 150))
circle(screen, (34, 139, 34), (60, 240), 90)
circle(screen, (255, 127, 127), (100, 370), 20)
circle(screen, (255, 127, 127), (10, 150), 20)
circle(screen, (255, 127, 127), (50, 200), 15)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
