import pygame
import math 
from random import choice
from random import randint

pygame.font.init()

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

font1 = pygame.font.Font(None, 50)


Tick = FPS
Balls = [] # массив снарядов присутствующих на карте
score = 0 
Targets1 = [] # массив целей первого уровня
Targets2 = [] # массив бомб второго уровня

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

def new_bomb(x, y):
	'''
	создает новую бомбу - шар класса Ball
	падает из самолета(мишень второго уровня)
	принимает на вход текущее положение самолета x, y
	'''
	bomb = Ball(randint(-5, 5), 0, x, y, GREEN, 500)
	Targets2.append(bomb)

def new_Targets1_lvl1():
	'''
	создает мишень первого уровня - шарик(подкласс Ball)
	'''
	target1 = Target_Level1(randint(-5, 5),randint(-5, 5),
							randint(WIDTH/2, WIDTH), randint(0, HEIGHT), RED, 999999)
	Targets1.append(target1)


def new_Targets2_lvl2():
	'''
	создает мишень второго уровня - самолет
	подкласс мишени первого уровня
	'''
	target2 = Target_Level2(15, 0, randint(0, WIDTH), randint(50, 150), BLUE, 999999)
	Targets2.append(target2)


class Gun:

	def __init__(self):
		'''
		класс пушки 
		x, y - координаты нижней вершины пушки 
		an - угол наклона ствола пушки к горизонту
		f2_power - величина заряда пушки
		on - если значение 1 значит пушка в процессе зарядки
		   - если значение 0 значит пушка бездействует
		live - жизни пушки(игрока)

		w, a, s, d - обеспечит движение танка при нажатии на эти клавиши

		'''
		self.x = 20
		self.y = 450
		self.an = 1
		self.f2_power = 10
		self.on = 0
		self.live = 3
		
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
		self.live = 3

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
		# удаление старых шаров
		if self.time > 0:
			self.time -= 1
		else:
			self.death = 1
			return self.death

	def hit_a_tank(self, x, y):
		# проверка на попадание шаркика в прямоугольник
		if ((self.x + self.r > x - 20 and self.x + self.r < x + 20) and
			(self.y + self.r > y and self.y + self.r < y + 20)):
			return True

		elif ((self.x + self.r > x - 20 and self.x + self.r < x + 20) and
			(self.y - self.r > y and self.y - self.r < y + 20)):
			return True

		elif ((self.x - self.r > x - 20 and self.x - self.r < x + 20) and 
			(self.y + self.r > y and self.y + self.r < y + 20)):
			return True

		elif ((self.x - self.r > x - 20 and self.x - self.r < x + 20) and
			(self.y - self.r > y and self.y - self.r < y + 20)):
			return True

		else:
			return False


class Target_Level1(Ball):

	def hittest(self, Balls, score):
		# проверка на попадание снаряда пушки в шарик из массива мишеней
			for i, el in enumerate(Balls):
				if (self.x - el.x)**2 + (self.y - el.y)**2 <= (self.r + el.r)**2:
					return True

	def move(self):
		# движение шариков но без гравитации
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

class Target_Level2(Ball):

	def draw(self):
		# рисует самолет(прямоугольник)
		pygame.draw.polygon(screen, self.color, [(self.x + 2 * self.r, self.y + self.r),
												(self.x - 2 * self.r, self.y + self.r), 
												(self.x - 2 * self.r, self.y - self.r),
												(self.x + 2 * self.r, self.y - self.r)])

	def create_bomb(self):
		# метод вызывает функцию создания бомбы
		new_bomb(self.x, self.y)


	def move(self):
		# движение самолета без гравитации
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


gun = Gun() # создание пушки (то чем управляет игрок)


for i in range(5):			# создали мишени первого уровня
		new_Targets1_lvl1()
'''
создаем мишень второго уровня - свамолет,
отобразится на экране, когда умрут все цели первого уровня
'''
plane = Target_Level2(15, 0, randint(0, WIDTH), randint(50, 150), BLUE, 999999) 


while not Finished:
	
	if gun.live == 0:
		Finished = True

	if plane.live == 0:
		Finished = True
	
	screen.fill(WHITE)
	gun.draw()
	gun.power_up()

	score_text = font1.render('Your score: ' + str(score), False, BLACK)
	screen.blit(score_text, (40, 10))

	for i, el in enumerate(Balls):
		# движение снарядов танка
		el.move()
		el.draw()

		if el.alive():
			Balls.pop(i)
	
	if score < 5:
		# если очков меньше 5 то на экране только цели первого уровня
		for i, el in enumerate(Targets1):
			el.move()
			el.draw()

		for i, el in enumerate(Targets1):
			if el.hittest(Balls, score):
				Targets1.pop(i)
				score += 1

	if score >= 5:
		'''
		если достигли 5 очков 
		появляется противник второго уровня - самолет
		каждые 30 тиков - 1 секудна он сбрасявает бомбу
		бомба может уменьшать здоровье танка при попадании
		'''

		plane.draw()
		plane.move()
		Tick -= 1
		
		if Tick == 0:
			plane.create_bomb()
			Tick = FPS


		for i, el in enumerate(Targets2):
			el.draw()
			el.move()
			
		for i, el in enumerate(Targets2):
			
			if el.hit_a_tank(gun.x, gun.y): 
				gun.live -= 1
				Targets2.pop(i)

		for i, el in enumerate(Balls):
			if el.hit_a_tank(plane.x, plane.y):
				plane.live -= 1
				print(1)
				Balls.pop(i)
				score += 2
			
	# движение танка по клавишам wasd
	
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
