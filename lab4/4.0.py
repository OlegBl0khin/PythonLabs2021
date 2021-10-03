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

pygame.draw.polygon(screen,  PINK, [(x/2 * 6/10, h/4 + h/2 * 3/4), (x/2 * 8/10, h/4 + h/2 * 3/4), (x/2 * 7/10, h/4 + h/2 * 1/4)])
pygame.draw.ellipse(screen,  GREY,                            (x/2 * 1/5, h/4 + h/2 * 1/4, x/2 * 1/6, h/2 * 1/2))

pygame.draw.circle (screen, WASHY,  (x/2 * 7/10, h/4 + h/2 * 1/4), h/2 * 1/12 )
pygame.draw.circle (screen, WASHY,  (x/2 * 17/60, h/4 + h/2 * 1/4), h/2 * 1/12)

pygame.draw.line   (screen, BLACK,  (x/2 * 7/32,     h/4 + h/2 * 15/40  ), (x/2 * 1/7,      h/4 + h/2 * 11/20  ), 1)
pygame.draw.line   (screen, BLACK,  (x/2 * 120/344,  h/4 + h/2 * 270/768), (x/2 * 483/1032, h/4 + h/2 * 423/768), 1)
pygame.draw.line   (screen, BLACK,  (x/2 * 483/1032, h/4 + h/2 * 423/768), (x/2 * 700/1032, h/4 + h/2 * 276/768), 1)
pygame.draw.line   (screen, BLACK,  (x/2 * 750/1032, h/4 + h/2 * 275/768), (x/2 * 930/1032, h/4 + h/2 * 330/768), 1)
pygame.draw.line   (screen, BLACK,  (x/2 * 930/1032, h/4 + h/2 * 330/768), (x/2 * 1032/1032,h/4 + h/2 * 250/768), 1)
pygame.draw.line   (screen, BLACK,  (x/2 * 250/1032, h/4 + h/2 * 536/768), (x/2 * 183/1032, h/4 + h/2 * 714/768), 1)
pygame.draw.line   (screen, BLACK,  (x/2 * 183/1032, h/4 + h/2 * 714/768), (x/2 * 133/1032, h/4 + h/2 * 714/768), 1)
pygame.draw.line   (screen, BLACK,  (x/2 * 345/1032, h/4 + h/2 * 528/768), (x/2 * 360/1032, h/4 + h/2 * 710/768), 1)
pygame.draw.line   (screen, BLACK,  (x/2 * 360/1032, h/4 + h/2 * 710/768), (x/2 * 410/1032, h/4 + h/2 * 710/768), 1)
pygame.draw.line   (screen, BLACK,  (x/2 * 680/1032, h/4 + h/2 * 3/4    ), (x/2 * 680/1032, h/4 + h/2 * 696/768), 1)
pygame.draw.line   (screen, BLACK,  (x/2 * 680/1032, h/4 + h/2 * 696/768), (x/2 * 630/1032, h/4 + h/2 * 696/768), 1)
pygame.draw.line   (screen, BLACK,  (x/2 * 760/1032, h/4 + h/2 * 3/4    ), (x/2 * 760/1032, h/4 + h/2 * 696/768), 1)
pygame.draw.line   (screen, BLACK,  (x/2 * 760/1032, h/4 + h/2 * 696/768), (x/2 * 810/1032, h/4 + h/2 * 696/768), 1)


pygame.draw.polygon(screen,  YELLOW, [(x/2 * 162/1032, h/4 + h/2 * 437/768), (x/2 * 155/1032, h/4 + h/2 * 300/768), 
                                                                   (x/2 * 74/1032, h/4 + h/2 * 430/1032)])


pygame.draw.circle (screen,  WHITE,  (x/2 * 110/1032,  h/4 + h/2 * 250/768),  h/2 * 25/768)
pygame.draw.circle (screen,    RED,  (x/2 * 130/1032,  h/4 + h/2 * 285/768),  h/2 * 25/768)
pygame.draw.circle (screen,  GREEN,  (x/2 *  95/1032,  h/4 + h/2 * 290/768),  h/2 * 25/768)

pygame.draw.polygon(screen,  RED   , [(x/2 * 1020/1032, h/4 + h/2 * 167/768), (x/2 * 1060/1032, h/4 + h/2 * 100/768), 
                                                                   (x/2 * 1010/1032, h/4 + h/2 * 90/768)])

pygame.draw.circle (screen, RED,  (x/2 , h/4 + h/2 * 85/768),  h/2 * 25/768)
pygame.draw.circle (screen, RED,  (x/2 , h/4 + h/2 * 95/768),  h/2 * 25/768)


