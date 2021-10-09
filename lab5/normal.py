import pygame
from pygame.draw import *
from random import *

pygame.init()

FPS = 30


# color list
WHITE  = (230, 230, 230)
PURPLE = (128,   0, 128)
BLUE   = (121, 121, 242)
BLACK  = (  0,   0,   0)
GREEN  = ( 22,  80,  68)
GRAY   = ( 77,  77,  77)
FISH   = (191, 203, 200)
RED    = (221, 166, 166)
BLOOD  = (211,  18,  23)



width  = 600
height = 800


general_surface = pygame.display.set_mode((width, height))
general_surface.fill(WHITE)

line(general_surface,  BLACK, (0, height / 2), (width, height / 2), 4)
rect(general_surface, PURPLE, (0, 0, width, height / 2))
    
def draw_sign(sign_size):
    transparent = (0, 0, 0, 0)
    sign_surface = pygame.Surface((600, 800))
    sign_surface = sign_surface.convert_alpha()
    sign_surface.fill(transparent)

    circle(sign_surface, BLOOD, (350, 200), 100, 7)
    polygon(sign_surface, BLOOD, [(290, 130), (350, 300), (410, 130),(260, 230),
                                                     (440, 230), (290, 130)], 7)

    sign_surface = pygame.transform.scale(sign_surface, (300 // sign_size, 400 // sign_size) )
    pygame.Surface.blit(general_surface, sign_surface, ( 0 + randint(0, 500),0 + randint(0, 300)))



def draw_bear(bear_size):
    transparent = (0, 0, 0, 0)
    bear_surface = pygame.Surface((600, 800))
    bear_surface = bear_surface.convert_alpha()
    bear_surface.fill(transparent)
    
    ellipse(bear_surface,  GRAY,  (350, 550, 200, 80))
    ellipse(bear_surface, BLACK, (350, 550, 200, 80), 2)
    ellipse(bear_surface, GREEN, (370, 580, 160, 50))
    ellipse(bear_surface, BLACK, (370, 580, 160, 50), 2)

    arc(bear_surface, BLACK, [220, 180, 800, 600], 2, 3, 4)
    line(bear_surface, BLACK, (450, 210), (450, 600), 2)

    ellipse(bear_surface, WHITE, (95, 245, 140, 75))
    ellipse(bear_surface, BLACK, (95, 245, 140, 75), 2)
    ellipse(bear_surface, WHITE, (10, 300, 190, 350))
    ellipse(bear_surface, BLACK, (10, 300, 190, 350), 2)
    ellipse(bear_surface, WHITE, (95, 550, 160, 120))
    ellipse(bear_surface, BLACK, (95, 550, 160, 120), 2)
    ellipse(bear_surface, WHITE, (170, 650, 110, 45))
    ellipse(bear_surface, BLACK, (170, 650, 110, 45), 2)
    ellipse(bear_surface, WHITE, (170, 370, 90, 45))
    ellipse(bear_surface, BLACK, (170, 370, 90, 45), 2)
    circle(bear_surface, WHITE, (117, 255), 12)
    circle(bear_surface, BLACK, (117, 255), 12, 2)
    ellipse(bear_surface, BLACK, (155, 265, 9, 7))
    ellipse(bear_surface, BLACK, (230, 275, 9, 7))
    arc(bear_surface, BLACK, [90, 280, 140, 20], -1.57, 0, 1)


    transparent = (0, 0, 0, 0)
    fish_surface = pygame.Surface((160, 140))
    fish_surface = fish_surface.convert_alpha()
    fish_surface.fill(transparent)

    polygon(fish_surface, RED, [(100,25), (90,5), (120, 10), (122, 12), (120,20), (100, 25)])
    polygon(fish_surface, BLACK, [(100,25), (90,5), (120, 10), (122, 12), (120,20), (100, 25)], 2)
    polygon(fish_surface, RED, [(70,55), (83,55), (85, 68), (65, 70), (69, 60), (70, 55)])
    polygon(fish_surface, BLACK, [(70,55), (83,55), (85, 68), (65, 70), (69, 60), (70, 55)], 2)
    polygon(fish_surface, RED, [(110,55), (120,55), (125, 60), (130, 68), (115, 75), (110, 55)])
    polygon(fish_surface, BLACK, [(110,55), (120,55), (125, 60), (130, 68), (115, 75), (110, 55)], 2)
    ellipse(fish_surface, FISH, (40, 20, 120, 40))
    ellipse(fish_surface, BLACK, (40, 20, 120, 40), 2)
    polygon(fish_surface, FISH, [(5,15), (5,65), (40, 40), (5,15)])
    polygon(fish_surface, BLACK, [(5,15), (5, 65), (40, 40), (5,15)], 2)
    circle(fish_surface, BLUE, (130, 40), 7)
    circle(fish_surface, BLACK, (131, 41), 4)
    fish_surface = pygame.transform.scale(fish_surface, (60, 40))
    fish_surface = pygame.transform.rotate(fish_surface, 30)
    pygame.Surface.blit(bear_surface, fish_surface, (370, 630))
    fish_surface = pygame.transform.rotate(fish_surface, 200)
    pygame.Surface.blit(bear_surface, fish_surface, (300, 600))
    fish_surface = pygame.transform.rotate(fish_surface, 100)
    pygame.Surface.blit(bear_surface, fish_surface, (360, 640))
    fish_surface = pygame.transform.rotate(fish_surface, 120)
    pygame.Surface.blit(bear_surface, fish_surface, (310, 610))
    fish_surface = pygame.transform.rotate(fish_surface, 200)
    pygame.Surface.blit(bear_surface, fish_surface, (380, 430))
    fish_surface = pygame.transform.rotate(fish_surface, 120)
    pygame.Surface.blit(bear_surface, fish_surface, (290, 420))


    bear_surface = pygame.transform.scale(bear_surface, (300 // bear_size, 400 // bear_size))
  
    pygame.Surface.blit(general_surface, bear_surface, (0 + randint(0, 400), 300 + randint(0, 200)))



def draw_pict(height, width, number_bears, bear_size, number_signs, sign_size): 

    '''
    Функция рисует картинку 9.
    height - высота картинки
    width  - ширина картинки 
    number_bears - количество медведей
    bear_size - размер медведей 
    number_signs - количество символов
    sign_size - размер символов
    
    '''
    

    general_surface = pygame.display.set_mode((width, height))
    general_surface.fill(WHITE)

    line(general_surface,  BLACK, (0, height / 2), (width, height / 2), 4)
    rect(general_surface, PURPLE, (0, 0, width, height / 2))

    for i in range(number_bears):
        draw_bear(bear_size)

    for i in range(number_signs):
        draw_sign(sign_size)



draw_pict(800, 600, 3, 1, 3, 1)




pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()

