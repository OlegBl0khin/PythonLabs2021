import pygame


h = 768
x = 1032

pygame.init()

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = ( 17, 240,  80)
RED =   (255,   0,   0)
GREY =  (128, 128, 128)
YELLOW =(255, 255,   0)
BLUE =  ( 17, 225, 240)
PINK =  (247,  22, 199)
WASHY=  (255, 227, 255)

FPS = 30
screen = pygame.display.set_mode((x, h))


screen.fill(GREY)


pygame.draw.rect(screen,  BLUE, (0,   0, x, h/2)) 
pygame.draw.rect(screen, GREEN, (0, h/2, x, h/2))

pygame.draw.polygon(screen,  PINK, [(x * 6/10, h * 3/4), (x * 8/10, h * 3/4), (x * 7/10, h * 1/4)])
pygame.draw.ellipse(screen,  GREY,                            (x * 1/5, h * 1/4, x * 1/6, h * 1/2))

pygame.draw.circle (screen, WASHY,  (x * 7/10, h * 1/4), h * 1/12 )
pygame.draw.circle (screen, WASHY,  (x * 17/60, h * 1/4), h * 1/12)

pygame.draw.line   (screen, BLACK,  (x * 7/32,     h * 15/40  ), (x * 1/7,      h * 11/20  ), 1)
pygame.draw.line   (screen, BLACK,  (x * 120/344,  h * 270/768), (x * 483/1032, h * 423/768), 1)
pygame.draw.line   (screen, BLACK,  (x * 483/1032, h * 423/768), (x * 700/1032, h * 276/768), 1)
pygame.draw.line   (screen, BLACK,  (x * 750/1032, h * 275/768), (x * 850/1032, h * 330/768), 1)
pygame.draw.line   (screen, BLACK,  (x * 850/1032, h * 330/768), (x * 890/1032, h * 284/768), 1)
pygame.draw.line   (screen, BLACK,  (x * 890/1032, h * 284/768), (x * 920/1032, h * 167/768), 1)
pygame.draw.line   (screen, BLACK,  (x * 250/1032, h * 536/768), (x * 183/1032, h * 714/768), 1)
pygame.draw.line   (screen, BLACK,  (x * 183/1032, h * 714/768), (x * 133/1032, h * 714/768), 1)
pygame.draw.line   (screen, BLACK,  (x * 345/1032, h * 528/768), (x * 360/1032, h * 710/768), 1)
pygame.draw.line   (screen, BLACK,  (x * 360/1032, h * 710/768), (x * 410/1032, h * 710/768), 1)
pygame.draw.line   (screen, BLACK,  (x * 680/1032, h * 3/4    ), (x * 680/1032, h * 696/768), 1)
pygame.draw.line   (screen, BLACK,  (x * 680/1032, h * 696/768), (x * 630/1032, h * 696/768), 1)
pygame.draw.line   (screen, BLACK,  (x * 760/1032, h * 3/4    ), (x * 760/1032, h * 696/768), 1)
pygame.draw.line   (screen, BLACK,  (x * 760/1032, h * 696/768), (x * 810/1032, h * 696/768), 1)


pygame.draw.polygon(screen,  YELLOW, [(x * 162/1032, h * 437/768), (x * 155/1032, h * 300/768), 
                                                                   (x * 74/1032, h * 430/1032)])


pygame.draw.circle (screen,  WHITE,  (x * 110/1032,  h * 250/768), h * 25/768)
pygame.draw.circle (screen,    RED,  (x * 130/1032,  h * 285/768), h * 25/768)
pygame.draw.circle (screen,  GREEN,  (x *  95/1032,  h * 290/768), h * 25/768)

pygame.draw.polygon(screen,  RED   , [(x * 920/1032, h * 167/768), (x * 960/1032, h * 100/768), 
                                                                   (x * 910/1032, h * 90/768)])

pygame.draw.circle (screen, RED,  (x * 925/1032, h * 85/768), h * 25/768)
pygame.draw.circle (screen, RED,  (x * 945/1032, h * 95/768), h * 25/768)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
