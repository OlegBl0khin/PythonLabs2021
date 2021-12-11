import pygame
import math 
from random import choice
from random import randint

pygame.init()
WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

FPS = 30
g = 1

RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN, BLACK, WHITE, GREY]

Balls = [] # массив снарядов присутствующих на карте
Points = 0
Targets = [] # массив целей 

Finished = False
'''
def new_target_1():
	target = level1_Target()

def new_target_2():
	target = level2_Target()
'''

def rotated_rect(x, y, a, b, an, screen, color):
	'''
	рисует повернутый на некоторый угол an прямоугольник со сторонами a b
	относительно координат x y 
	также функция принимает значения эрана и цвета
	'''
	cos = math.cos(an)
	sin = math.sin(an)
	pygame.draw.polygon(screen, color, [(x, y), (x + a*cos, y - a*sin), 
		(x + a*cos - b*sin, y - a*sin - b*cos), 
		(x - b*sin, y - b*cos)])

def new_ball(vx, vy, x, y, color, time):
	# пополняет массив с шариками, когда происходит выстрел
	ball = Ball(vx, vy, x, y, color, time)
	Balls.append(ball)

class Gun:

	def __init__(self):
		'''
		класс пушки 
		x, y - координаты нижней вершины пушки 
		an - угол наклона ствола пушки к горизонту
		f2_power - величина заряда пушки
		on - если значение 1 значит пушка в процессе зарядки
		   - если значение 0 значит пушка бездействует

		w, a, s, d - обеспечит движение танка при нажатии на эти клавиши
		'''
		self.x = 20
		self.y = 450
		self.an = 1
		self.f2_power = 10
		self.on = 0
		
		self.w = 0
		self.s = 0
		self.a = 0
		self.d = 0

		self.color = BLACK

	def targetting(self, event):
		#прицеливание, пушка направлена в сторону курсора мышки
		if event:
			try:
				self.an = math.atan((self.y - event.pos[1]) / (event.pos[0] - self.x))
			except:
				ZeroDivisionError
		
	def draw(self):
		# метод, который обеспечивает постоянную зарисовку текущего положения пушки
		pygame.draw.rect(screen, GREEN, (self.x - 20, self.y, 40, 20) )
		rotated_rect(self.x, self.y, self.f2_power, 10, self.an, screen, self.color)
		
	def fire2_start(self):
		# метод запускающийся в момент, когда игрок нажал кнопку и пушка начала заряжаться
		self.on = 1
		self.color = RED
		
	def power_up(self):
		# увеличивает величину заряда пока игрок не отпускает кнопку
		if (self.on and self.f2_power <= 100):
			self.f2_power += 2

	def fire2_end(self):
		# игрок отпустил кнопку и произошел выстрел, состоянее пушки вернулось к начальному
		new_ball(self.f2_power * math.cos(self.an), - self.f2_power * math.sin(self.an),
													self.x, self.y, BLACK, 1000 )
		self.f2_power = 10
		self.color = GREY
		self.on = 0

	def move_up_start(self):
		# начинает двигать танк вверх при нажатии на w
		self.w = 1

	def move_down_start(self):
		# начинает двигать танк вниз при нажатии на s
		self.s = 1

	def move_left_start(self):
		# начинает двигать танк влево при нажатии на a
		self.a = 1

	def move_right_start(self):
		# начинает двигать танк вправо при нажатии на d
		self.d = 1


	def moving_up(self):
		# двигает танк вверх при нажатии на w
		if self.w:
			self.y -= 1

	def moving_down(self):
		# двигает танк вниз при нажатии на s
		if self.s:
			self.y += 1

	def moving_left(self):
		# двигает танк влево при нажатии на a
		if self.a:
			self.x -= 1

	def moving_right(self):
		# двигает танк вправо при нажатии на d
		if self.d:
			self.x += 1


	def move_up_stop(self):
		# двигает танк вверх при нажатии на w
		self.w = 0

	def move_down_stop(self):
		# двигает танк вниз при нажатии на s
		self.s = 0

	def move_left_stop(self):
		# начинает двигать танк влево при нажатии на a
		self.a = 0

	def move_right_stop(self):
		# начинает двигать танк вправо при нажатии на d
		self.d = 0

