import pygame


pygame.init()

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)
GREY =  (128, 128, 128)
YELLOW =(255, 255,   0)

FPS = 30
screen = pygame.display.set_mode((800, 800))


screen.fill(GREY)

pygame.draw.circle(screen, YELLOW, (400, 400), 200)
pygame.draw.circle(screen, BLACK, (400, 400), 200, 3)

pygame.draw.circle(screen, RED, (325, 350), 45)
pygame.draw.circle(screen, RED, (475, 350), 30)

pygame.draw.circle(screen, BLACK, (325, 350), 45, 1)
pygame.draw.circle(screen, BLACK, (475, 350), 30, 1)

pygame.draw.circle(screen, BLACK, (325, 350), 15)
pygame.draw.circle(screen, BLACK, (475, 350), 15)

pygame.draw.rect(screen, BLACK, (325, 475, 150, 25))

pygame.draw.polygon(screen, BLACK, [(325, 275), (310, 295), (370, 325), (385, 305)])

pygame.draw.polygon(screen, BLACK, [(475, 275), (490, 295), (430, 325), (415, 305)])



pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
