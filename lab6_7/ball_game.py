import pygame
from pygame.draw import *
from random import randint
pygame.font.init()
pygame.init()
font1 = pygame.font.Font(None, 30)

FPS = 30
height = 400
width = 500
screen = pygame.display.set_mode((width, height))

RED     = (255,   0,   0)
BLUE    = (  0,   0, 255)
YELLOW  = (255, 255,   0)
GREEN   = (0  , 255,   0)
MAGENTA = (255,   0, 255)
CYAN    = (0  , 255, 255)
BLACK   = (0  ,   0,   0)
WHITE   = (255, 255, 255)

COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

class Ball:

    def __init__(self, color, radius, coordinates, velocity):

        '''
        создаем переменную класса Ball
        color - цвет шарика
        radius - радиус шарика
        coordinates - координаты шарика
        velocity - скорость шарика
        
        '''
        self.color = color 
        self.radius = radius
        self.coordinates = coordinates
        self.velocity = velocity
       

    def move(self):

        '''
        функция движения шарика
        извеняет координаты шарика в зависимости от его скорости
        '''
        
        v0_x, v0_y = self.velocity
        self.coordinates[0] += v0_x
        self.coordinates[1] += v0_y

    def collisions(self, BORDER_COORD):

        '''
        функция реализует отображения
        если шарик попадает в стену меняет направление его скорости
        '''

        if (self.coordinates[0] - self.radius <= 0 or 
        self.coordinates[0] + self.radius >= BORDER_COORD[0]):

            self.velocity[0] *= -1

        if (self.coordinates[1] - self.radius <= 0 or 
        self.coordinates[1] + self.radius >= BORDER_COORD[1]):

            self.velocity[1] *= -1

    def draw(self): 

        '''
        функция обновляет положения шариков на картинке
        '''
        
        pygame.draw.circle(screen, self.color, self.coordinates, self.radius)

    def pop(self, click_position):

        '''
        функция возвращает 1 если кликом попали некоторому по шарику 
        необходима для реализации удаления шариков
        '''

        if ((click_position[0] - self.coordinates[0]  ) ** 2 + 
           ( click_position[1] - self.coordinates[1]  ) ** 2 < (self.radius) ** 2 ):
            return 1
                                                                                                    
        else:
            return 0


class Cube:
    def __init__(self, color, radius, coordinates, velocity):

        '''
        создаем квадратик по аналогии с шариком
        '''

        self.color = color
        self.radius = radius
        self.coordinates = coordinates
        self.velocity = velocity
       

    def move(self):

        '''
        Движение квадратика
        '''

        v0_x, v0_y = self.velocity
        self.coordinates[0] += v0_x
        self.coordinates[1] += v0_y

    def collisions(self, BORDER_COORD):

        '''
        соударение квадратика со стенкой
        '''

        if (self.coordinates[0] - self.radius <= 0 or
            self.coordinates[0] + self.radius >= BORDER_COORD[0]):

            self.velocity[0] *= -1

        if (self.coordinates[1] - self.radius <= 0 or
            self.coordinates[1] + self.radius >= BORDER_COORD[1]):
            
            self.velocity[1] *= -1

    def pop(self, click_position):

        '''
        Удаление квадратика
        '''

        if (self.coordinates[0] + self.radius >= click_position[0] and 
            self.coordinates[0] - self.radius <= click_position[0] and 
            self.coordinates[1] + self.radius >= click_position[1] and 
            self.coordinates[1] - self.radius <= click_position[1]):

            return 1
        else:
            return 0

    def draw(self):

        '''
        Рисование квадратиков
        '''

        pygame.draw.rect(screen, self.color, (self.coordinates[0] - self.radius, 
        self.coordinates[1] - self.radius, 2 * self.radius, 2 * self.radius) )



