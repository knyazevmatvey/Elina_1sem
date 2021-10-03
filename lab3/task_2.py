import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 600))

def tree(x, y, a, b):
    rect(screen, (150, 75, 0), (x + a / 4, y + b, a / 2, 3 * b / 2))
    ellipse(screen, (34, 139, 34), (x, y + b, a, b))
    ellipse(screen, (34, 139, 34), (x, y, a, b))
    circle(screen, (34, 139, 34), (x + a / 2, y + b), 3 * a / 4)
    circle(screen, (255, 127, 127), (x + a, y + b), a / 5)
    circle(screen, (255, 127, 127), (x + a / 4, y + 2 * b / 5), a / 4)

rect(screen, (135, 206, 250), (0, 0, 400, 270))
rect(screen, (0, 255, 0), (0, 270, 400, 330))
#polygon(screen, (255, 255, 0), [(100,100), (200,50),
#                               (300,100), (100,100)])
#polygon(screen, (0, 0, 255), [(100,100), (200,50),
#                               (300,100), (100,100)], 5)
circle(screen, (255, 200, 0), (380, 50), 70)
tree(0, 150, 60, 75)
tree(70, 160, 50, 100)
tree(30, 350, 70, 90)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