class Ball:
	def __init__(self, vx, vy, x, y, color, time):
		'''
		класс снарядов пушки
		vx, vy - покоординатная скорость снаряда
		x, y - координаты 
		r - радиус снаряда
		time - время жизни снаряда
		death - характеристика мертвого снаряда
		'''
		self.vx = vx
		self.vy = vy
		self.x = x
		self.y = y
		self.r = 10
		self.color = color
		self.time = time
		self.death = 0

	def draw(self):
		# метод обеспечивает зарисовку снарядов в текущий момент времени
		pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)

	def move(self):
		# метод обеспечивает перемещение шариков вместе с соударением об все стенки
		if (self.vx + self.x + self.r >= WIDTH):
			self.vx = - 0.8 * self.vx

		if (self.vx + self.x + self.r <= 0):
			self.vx = - 0.8 * self.vx

		if (self.vy + self.y + self.r >= HEIGHT):
			self.vy = - 0.8 * self.vy

		if (self.vy + self.y + self.r <= 0):
			self.vy = - self.vy

		self.x += self.vx
		self.y += self.vy
		self.vy += g

	def alive(self):
		if self.time > 0:
			self.time -= 1
		else:
			self.death = 1
			return self.death

	def hittest(self, obj):
		'''
		Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

		Args:
			obj: Обьект, с которым проверяется столкновение.
		Returns:
			Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
		'''
		if((self.x - obj.x) ** 2 + (self.y - obj.y) ** 2 <= (self.r + obj.r) ** 2):
			return True
		else:
			return False


'''
class Target_Level1(Ball):
	def hittest(self, Targets, Balls):
		for i, el in enumerate(Targets):

'''



'''
class Target:
	def __init__(self, vx = 0, vy = 10):
		self.alive = 1
		self.x = HEIGHT - 50
		self.y = randint(50, HEIGHT - 50)
		self.vx = vx
		self.vy = vy
		self.r = 15
		self.color = RED

	def draw(self):
		pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)

	def move(self):
		# метод обеспечивает перемещение цели вместе с соударением об все стенки
		if (self.vx + self.x + self.r >= WIDTH):
			self.vx = - 0.8 * self.vx

		if (self.vx + self.x + self.r <= 0):
			self.vx = - 0.8 * self.vx

		if (self.vy + self.y + self.r >= HEIGHT):
			self.vy = - 0.8 * self.vy

		if (self.vy + self.y + self.r <= 0):
			self.vy = - self.vy

		self.x += self.vx
		self.y += self.vy
		self.vy += g

class level1_Target(Target):
	def __init__(self, vx = 0, vy = 10):
		super().__init__(vx, vy)

class level2_Target:
	def __init__(self, vx = randint(-10, 10), vy = randint(-10, 10)):
		super().__init__(vx, vy)

'''

gun = Gun()


while not Finished:

	screen.fill(WHITE)
	gun.draw()
	gun.power_up()
	#target.draw()
	#target.move()

	for i, el in enumerate(Balls):
		el.move()
		el.draw()
		el.alive()

		if el.alive():
			Balls.pop(i)
		#if el.hittest(target):
		#	points += 1
		#	if points >= 5:
		#		new_target_2()
		#	else:
		#		new_target_1()


	gun.moving_up()
	gun.moving_down()
	gun.moving_left()
	gun.moving_right()



	pygame.display.update()

	clock.tick(FPS)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			Finished = True
		elif event.type == pygame.MOUSEBUTTONDOWN:
			gun.fire2_start()

		elif event.type == pygame.MOUSEBUTTONUP:
			gun.fire2_end()

		elif event.type == pygame.MOUSEMOTION:
			gun.targetting(event)

		if event.type == pygame.KEYDOWN:
			if event.unicode == 'w':
				gun.move_up_start()

			elif event.unicode == 's':
				gun.move_down_start()

			elif event.unicode == 'd':
				gun.move_right_start()

			elif event.unicode == 'a':
				gun.move_left_start()

		if event.type == pygame.KEYUP:
			if event.unicode == 'w':
				gun.move_up_stop()

			elif event.unicode == 's':	
				gun.move_down_stop()

			elif event.unicode == 'd':
				gun.move_right_stop()

			elif event.unicode == 'a':
				gun.move_left_stop()