def internal_collisions(pool2):
    '''
    Функция реализует соударения между квадратиками
    '''

    for i, el in enumerate(pool2): 

        for j in range(i + 1, len(pool2)):

           

            if ( abs(pool2[i].coordinates[0] - pool2[j].coordinates[0]) <= 
                pool2[i].radius + pool2[j].radius and 
                abs(pool2[i].coordinates[1] - pool2[j].coordinates[1]) <= 
                pool2[i].radius + pool2[j].radius and 
                abs(pool2[i].coordinates[1] - pool2[i].velocity[1] -
                pool2[j].coordinates[1] + pool2[j].velocity[1]) <= 
                pool2[i].radius + pool2[j].radius ):

                pool2[i].velocity[0] *= -1
                pool2[j].velocity[0] *= -1

            if ( abs(pool2[i].coordinates[1] - pool2[j].coordinates[1]) <= 
                pool2[i].radius + pool2[j].radius and
                abs(pool2[i].coordinates[0] - pool2[j].coordinates[0]) <= 
                pool2[i].radius + pool2[j].radius and 
                abs(pool2[i].coordinates[0] - pool2[i].velocity[0] - 
                pool2[j].coordinates[0] + pool2[j].velocity[0]) <= 
                pool2[i].radius + pool2[j].radius  ):

                pool2[i].velocity[1] *= -1
                pool2[j].velocity[1] *= -1
 

number_balls = 10
pool1 = []
for i in range(number_balls):
    '''
    создали бассейн с шариками для одновременного движения
    '''

    color       = COLORS[randint(0, 5)]
    radius      = randint(10, 20)
    coordinates = [randint(20, width - 20), randint(20, height - 20)]
    velocity    = [randint(1, 5),     randint(1, 5)     ]


    x = Ball(color, radius, coordinates, velocity)

    pygame.draw.circle(screen, color, coordinates, radius)
    pool1.append(x)


pool2 = [] # бассейн для квадратиков


pygame.display.update()
clock = pygame.time.Clock()
finished = False


score = 0
print(len(pool1))


while not finished:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:

            if (event.button == 3):
                '''
                Если нажимаем на правую кнопку мыши то спавнится квадратик
                Если в момент клика есть другой квадратик на этой же территории
                квадратик не появится

                '''
                color       = COLORS[randint(0, 5)]
                radius      = randint(30, 50)
                coordinates = [event.pos[0], event.pos[1]]
                velocity    = [randint(1, 5),     randint(1, 5)     ]

                x = Cube(color, radius, coordinates, velocity)

                pygame.draw.rect(screen, color, (coordinates[0] - radius, 
                         coordinates[1] - radius, 2 * radius, 2 * radius))

                f = 0

                for i, el in enumerate(pool2):
                    if (abs(pool2[i].coordinates[1] - coordinates[1]) <= 
                    pool2[i].radius + radius and
                    abs(pool2[i].coordinates[0] - coordinates[0]) <= 
                    pool2[i].radius + radius):

                        f = 1

                if (f == 0):
                    pool2.append(x)

                if (f == 1):
                    score -= 1

                   
            for i, el in enumerate(pool1):
                '''
                Если мы кликом левой кнопки мыши попадем по шарику
                он исчезнет и мы получаем +1 к очкам
                ''' 
                if (event.button == 1): 
                    if (el.pop(event.pos) == 1):       # если шарик удален 
                        pool1.pop(i)       
                        score += 1
                        print(score)

            for i, el in enumerate(pool2):
                '''
                Если кликом левой кнопки мыши попадаем по шарику
                '''
                if (event.button == 1):
                    if (pool2[i].pop(event.pos) == 1):
                        pool2.pop(i)
                        score += 2
                        print(score)
                        
    
    internal_collisions(pool2)
    
    for i, el in enumerate(pool2):
        
        pool2[i].collisions([width, height])
        pool2[i].move()
        pool2[i].draw()

    for i, el in enumerate(pool1):

        pool1[i].collisions([width, height])
        pool1[i].move()
        pool1[i].draw()

    score_text = font1.render('Your score: ' + str(score), True, WHITE)
    screen.blit(score_text, (10, 10))
    pygame.display.update()


    pygame.display.update()
    clock.tick(FPS)
    screen.fill(BLACK)

pygame.quit()




