import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 600))


# colors
white = (255, 255, 255)
black = (0, 0, 0)
eye_color = (0, 50, 255)
corn_color = (106, 90, 205)

# colors for upper hair
blue1 = (0, 191, 255)
blue2 = (30, 144, 235)
blue3 = (0, 0, 128)
blue4 = (138, 43, 226)

# colors for lower hair
violet1 = (123, 104, 238)
violet2 = (0, 0, 139)
violet3 = (138, 43, 226)
violet4 = (25, 25, 112)
violet5 = (75, 0, 130)

brown = (150, 75, 0)
green = (34, 139, 34)
apple = (255, 127, 127)
yellow = (255, 200, 0)
bright_green = (0, 255, 0)
sky_blue = (135, 206, 250)


# больше функций богу функций
# (ну в лабе беск много функций поэтому здесь тоже)

def tree(x, y, a, b):
    '''
    Функция рисует дерево
    x, y - координаты дерева (сама точка единорога неочевидна)
    a, b - размеры дерева (точнее пропорциональные им числа)
    surface - поверхность, на которой рисуем
    '''
    
    # trunk
    rect(screen, brown, (x + a/4, y + b, a/2, 3*b/2))

    # leaves
    ellipse(screen, green, (x, y + b, a, b))
    ellipse(screen, green, (x, y, a, b))
    circle(screen, green, (x + a/2, y + b), 3*a/4)

    # apples
    circle(screen, apple, (x + a, y + b), (a+b) / 10)
    circle(screen, apple, (x + a/4, y + 2*b/5), (a+b) / 8)



def horse_body(x, y, a, b, surface = screen):
    ellipse(surface, white, (x, y, a, b))

def horse_legs(x, y, a, b, surface = screen):
    rect(surface, white, (x + a / 9, y + b / 2, abs(a) / 9, 3 * b / 2))
    rect(surface, white, (x + 3 * a / 9, y + b / 4, abs(a) / 9, 3 * b / 2))
    rect(surface, white, (x + 5 * a / 9, y + b / 2, abs(a) / 9, 3 * b / 2))
    rect(surface, white, (x + 7 * a / 9, y + b / 4, abs(a) / 9, 3 * b / 2))

def horse_head(x, y, a, b, surface = screen):
    
    # head
    ellipse(surface, white, (x + 7 * a / 9, y - b, 2 * a / 9, 3 * b / 2))
    ellipse(surface, white, (x + 7 * a / 9, y - 5 * b / 6, 4 * a / 9, b / 3))
    ellipse(surface, white, (x + 2*a/3, y - b, 4*a/9, 4*b/9))

    # eye
    circle(surface, eye_color, (x + a, y - 5 * b / 6), max(a, b) / 15)
    circle(surface, black, (x + a, y - 5 * b / 6), max(a, b) / 30)

    # corn
    polygon(surface, corn_color, [(x + 8 * a / 9, y - 5 * b / 3),
                                  (x + a, y - b), (x + 7 * a / 9,y - b)])

def upper_hair(x, y, a, b, surface = screen):
    ellipse(surface, blue1, (x + 5.5*a/9, y - 5*b/4, 4*a/9, b/3))
    ellipse(surface, blue2, (x + 4.5*a/9, y - 4*b/4, 4*a/9, b/3))
    ellipse(surface, blue3, (x + 4*a/9, y - 3*b/4, 5*a/9, b/2))
    ellipse(surface, blue4, (x + 3*a/9, y - 0.35*b, 5*a/9, b/2))

def lower_hair(x, y, a, b, surface = screen):
    ellipse(surface, violet1, (x - 2*a/9, y + b/2 - b/6, a*4/9, b*4/9))
    ellipse(surface, violet2, (x - a/3, y + 0.5 * b, 5 * a / 9, b / 2))
    ellipse(surface, violet3, (x - 3.5 * a / 9, y + 0.8 * b, 5 * a / 9, b / 2))
    ellipse(surface, violet4, (x - 4 * a / 9, y + 1.1 * b, 5 * a / 9, b / 2))
    ellipse(surface, violet5, (x - 4 * a / 9, y + 1.4 * b, 5 * a / 9, b / 2))
    

def horse(x, y, a, b, surface = screen):
    '''
    Функция рисует единорога
    x, y - координаты единорога (сама точка единорога неочевидна)
    a, b - размеры единорога (точнее пропорциональные им числа)
    surface - поверхность, на которой рисуем
    '''
    
    horse_body(x, y, a, b)
    horse_legs(x, y, a, b)
    horse_head(x, y, a, b)
    upper_hair(x, y, a, b)
    lower_hair(x, y, a, b)

def sun(x, y, r, surface = screen):
    '''
    Функция рисует солнце
    x, y - центр солнца
    r - радиус солнца
    '''
    circle(surface, yellow, (x, y), r)

def sky(border, a, b, surface = screen):
    '''
    Функция рисует небо и траву
    border - граница между небом и землей
    a, b - размеры экрана
    '''
    rect(surface, sky_blue, (0, 0, a, border))
    rect(surface, bright_green, (0, border, a, b - border))
    
    




# main


sky(270, 400, 600)
sun(380, 50, 70)

# tree parameters
Trees = [(0, 150, 60, 75), (70, 160, 50, 100), (30, 350, 70, 90)]
for tr in Trees:
    tree(*tr)

# horse parameters
Horses = [(230, 300, 100, 70), (300, 500, 70, 50), (200, 450, -70, 60)]
for h in Horses:
    horse(*h)





pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