pygame.draw.polygon(screen,  PINK, [(x - x/2 * 6/10, h/4 + h/2 * 3/4), (x - x/2 * 8/10, h/4 + h/2 * 3/4), (x - x/2 * 7/10, h/4 + h/2 * 1/4)])
pygame.draw.ellipse(screen,  GREY,                            (x - x/2 * 1/5 - x/2 * 1/6, h/4 + h/2 * 1/4, x/2 * 1/6, h/2 * 1/2))

pygame.draw.circle (screen, WASHY,  (x - x/2 * 7/10,  h/4 + h/2 * 1/4), h/2 * 1/12)
pygame.draw.circle (screen, WASHY,  (x - x/2 * 17/60, h/4 + h/2 * 1/4), h/2 * 1/12)

pygame.draw.line   (screen, BLACK,  (x - x/2 * 7/32,     h/4 + h/2 * 15/40  ), (x - x/2 * 1/7,      h/4 + h/2 * 11/20  ), 1)
pygame.draw.line   (screen, BLACK,  (x - x/2 * 120/344,  h/4 + h/2 * 270/768), (x - x/2 * 483/1032, h/4 + h/2 * 423/768), 1)
pygame.draw.line   (screen, BLACK,  (x - x/2 * 483/1032, h/4 + h/2 * 423/768), (x - x/2 * 700/1032, h/4 + h/2 * 276/768), 1)
pygame.draw.line   (screen, BLACK,  (x - x/2 * 750/1032, h/4 + h/2 * 275/768), (x - x/2 * 930/1032, h/4 + h/2 * 330/768), 1)
pygame.draw.line   (screen, BLACK,  (x - x/2 * 930/1032, h/4 + h/2 * 330/768), (x - x/2 * 1032/1032, h/4 + h/2 * 250/768), 1)
pygame.draw.line   (screen, BLACK,  (x - x/2 * 250/1032, h/4 + h/2 * 536/768), (x - x/2 * 183/1032, h/4 + h/2 * 714/768), 1)
pygame.draw.line   (screen, BLACK,  (x - x/2 * 183/1032, h/4 + h/2 * 714/768), (x - x/2 * 133/1032, h/4 + h/2 * 714/768), 1)
pygame.draw.line   (screen, BLACK,  (x - x/2 * 345/1032, h/4 + h/2 * 528/768), (x - x/2 * 360/1032, h/4 + h/2 * 710/768), 1)
pygame.draw.line   (screen, BLACK,  (x - x/2 * 360/1032, h/4 + h/2 * 710/768), (x - x/2 * 410/1032, h/4 + h/2 * 710/768), 1)
pygame.draw.line   (screen, BLACK,  (x - x/2 * 680/1032, h/4 + h/2 * 3/4    ), (x - x/2 * 680/1032, h/4 + h/2 * 696/768), 1)
pygame.draw.line   (screen, BLACK,  (x - x/2 * 680/1032, h/4 + h/2 * 696/768), (x - x/2 * 630/1032, h/4 + h/2 * 696/768), 1)
pygame.draw.line   (screen, BLACK,  (x - x/2 * 760/1032, h/4 + h/2 * 3/4    ), (x - x/2 * 760/1032, h/4 + h/2 * 696/768), 1)
pygame.draw.line   (screen, BLACK,  (x - x/2 * 760/1032, h/4 + h/2 * 696/768), (x - x/2 * 810/1032, h/4 + h/2 * 696/768), 1)
pygame.draw.line   (screen, BLACK,  (x/2, h/4 + h/2 * 250/768), (x/2 , h/4 + h/2 * 150/768), 1)

pygame.draw.polygon(screen,  YELLOW, [(x - x/2 * 162/1032, h/4 + h/2 * 437/768), (x - x/2 * 155/1032, h/4 + h/2 * 300/768), 
                                                                   (x - x/2 * 74/1032, h/4 + h/2 * 430/1032)])


pygame.draw.circle (screen,  WHITE,  (x - x/2 * 110/1032,  h/4 + h/2 * 250/768),  h/2 * 25/768)
pygame.draw.circle (screen,    RED,  (x - x/2 * 130/1032,  h/4 + h/2 * 285/768),  h/2 * 25/768)
pygame.draw.circle (screen,  GREEN,  (x - x/2 *  95/1032,  h/4 + h/2 * 290/768),  h/2 * 25/768)

pygame.draw.polygon(screen,  RED   , [(x - x/2 * 1020/1032, h/4 + h/2 * 167/768), (x - x/2 * 1060/1032, h/4 + h/2 * 100/768), 
                                                                   (x - x/2 * 1010/1032, h/4 + h/2 * 90/768)])

pygame.draw.circle (screen, RED,  (x/2 , h/4 + h/2 * 85/768),  h/2 * 25/768)
pygame.draw.circle (screen, RED,  (x/2 , h/4 + h/2 * 95/768),  h/2 * 25/768)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()



