import pygame


h = 768
w = 1032

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
screen = pygame.display.set_mode((w, h))


screen.fill(GREY)


pygame.draw.rect(screen,  BLUE, (0,   0, w, h/2)) 
pygame.draw.rect(screen, GREEN, (0, h/2, w, h/2))

pygame.draw.polygon(screen,  PINK, [(w * 6/10, h * 3/4), (w * 8/10, h * 3/4), (w * 7/10, h * 1/4)])
pygame.draw.ellipse(screen,  GREY,                            (w * 1/5, h * 1/4, w * 1/6, h * 1/2))

pygame.draw.circle (screen, WASHY,  (w * 7/10, h * 1/4), h * 1/12 )
pygame.draw.circle (screen, WASHY,  (w * 17/60, h * 1/4), h * 1/12)

pygame.draw.line   (screen, BLACK,  (w * 7/32,     h * 15/40  ), (w * 1/7,      h * 11/20  ), 1)
pygame.draw.line   (screen, BLACK,  (w * 120/344,  h * 270/768), (w * 483/1032, h * 423/768), 1)
pygame.draw.line   (screen, BLACK,  (w * 483/1032, h * 423/768), (w * 700/1032, h * 276/768), 1)
pygame.draw.line   (screen, BLACK,  (w * 750/1032, h * 275/768), (w * 850/1032, h * 330/768), 1)
pygame.draw.line   (screen, BLACK,  (w * 850/1032, h * 330/768), (w * 890/1032, h * 284/768), 1)
pygame.draw.line   (screen, BLACK,  (w * 890/1032, h * 284/768), (w * 920/1032, h * 167/768), 1)
pygame.draw.line   (screen, BLACK,  (w * 250/1032, h * 536/768), (w * 183/1032, h * 714/768), 1)
pygame.draw.line   (screen, BLACK,  (w * 183/1032, h * 714/768), (w * 133/1032, h * 714/768), 1)
pygame.draw.line   (screen, BLACK,  (w * 345/1032, h * 528/768), (w * 360/1032, h * 710/768), 1)
pygame.draw.line   (screen, BLACK,  (w * 360/1032, h * 710/768), (w * 410/1032, h * 710/768), 1)
pygame.draw.line   (screen, BLACK,  (w * 680/1032, h * 3/4    ), (w * 680/1032, h * 696/768), 1)
pygame.draw.line   (screen, BLACK,  (w * 680/1032, h * 696/768), (w * 630/1032, h * 696/768), 1)
pygame.draw.line   (screen, BLACK,  (w * 760/1032, h * 3/4    ), (w * 760/1032, h * 696/768), 1)
pygame.draw.line   (screen, BLACK,  (w * 760/1032, h * 696/768), (w * 810/1032, h * 696/768), 1)


pygame.draw.polygon(screen,  YELLOW, [(w * 162/1032, h * 437/768), (w * 155/1032, h * 300/768), 
                                                                   (w * 74/1032, h * 430/1032)])


pygame.draw.circle (screen,  WHITE,  (w * 110/1032,  h * 250/768), h * 25/768)
pygame.draw.circle (screen,    RED,  (w * 130/1032,  h * 285/768), h * 25/768)
pygame.draw.circle (screen,  GREEN,  (w *  95/1032,  h * 290/768), h * 25/768)

pygame.draw.polygon(screen,  RED   , [(w * 920/1032, h * 167/768), (w * 960/1032, h * 100/768), 
                                                                   (w * 910/1032, h * 90/768)])

pygame.draw.circle (screen, RED,  (w * 925/1032, h * 85/768), h * 25/768)
pygame.draw.circle (screen, RED,  (w * 945/1032, h * 95/768), h * 25/768)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
